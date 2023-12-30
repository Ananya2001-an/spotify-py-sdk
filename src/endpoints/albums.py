from .endpoints_base import EndpointsBase
from typing import Optional, Union
from src.types import *


class Albums(EndpointsBase):

    def __init__(self, api):
        super().__init__(api)

    def get(self, id_or_ids: Union[str, list[str]], market: Optional[MARKET] = None):
        if type(id_or_ids) is str:
            params = EndpointsBase.params_for({"market": market})
            album = self.get_request(f"albums/{id_or_ids}{params}")
            return album

        params = EndpointsBase.params_for({"ids": id_or_ids, "market": market})
        response = self.get_request(f"albums{params}")
        return response["albums"]

    def tracks(self, album_id: str, market: Optional[MARKET] = None,
               limit: Optional[int] = None, offset: Optional[int] = None):
        params = EndpointsBase.params_for({"market": market, "limit": limit, "offset": offset})
        return self.get_request(f"albums/{album_id}/tracks{params}")
