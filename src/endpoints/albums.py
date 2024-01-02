from .endpoints_base import EndpointsBase
from typing import Optional, Union
from src.types import *
import asyncio

class Albums(EndpointsBase):
    """Make calls to the Albums api endpoint
    """

    def __init__(self, api):
        """Constructor method
        """
        super().__init__(api)

    def _get_sync(self, id_or_ids: Union[str, list[str]], market: Optional[MARKET] = None):
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

    async def _get_async(self, id_or_ids: Union[str, list[str]], market: Optional[MARKET] = None):
        """Get albums by providing album id

        :param id_or_ids: pass a single id or a list of ids
        """
        if type(id_or_ids) is str:
            params = EndpointsBase.params_for({"market": market})
            album = await self.get_request(f"albums/{id_or_ids}{params}")
            return album

        params = EndpointsBase.params_for({"ids": id_or_ids, "market": market})
        response = await self.get_request(f"albums{params}")
        return response["albums"]

    def get(self, id_or_ids: Union[str, list[str]], market: Optional[MARKET] = None):
        """Get albums by providing album id

        :param id_or_ids: pass a single id or a list of ids
        """
        if asyncio.get_event_loop().is_running():
            return asyncio.ensure_future(self._get_async(id_or_ids, market))
        else:
            return self._get_sync(id_or_ids, market)

    def _tracks_sync(self, album_id: str, market: Optional[MARKET] = None,
                     limit: Optional[int] = None, offset: Optional[int] = None):
        """Synchronously get tracks for the given Album"""
        params = EndpointsBase.params_for({"market": market, "limit": limit, "offset": offset})
        return self.get_request(f"albums/{album_id}/tracks{params}")

    async def _tracks_async(self, album_id: str, market: Optional[MARKET] = None,
                            limit: Optional[int] = None, offset: Optional[int] = None):
        """Asynchronously get tracks for the given Album"""
        params = EndpointsBase.params_for({"market": market, "limit": limit, "offset": offset})
        return await self.get_request(f"albums/{album_id}/tracks{params}")

    def tracks(self, album_id: str, market: Optional[MARKET] = None,
               limit: Optional[int] = None, offset: Optional[int] = None):
        """
        Get tracks for the given Album. Determines if the call should be async or sync.
        :param album_id: pass album id
        """
        if asyncio.get_event_loop().is_running():
            return asyncio.ensure_future(self._tracks_async(album_id, market, limit, offset))
        else:
            return self._tracks_sync(album_id, market, limit, offset)

