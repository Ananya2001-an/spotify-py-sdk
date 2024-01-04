from typing import Union

from .endpoints_base import EndpointsBase
from src.types import *
import asyncio


class Episodes(EndpointsBase):
    """Make calls to the episodes endpoint."""

    def __init__(self, api):
        """Constructor method"""
        super().__init__(api)

    async def _get_async(self, id_or_ids: Union[str, list[str]], market: MARKET):
        """async Get episodes by ids

        :param id_or_ids: pass single id or a list of ids
        :param market: pass market area like "GB"
        """
        if type(id_or_ids) is str:
            params = EndpointsBase.params_for({"market": market})
            album = await self.get_request(f"episodes/{id_or_ids}{params}")
            return album

        params = EndpointsBase.params_for({"ids": id_or_ids, "market": market})
        response = await self.get_request(f"episodes{params}")
        return response["episodes"]

    def _get_sync(self, id_or_ids: Union[str, list[str]], market: MARKET):
        """sync Get episodes by ids

        :param id_or_ids: pass single id or a list of ids
        :param market: pass market area like "GB"
        """
        if type(id_or_ids) is str:
            params = EndpointsBase.params_for({"market": market})
            album = self.get_request(f"episodes/{id_or_ids}{params}")
            return album

        params = EndpointsBase.params_for({"ids": id_or_ids, "market": market})
        response = self.get_request(f"episodes{params}")
        return response["episodes"]

    def get(self, id_or_ids: Union[str, list[str]], market: MARKET):
        """Get episodes by ids

        :param id_or_ids: pass single id or a list of ids
        :param market: pass market area like "GB"
        """
        if asyncio.get_event_loop().is_running():
            return asyncio.ensure_future(self._get_async(id_or_ids, market))
        else:
            return self._get_sync(id_or_ids, market)
