from .endpoints_base import EndpointsBase
from src.types import *


class RemovePlaylistItemsRequest:
    def __init__(self, tracks: list[dict[str]], snapshot_id: Optional[str] = None):
        self.tracks = tracks
        self.snapshot_id = snapshot_id


class UpdatePlaylistItemsRequest:
    def __init__(self, uris: Optional[list[str]] = None, range_start: Optional[int] = None, insert_before: Optional[int] = None, range_length: Optional[int] = None, snapshot_id: Optional[str] = None):
        self.uris = uris
        self.range_start = range_start
        self.insert_before = insert_before
        self.range_length = range_length
        self.snapshot_id = snapshot_id


class ChangePlaylistDetailsRequest:
    def __init__(self, name: Optional[str] = None, public: Optional[bool] = None, collaborative: Optional[bool] = None, description: Optional[str] = None):
        self.name = name
        self.public = public
        self.collaborative = collaborative
        self.description = description


class CreatePlaylistRequest:
    def __init__(self, name: str, public: Optional[bool] = None, collaborative: Optional[bool] = None, description: Optional[str] = None):
        self.name = name
        self.public = public
        self.collaborative = collaborative
        self.description = description


class Playlists(EndpointsBase):
    def __init__(self, api):
        super().__init__(api)

    def get_playlist(self, playlist_id: str, market: Optional[MARKET] = None, fields: Optional[str] = None, additional_types: Optional[list[QueryAdditionalTypes]] = None):
        params = EndpointsBase.params_for({"market": market, "fields": fields, "additional_types": ",".join(additional_types) if additional_types else None})
        return self.get_request(f"playlists/{playlist_id}{params}")

    def get_playlist_items(self, playlist_id: str, market: Optional[MARKET] = None, fields: Optional[str] = None, limit: Optional[int] = None, offset: Optional[int] = None, additional_types: Optional[list[QueryAdditionalTypes]] = None):
        params = EndpointsBase.params_for({"market": market, "fields": fields, "limit": limit, "offset": offset, "additional_types": ",".join(
            additional_types) if additional_types else None})
        return self.get_request(f"playlists/{playlist_id}/tracks{params}")

    def change_playlist_details(self, playlist_id: str, request: ChangePlaylistDetailsRequest):
        self.put_request(f"playlists/{playlist_id}", request)

    def move_playlist_items(self, playlist_id: str, range_start: int, range_length: int, move_to_position: int):
        return self.update_playlist_items(playlist_id, UpdatePlaylistItemsRequest(range_start, move_to_position, range_length))

    def update_playlist_items(self, playlist_id: str, request: UpdatePlaylistItemsRequest):
        return self.put_request(f"playlists/{playlist_id}/tracks", request)

    def add_items_to_playlist(self, playlist_id: str, uris: Optional[list[str]] = None, position: Optional[int] = None):
        self.post_request(f"playlists/{playlist_id}/tracks", {
            "position": position,
            "uris": uris
        })

    def remove_items_from_playlist(self, playlist_id: str, request: RemovePlaylistItemsRequest):
        self.delete_request(f"playlists/{playlist_id}/tracks", request)

    def get_users_playlists(self, user_id: str, limit: Optional[int] = None, offset: Optional[int] = None):
        params = EndpointsBase.params_for({"limit": limit, "offset": offset})
        return self.get_request(f"users/{user_id}/playlists{params}")

    def create_playlist(self, user_id: str, request: CreatePlaylistRequest):
        return self.post_request(f"users/{user_id}/playlists", request)

    def get_playlist_cover_image(self, playlist_id: str):
        return self.get_request(f"playlists/{playlist_id}/images")

    # TODO
    # def add_custom_playlist_cover_image(self, playlist_id: str, image_data: Union[str]):

    def add_custom_playlist_cover_image_from_base64_string(self, playlist_id: str, base64_encoded_jpeg: str):
        self.put_request(f"playlists/{playlist_id}/images", base64_encoded_jpeg, "image/jpeg")







