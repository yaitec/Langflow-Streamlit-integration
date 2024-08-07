from typing import Optional
from pydantic import BaseModel, Field
from langflow.services.deps import get_settings_service


streamlit_frontend_port = get_settings_service().settings.streamlit_frontend_port


class ChatModel(BaseModel):
    title: str =  "Welcome to My Streamlit Chat Application"
    welcome_msg: str = "Hello human, welcome to the digital world. Feel free to ask questions; I am ready to help you."
    write_speed: float = 0.05
    input_msg: str = "Ask some question..."
    ai_avatar: Optional[str] = None
    user_avatar: Optional[str] = None
    port: int = streamlit_frontend_port


class ChatMessageModel(BaseModel):
    role: str
    content: str
    type: str = Field("text", pattern="text|image")
