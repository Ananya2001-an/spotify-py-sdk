from .endpoints_base import EndpointsBase
from src.types import *


class Users(EndpointsBase):
    def __init__(self, api):
        super().__init__(api)

    def profile(self, user_id: str):
        return self.get_request(f"users/{user_id}")

