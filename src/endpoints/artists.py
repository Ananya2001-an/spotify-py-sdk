from typing import Optional, Union
from src.types import *
from .endpoints_base import EndpointsBase


class Artists(EndpointsBase):

    def __init__(self, api):
        super().__init__(api)

    def get(self, id_or_ids: Union[str, list[str]]):
        if type(id_or_ids) is str:
            artist = self.get_request(f"artists/{id_or_ids}")
            return artist

        params = EndpointsBase.params_for({"ids": id_or_ids})
        response = self.get_request(f"artists{params}")
        return response.artists

    def albums(self, id: str, include_groups: Optional[str] = None, market: Optional[MARKET] = None, limit: Optional[int] = None, offset: Optional[int] = None):
        params = EndpointsBase.params_for({"include_groups": include_groups, "market": market, "limit": limit, "offset": offset})
        return self.get_request(f"artists/{id}/albums{params}")

    def top_tracks(self, id: str, market: MARKET):
        # market is needed here though mentioned optional in the docs
        params = EndpointsBase.params_for({"market": market})
        return self.get_request(f"artists/{id}/top-tracks{params}")

    def related_artists(self, id: str):
        return self.get_request(f"artists/{id}/related-artists")