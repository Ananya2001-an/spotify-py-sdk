from .endpoints_base import EndpointsBase
from src.types import *


class Markets(EndpointsBase):
    """Make calls to the markets endpoint
    """
    def __init__(self, api):
        """Constructor method
        """
        super().__init__(api)

    def get_available_markets(self):
        """Get all available_markets
        """
        return self.get_request("markets")

