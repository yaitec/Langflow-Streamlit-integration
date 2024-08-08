from typing import Optional
from langflow.custom import Component
from langflow.schema.message import Message, Data
from langflow.inputs import MessageTextInput, IntInput
import sys
from json import loads, dumps

class Listen(Component):
    display_name = "Listen"
    description = "Retrieve the next Streamlit chat message (webhook)."
    icon = "Streamlit"
    response = None

    inputs = [
        IntInput(
            name="timeout",
            display_name="Timeout",
            info="Timeout in seconds",
            value=120,
            required=True
        ),
        IntInput(
            name="port",
            display_name="Port",
            info="Port that Streamlit API is Running",
            advanced=True,
            value=7881,
            required=True
        ),
        StrInput(
            name="title",
            display_name="Title",
            value="Welcome to My Streamlit Chat Application",
            info="The title of chat template",
            required=False,
            advanced=True
        ),
        StrInput(
            name="welcome_msg",
            display_name="Welcome Message",
            required=True,
            advanced=True
        ),
        StrInput(
            name="input_msg",
            display_name="Input Message",
            required=True,
            value="A Text Input Placeholder",
            advanced=True
        ),
        FloatInput(
            name="write_speed",
            display_name="Write Speed",
            value=0.2,
            required=True,
            advanced=True
        ),
        MessageTextInput(
            name="ai_avatar",
            display_name="AI Avatar",
            value="🤖",
            info="It must be an emoji",
            required=False,
            advanced=True
        ),
        MessageTextInput(
            name="user_avatar",
            display_name="User Avatar",
            value="",
            required=False,
            advanced=True
        ),
    ]

    outputs = [
        Output(display_name="Session ID", name="session_id", method="session_id_response"),
        Output(display_name="Message Content", name="message_content", method="message_content_response"),
        Output(display_name="History", name="chat history", method="chat_history_response"),
    ]

    def get_api_response(self):
        import requests
        body = {
            "title": self.title,
            "welcome_msg": self.welcome_msg,
            "input_msg": self.input_msg,
            "write_speed": self.write_speed,
        }
        if self.ai_avatar: body["ai_avatar"] = self.ai_avatar
        if self.user_avatar: body["user_avatar"] = self.user_avatar
        resp = requests.post(f"http://localhost:{self.port}/api/v1/chats", json=body)
        resp = requests.get(f"http://localhost:{self.port}/api/v1/listen/message?timeout={self.timeout}")
        if resp.status_code == 200:
            self.response = loads(resp.content)
            return self.response
        else:
            raise Exception("Timeout exception")
    
    def session_id_response(self) -> Message:
        if self.response is not None:
            return Message(
                text=self.response["session_id"],
            )
        return Message(
            text=self.get_api_response()["session_id"],
        )

    def message_content_response(self) -> Message:
        if self.response is not None:
            return Message(
                text=self.response["content"],
                sender="User",
            )
        return Message(
            text=self.get_api_response()["content"],
        )

    def chat_history_response(self) -> Data:
        if self.response is not None:
            return self.response["history"]
        return self.get_api_response()["history"]