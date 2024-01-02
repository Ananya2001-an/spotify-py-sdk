import json
import requests
import httpx
import asyncio
import inspect
from typing import Optional, Union, Literal
from .auth.access_token_manager import AccessTokenManager
from .types import *
from requests import HTTPError
from .endpoints import *


class SpotifyApi:
    """Create an api instance and call the various endpoint methods.

    :param client_id: Client_ID for your app
    :type client_id: str
    :param client_secret: Client_Secret for your app
    :type client_secret: str
    :param config: pass :class:`SdkConfig` instance, defaults to None
    :type config: :class:`SdkConfig`, optional
    """
    _root_url: str = "https://api.spotify.com/v1/"

    def __init__(self, client_id: str, client_secret: str, config: Optional[SdkConfig] = None):
        """Constructor method
        """
        self.access_token_manager: AccessTokenManager = AccessTokenManager(client_id, client_secret)
        self.sdk_config: Optional[SdkConfig] = config
        self.albums: Albums = Albums(self)
        self.artists: Artists = Artists(self)
        self.audiobooks: Audiobooks = Audiobooks(self)
        self.browse: Browse = Browse(self)
        self.chapters: Chapters = Chapters(self)
        self.episodes: Episodes = Episodes(self)
        self.recommendations: Recommendations = Recommendations(self)
        self.markets: Markets = Markets(self)
        # self.player: Player = Player(self) # need different auth strategy; yet to be implemented
        self.playlists: Playlists = Playlists(self)
        self.shows: Shows = Shows(self)
        self.tracks: Tracks = Tracks(self)
        self.users: Users = Users(self)
        self.search: Search = Search(self)
        # self.current_user: CurrentUser = CurrentUser(self) # need different auth strategy; yet to be implemented

    @classmethod
    async def _fetch_results_async(cls, url: str, opts: dict):
        """async signature for Fetch results by making a request to the given URL"""
        async with httpx.AsyncClient() as client:
            try:
                response = await client.request(
                    method=opts["method"],
                    url=url,
                    headers=opts["headers"],
                    data=opts["body"]
                )
                return response.json()
            except httpx.HTTPError as e:
                raise Exception(f"Failed to fetch result! {e}")

    @classmethod
    def _fetch_results_sync(cls, url: str, opts: dict):
        """async signature for Fetch results by making a request to the given URL"""
        with httpx.Client() as client:
            try:
                response = client.request(
                    method=opts["method"],
                    url=url,
                    headers=opts["headers"],
                    data=opts["body"]
                )
                return response.json()
            except httpx.HTTPError as e:
                raise Exception(f"Failed to fetch result! {e}")
s
    @classmethod
    def fetch_results(cls, url: str, opts: dict):
        """Fetch results by making a request to the given URL"""
        if asyncio.get_event_loop().is_running():
            return asyncio.ensure_future(cls._fetch_results_async(url, opts))
        else:
            return cls._fetch_results_sync(url, opts)


    def make_request(self, method: Literal["GET", "POST", "PUT", "DELETE"], url: str, body: Optional[any] = None,
                     content_type: Optional[str] = None):
        """Get access token and make necessary request call to the api endpoint
        """
        try:
            access_token = self.access_token_manager.get_access_token()
        except HTTPError as e:
            raise "Access Token not available! Authenticate again."

        full_url = SpotifyApi._root_url + url
        opts = {
            "method": method,
            "headers": {
                "Authorization": f"Bearer {access_token}",
                "Content-Type": content_type if content_type else "application/json"
            },
            "body": json.dumps(body) if body and type(body) is not str else body
        }

        try:
            if self.sdk_config:
                if self.sdk_config.before_request:
                    self.sdk_config.before_request(full_url, opts)
                if self.sdk_config.fetch:
                    result = self.sdk_config.fetch(full_url, opts)
                else:
                    result = SpotifyApi.fetch_results(full_url, opts)
                if self.sdk_config.after_request:
                    self.sdk_config.after_request(full_url, opts, result)
                return result

            return SpotifyApi.fetch_results(full_url, opts)
        except (HTTPError, ValueError, InterruptedError) as e:
            raise e
            # handled = self.sdk_config.error_handler.handleErrors(e)
            # if not handled:
            #     raise Exception("Failed to make request! Try again.")

