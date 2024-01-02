from .endpoints_base import EndpointsBase
from typing import Optional, Union
from src.types import *
import asyncio


class Audiobooks(EndpointsBase):
    """Make calls to the Audiobooks api endpoint
    """
    def __init__(self, api):
        """Constructor method
        """
        super().__init__(api)

    async def _get_async(self, id_or_ids: Union[str, list[str]], market: Optional[MARKET] = None):
        """Asynchronously get audiobooks by providing id"""
        if isinstance(id_or_ids, str):
            params = EndpointsBase.params_for({"market": market})
            return await self.get_request(f"audiobooks/{id_or_ids}{params}")

        params = EndpointsBase.params_for({"ids": id_or_ids, "market": market})
        response = await self.get_request(f"audiobooks{params}")
        return response["audiobooks"]

    def _get_sync(self, id_or_ids: Union[str, list[str]], market: Optional[MARKET] = None):
        """Synchronously get audiobooks by providing id"""
        if isinstance(id_or_ids, str):
            params = EndpointsBase.params_for({"market": market})
            return self.get_request(f"audiobooks/{id_or_ids}{params}")

        params = EndpointsBase.params_for({"ids": id_or_ids, "market": market})
        response = self.get_request(f"audiobooks{params}")
        return response["audiobooks"]

    def get(self, id_or_ids: Union[str, list[str]], market: Optional[MARKET] = None):
        """Get audiobooks by providing id"""
        if asyncio.get_event_loop().is_running():
            return asyncio.ensure_future(self._get_async(id_or_ids, market))
        else:
            return self._get_sync(id_or_ids, market)

        # Chapters method

    async def _get_audiobook_chapters_async(self, id: str, market: Optional[MARKET] = None, limit: Optional[int] = None,
                                            offset: Optional[int] = None):
        """Asynchronously get chapters of an audiobook"""
        params = EndpointsBase.params_for({"market": market, "limit": limit, "offset": offset})
        return await self.get_request(f"audiobooks/{id}/chapters{params}")

    def _get_audiobook_chapters_sync(self, id: str, market: Optional[MARKET] = None, limit: Optional[int] = None,
                                     offset: Optional[int] = None):
        """Synchronously get chapters of an audiobook"""
        params = EndpointsBase.params_for({"market": market, "limit": limit, "offset": offset})
        return self.get_request(f"audiobooks/{id}/chapters{params}")

    def get_audiobook_chapters(self, id: str, market: Optional[MARKET] = None, limit: Optional[int] = None,
                               offset: Optional[int] = None):
        """Get chapters of an audiobook"""
        if asyncio.get_event_loop().is_running():
            return asyncio.ensure_future(self._get_audiobook_chapters_async(id, market, limit, offset))
        else:
            return self._get_audiobook_chapters_sync(id, market, limit, offset)