from typing import Union

from .endpoints_base import EndpointsBase
from src.types import *


class Episodes(EndpointsBase):
    """Make calls to the episodes endpoint.
    """
    def __init__(self, api):
        """Constructor method
        """
        super().__init__(api)

    def get(self, id_or_ids: Union[str, list[str]], market: MARKET):
        """Get episodes by ids

        :param id_or_ids: pass single id or a list of ids
        :param market: pass market area like "GB"
        """
        if type(id_or_ids) is str:
            params = EndpointsBase.params_for({"market": market})
            album = self.get_request(f"episodes/{id_or_ids}{params}")
            return album

        params = EndpointsBase.params_for({"ids": id_or_ids, "market": market})
        response = self.get_request(f"episodes{params}")
        return response["episodes"]

