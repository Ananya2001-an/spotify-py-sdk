from typing import Union

from .endpoints_base import EndpointsBase
from src.types import *
import asyncio


class Tracks(EndpointsBase):
    def __init__(self, api):
        super().__init__(api)

    async def _get_async(
        self, id_or_ids: Union[str, list[str]], market: Optional[MARKET] = None
    ):
        if type(id_or_ids) is str:
            params = EndpointsBase.params_for({"market": market})
            return await self.get_request(f"tracks/{id_or_ids}{params}")

        params = EndpointsBase.params_for({"ids": id_or_ids, "market": market})
        response = await self.get_request(f"tracks{params}")
        return response["tracks"]

    def _get_sync(
        self, id_or_ids: Union[str, list[str]], market: Optional[MARKET] = None
    ):
        if type(id_or_ids) is str:
            params = EndpointsBase.params_for({"market": market})
            return self.get_request(f"tracks/{id_or_ids}{params}")

        params = EndpointsBase.params_for({"ids": id_or_ids, "market": market})
        response = self.get_request(f"tracks{params}")
        return response["tracks"]

    def get(self, id_or_ids: Union[str, list[str]], market: Optional[MARKET] = None):
        if asyncio.get_event_loop().is_running():
            return self._get_async(id_or_ids, market)
        else:
            return self._get_sync(id_or_ids, market)

    async def _audio_features_async(self, id_or_ids: Union[str, list[str]]):
        if type(id_or_ids) is str:
            return await self.get_request(f"audio-features/{id_or_ids}")

        params = EndpointsBase.params_for({"ids": id_or_ids})
        response = await self.get_request(f"audio-features{params}")
        return response["audio_features"]

    def _audio_features_sync(self, id_or_ids: Union[str, list[str]]):
        if type(id_or_ids) is str:
            return self.get_request(f"audio-features/{id_or_ids}")

        params = EndpointsBase.params_for({"ids": id_or_ids})
        response = self.get_request(f"audio-features{params}")
        return response["audio_features"]

    def audio_features(self, id_or_ids: Union[str, list[str]]):
        if asyncio.get_event_loop().is_running():
            return self._audio_features_async(id_or_ids)
        else:
            return self._audio_features_sync(id_or_ids)

    def audio_analysis(self, id: str):
        return self.get_request(f"audio-analysis/{id}")
