import json
import requests
from typing import Optional, Union, Literal
from .auth.access_token_manager import AccessTokenManager
from .types import *
from requests import HTTPError
from .endpoints import *


class SpotifyApi:
    _root_url: str = "https://api.spotify.com/v1/"

    # using client credentials auth strategy
    def __init__(self, client_id: str, client_secret: str, config: Optional[SdkConfig] = None):
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
        # self.player: Player = Player(self)
        self.playlists: Playlists = Playlists(self)
        self.shows: Shows = Shows(self)
        self.tracks: Tracks = Tracks(self)
        self.users: Users = Users(self)
        self.search: Search = Search(self)
        # self.current_user: CurrentUser = CurrentUser(self)

    @classmethod
    def fetch_results(cls, url: str, opts: dict):
        try:
            result = requests.request(method=opts["method"], url=url, headers=opts["headers"], data=opts["body"])
            return result.json()
        except HTTPError as e:
            raise f"Failed to fetch result! {e}"

    def make_request(self, method: Literal["GET", "POST", "PUT", "DELETE"], url: str, body: Optional[any] = None,
                     content_type: Optional[str] = None):
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

