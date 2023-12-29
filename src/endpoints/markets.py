from .endpoints_base import EndpointsBase
from src.types import *


class Markets(EndpointsBase):
    def __init__(self, api):
        super().__init__(api)

    def get_available_markets(self):
        return self.get_request("markets")

