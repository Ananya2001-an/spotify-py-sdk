from typing import Union

from .endpoints_base import EndpointsBase
from src.types import *


class Chapters(EndpointsBase):

    def __init__(self, api):
        super().__init__(api)

    def get(self, id_or_ids: Union[str, list[str]], market: CHAPTER_MARKET):
        if type(id_or_ids) is str:
            params = EndpointsBase.params_for({"market": market})
            return self.get_request(f"chapters/{id_or_ids}{params}")

        params = EndpointsBase.params_for({"ids": id_or_ids, "market": market})
        response = self.get_request(f"chapters{params}")
        return response["chapters"]
