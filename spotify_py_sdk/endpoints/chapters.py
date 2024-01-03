from typing import Union

from .endpoints_base import EndpointsBase
from spotify_py_sdk.types import *


class Chapters(EndpointsBase):
    """Make calls to the chapters api endpoint
    """
    def __init__(self, api):
        """Constructor method
        """
        super().__init__(api)

    def get(self, id_or_ids: Union[str, list[str]], market: CHAPTER_MARKET):
        """Get chapters

        :param id_or_ids: pass single id or a list of ids
        :param market: pass market like "GB"
        """
        if type(id_or_ids) is str:
            params = EndpointsBase.params_for({"market": market})
            return self.get_request(f"chapters/{id_or_ids}{params}")

        params = EndpointsBase.params_for({"ids": id_or_ids, "market": market})
        response = self.get_request(f"chapters{params}")
        return response["chapters"]
