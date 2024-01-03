from typing import Union

from .endpoints_base import EndpointsBase
from spotify_py_sdk.types import *


class Search(EndpointsBase):
    def __init__(self, api):
        super().__init__(api)

    def execute(self, q: str, type: list[ITEM_TYPES], market: Optional[MARKET] = None, limit: Optional[int] = None, offset: Optional[int] = None, include_external: Optional[str] = None):
        params = EndpointsBase.params_for({
            "q": q,
            "type": type,
            "market": market,
            "limit": limit,
            "offset": offset,
            "include_external": include_external
        })
        return self.get_request(f"search{params}")

