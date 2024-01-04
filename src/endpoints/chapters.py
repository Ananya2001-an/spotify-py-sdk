from typing import Union

from .endpoints_base import EndpointsBase
from src.types import *
import asyncio


class Chapters(EndpointsBase):
    """Make calls to the chapters api endpoint"""

    def __init__(self, api):
        """Constructor method"""
        super().__init__(api)

    async def _get_async(
        self, id_or_ids: Union[str, list[str]], market: CHAPTER_MARKET
    ):
        """Asynchronously get chapters"""
        if isinstance(id_or_ids, str):
            params = EndpointsBase.params_for({"market": market})
            return await self.get_request(f"chapters/{id_or_ids}{params}")

        params = EndpointsBase.params_for({"ids": id_or_ids, "market": market})
        response = await self.get_request(f"chapters{params}")
        return response["chapters"]

    def _get_sync(self, id_or_ids: Union[str, list[str]], market: CHAPTER_MARKET):
        """Synchronously get chapters"""
        if isinstance(id_or_ids, str):
            params = EndpointsBase.params_for({"market": market})
            return self.get_request(f"chapters/{id_or_ids}{params}")

        params = EndpointsBase.params_for({"ids": id_or_ids, "market": market})
        response = self.get_request(f"chapters{params}")
        return response["chapters"]

    def get(self, id_or_ids: Union[str, list[str]], market: CHAPTER_MARKET):
        """Get chapters"""
        if asyncio.get_event_loop().is_running():
            return asyncio.ensure_future(self._get_async(id_or_ids, market))
        else:
            return self._get_sync(id_or_ids, market)
