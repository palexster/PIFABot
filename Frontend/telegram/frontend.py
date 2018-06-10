
from generic import frontend
import os

class TelegramFrontend(Frontend):

    necessary_information = [
        "FE_CLASS",
        "TELEGRAM_TOKEN_ID"
    ]

    def __init__(self):
        self.telegram_token_id = os.get_env("TELEGRAM_TOKEN_ID")



