from .endpoints_base import EndpointsBase
from typing import Optional, Union
from src.types import *


class Audiobooks(EndpointsBase):

    def __init__(self, api):
        super().__init__(api)

    def get(self, id_or_ids: Union[str, list[str]], market: Optional[MARKET] = None):
        if type(id_or_ids) is str:
            params = EndpointsBase.params_for({"market": market})
            return self.get_request(f"audiobooks/{id_or_ids}{params}")

        params = EndpointsBase.params_for({"ids": id_or_ids, "market": market})
        response = self.get_request(f"audiobooks{params}")
        return response["audiobooks"]

    def get_audiobook_chapters(self, id: str, market: Optional[MARKET] = None, limit: Optional[int] = None, offset: Optional[int] = None):
        params = EndpointsBase.params_for({"market": market, "limit": limit, "offset": offset})
        return self.get_request(f"audiobooks/{id}/chapters{params}")
