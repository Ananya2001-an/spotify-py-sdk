from typing import Union

from .endpoints_base import EndpointsBase
from spotify_py_sdk.types import *


class Shows(EndpointsBase):
    def __init__(self, api):
        super().__init__(api)

    def get(self, id_or_ids: Union[str, list[str]], market: MARKET):
        if type(id_or_ids) is str:
            params = EndpointsBase.params_for({"market": market})
            return self.get_request(f"shows/{id_or_ids}{params}")

        params = EndpointsBase.params_for({"ids": id_or_ids, "market": market})
        response = self.get_request(f"shows{params}")
        return response["shows"]

    def episodes(self, id: str, market: Optional[str] = None, limit: Optional[int] = None, offset: Optional[int] = None):
        params = EndpointsBase.params_for({"market": market, "limit": limit, "offset": offset})
        return self.get_request(f"shows/{id}/episodes{params}")

