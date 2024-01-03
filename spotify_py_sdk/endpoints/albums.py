from .endpoints_base import EndpointsBase
from typing import Optional, Union
from spotify_py_sdk.types import *


class Albums(EndpointsBase):
    """Make calls to the Albums api endpoint
    """

    def __init__(self, api):
        """Constructor method
        """
        super().__init__(api)

    def get(self, id_or_ids: Union[str, list[str]], market: Optional[MARKET] = None):
        """Get albums by providing album id

        :param id_or_ids: pass a single id or a list of ids
        """
        if type(id_or_ids) is str:
            params = EndpointsBase.params_for({"market": market})
            album = self.get_request(f"albums/{id_or_ids}{params}")
            return album

        params = EndpointsBase.params_for({"ids": id_or_ids, "market": market})
        response = self.get_request(f"albums{params}")
        return response["albums"]

    def tracks(self, album_id: str, market: Optional[MARKET] = None,
               limit: Optional[int] = None, offset: Optional[int] = None):
        """Get tracks for the given Album

        :param album_id: pass album id
        """
        params = EndpointsBase.params_for({"market": market, "limit": limit, "offset": offset})
        return self.get_request(f"albums/{album_id}/tracks{params}")
