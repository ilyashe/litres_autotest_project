from typing import Literal
from utils import tools
from pydantic_settings import BaseSettings
import os
from dotenv import load_dotenv

Context = Literal['local_emulator', 'bstack']

class Config(BaseSettings):
    context: Context = 'local_emulator'

    bstack_userName: str = ''
    bstack_accessKey: str = ''
    app: str
    platformVersion: str = ''
    deviceName: str = ''
    udid: str = ''
    remote_url: str = ''
    timeout: float = 10.0


def load_config():
    context = os.getenv('context', 'bstack')
    env_path = tools.path_to_env(f'.env.{context}')
    load_dotenv(dotenv_path=env_path)
    if context == 'bstack':
        load_dotenv(dotenv_path=tools.path_to_env('.env'), override=True)

    base_config = Config(_env_file=env_path)
    base_config.context = context
    return base_config


config = load_config()
