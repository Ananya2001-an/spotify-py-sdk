from typing import Optional, Union
from src.types import *
from .endpoints_base import EndpointsBase
import asyncio


class Artists(EndpointsBase):
    """Make calls to the Artists api endpoint
    """
    def __init__(self, api):
        """Constructor method
        """
        super().__init__(api)

    async def _get_async(self, id_or_ids: Union[str, list[str]]):
        """Asynchronously get artists by providing artist id"""
        if isinstance(id_or_ids, str):
            artist = await self.get_request(f"artists/{id_or_ids}")
            return artist

        params = EndpointsBase.params_for({"ids": id_or_ids})
        response = await self.get_request(f"artists{params}")
        return response["artists"]

    def _get_sync(self, id_or_ids: Union[str, list[str]]):
        """Synchronously get artists by providing artist id"""
        if isinstance(id_or_ids, str):
            artist = self.get_request(f"artists/{id_or_ids}")
            return artist

        params = EndpointsBase.params_for({"ids": id_or_ids})
        response = self.get_request(f"artists{params}")
        return response["artists"]

    def get(self, id_or_ids: Union[str, list[str]]):
        """Get artists by providing artist id"""
        if asyncio.get_event_loop().is_running():
            return asyncio.ensure_future(self._get_async(id_or_ids))
        else:
            return self._get_sync(id_or_ids)

    async def _albums_async(self, id: str, include_groups: Optional[str] = None, market: Optional[MARKET] = None,
                            limit: Optional[int] = None, offset: Optional[int] = None):
        """Asynchronously get albums of an artist"""
        params = EndpointsBase.params_for(
            {"include_groups": include_groups, "market": market, "limit": limit, "offset": offset})
        return await self.get_request(f"artists/{id}/albums{params}")

    def _albums_sync(self, id: str, include_groups: Optional[str] = None, market: Optional[MARKET] = None,
                     limit: Optional[int] = None, offset: Optional[int] = None):
        """Synchronously get albums of an artist"""
        params = EndpointsBase.params_for(
            {"include_groups": include_groups, "market": market, "limit": limit, "offset": offset})
        return self.get_request(f"artists/{id}/albums{params}")

    def albums(self, id: str, include_groups: Optional[str] = None, market: Optional[MARKET] = None,
               limit: Optional[int] = None, offset: Optional[int] = None):
        """Get albums of an artist"""
        if asyncio.get_event_loop().is_running():
            return asyncio.ensure_future(self._albums_async(id, include_groups, market, limit, offset))
        else:
            return self._albums_sync(id, include_groups, market, limit, offset)

    # Top Tracks method
    async def _top_tracks_async(self, id: str, market: MARKET):
        """Asynchronously get top tracks of an artist"""
        params = EndpointsBase.params_for({"market": market})
        return await self.get_request(f"artists/{id}/top-tracks{params}")

    def _top_tracks_sync(self, id: str, market: MARKET):
        """Synchronously get top tracks of an artist"""
        params = EndpointsBase.params_for({"market": market})
        return self.get_request(f"artists/{id}/top-tracks{params}")

    def top_tracks(self, id: str, market: MARKET):
        """Get top tracks of an artist"""
        if asyncio.get_event_loop().is_running():
            return asyncio.ensure_future(self._top_tracks_async(id, market))
        else:
            return self._top_tracks_sync(id, market)

    # Related Artists method
    async def _related_artists_async(self, id: str):
        """Asynchronously get related artists"""
        return await self.get_request(f"artists/{id}/related-artists")

    def _related_artists_sync(self, id: str):
        """Synchronously get related artists"""
        return self.get_request(f"artists/{id}/related-artists")

    def related_artists(self, id: str):
        """Get related artists"""
        if asyncio.get_event_loop().is_running():
            return asyncio.ensure_future(self._related_artists_async(id))
        else:
            return self._related_artists_sync(id)