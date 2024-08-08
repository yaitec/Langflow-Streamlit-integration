from langflow.services.deps import get_settings_service
from subprocess import run, PIPE
from loguru import logger
import threading
import sys
import os
import platform


settings = get_settings_service().settings


def check_if_port_is_used_by_program(port, programs=[]):
    if sys.platform.startswith("linux") or sys.platform == "darwin":  # Linux and macOS
        command = f"lsof -i :{port}"
    elif sys.platform == "win32":
        command = f"netstat -ano | findstr :{port}"
    else:
        raise OSError(f"Unsupported platform: {sys.platform}")

    result = run(command, shell=True, stdout=PIPE, stderr=PIPE, text=True).stdout
    if any([program in result for program in programs]):
        return True
    else:
        return False


def kill_process_on_port(port):
    if sys.platform.startswith("linux") or sys.platform == "darwin":  # Linux and macOS
        command = f"fuser -k {port}/tcp"
    elif sys.platform == "win32":
        command = (
            f"netstat -ano | findstr :{port} | " "for /F \"tokens=5\" %P in ('findstr :{port}') do taskkill /F /PID %P"
        )
    else:
        raise OSError(f"Unsupported platform: {sys.platform}")

    result = run(command, shell=True, stdout=PIPE, stderr=PIPE, text=True)
    if result.returncode == 0:
        logger.debug(f"Successfully killed the process using port {port}.")
    else:
        logger.debug(f"Failed to kill the process using port {port}. Error: {result.stderr}")


class StreamlitApplication:
    port = settings.streamlit_frontend_port
    path = settings.streamlit_folder_path

    @classmethod
    def __load_streamlit(cls):
        if not os.path.exists(f"{cls.path}streamlit.py"):
            with open(f"{cls.path}streamlit.py", "w") as file:
                file.write("import streamlit as st")
        else:
            with open(f"{cls.path}streamlit.py", "r+") as file:
                content = file.read()
                if len(content) < 10:
                    file.seek(0)
                    file.write("import streamlit as st\nfrom time import sleep\nwhile True:\n    sleep(2)")
                    file.truncate()

    @classmethod
    def run_streamlit(cls, args):
        if run(
            f"poetry run streamlit run {cls.path}streamlit.py --browser.serverPort {cls.port} --server.port {cls.port} {args}",
            shell=True,
            stdout=PIPE,
        ).returncode != 0:
            exit()

    @classmethod
    def start(cls, args="--server.headless false"):
        if check_if_port_is_used_by_program(cls.port, ["streamlit"]):
            kill_process_on_port(cls.port)
        cls.__load_streamlit()
        streamlit_thread = threading.Thread(target=cls.run_streamlit, args=(args,))
        streamlit_thread.start()

    @classmethod
    def restart(cls):
        kill_process_on_port(cls.port)
        cls.start("--server.headless true")
