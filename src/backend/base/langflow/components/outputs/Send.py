from langflow.custom import Component
from langflow.schema.message import Message
from langflow.inputs import MessageTextInput, DropdownInput, NestedDictInput, IntInput, StrInput, BoolInput
from json import loads, dumps


class Send(Component):
    display_name = "Send"
    description = "Send a streamlit chat message (webhook)."
    icon = "Streamlit"

    inputs = [
        MessageTextInput(
            name="session_id",
            display_name="Session ID",
            info="Session ID of streamlit. For each browser tab that connects to the Streamlit server, a new session is created.",
            placeholder="Enter the session ID",
            value="",
            required=True
        ),
        DropdownInput(
            name="role",
            display_name="Role",
            options=["ai", "user"],
            info="Message sender role.",
            placeholder="Enter the message sender role.",
            value="ai",
            required=True
        ),
        MessageTextInput(
            name="message",
            display_name="Message",
            info="Content of the message that will be sent.",
            value="",
            required=True
        ),
        NestedDictInput(
            name="tweaks",
            display_name="Tweaks",
            info="The tweaks can be used to modify the flow's parameters and components.",
            value={},
            required=True,
            advanced=True
        ),
        IntInput(
            name="port",
            display_name="Port",
            info="Streamlit API Port",
            value=7881,
            required=True,
            advanced=True
        ),
        StrInput(
            name="hostname",
            display_name="hostname",
            info="IP or hostname of Streamlit API",
            value="localhost",
            required=True,
            advanced=True
        ),
        BoolInput(
            name="rerun",
            display_name="Rerun Flow",
            info="If True, run the current flow again",
            value=True,
            required=True,
            advanced=True
        )
    ]

    outputs = [
        Output(display_name="Text", name="text", method="text_response"),
    ]


    async def text_response(self) -> Message:
        import requests
        flow_id = self.vertex.graph.flow_id
        resp = requests.post(f"http://{self.hostname}:{self.port}/api/v1/sessions/{self.session_id}/messages", json={"role": self.role, "content": self.message})
        if resp.status_code == 200:
            self.rerun and await self.run_flow(
                inputs={"input_value": ""}, flow_id=flow_id, tweaks=self.tweaks
            )
            return Message(text=dumps(loads(resp.content)))
        else:
            raise Exception("Timeout exception")
