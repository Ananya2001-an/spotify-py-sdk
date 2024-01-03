from .endpoints_base import EndpointsBase
from spotify_py_sdk.types import *


class QueryRange:
    def __init__(self, timestamp: int, type: Literal["before", "after"]):
        self.timestamp = timestamp
        self.type = type


class Player(EndpointsBase):
    def __init__(self, api):
        super().__init__(api)

    def get_playback_state(self, market: Optional[MARKET] = None, additional_types: Optional[str] = None):
        params = EndpointsBase.params_for({
            "market": market,
            "additional_types": additional_types
        })
        return self.get_request(f"me/player{params}")

    def get_available_devices(self):
        return self.get_request(f"me/player/devices")

    def get_current_playing_track(self, market: Optional[MARKET] = None, additional_types: Optional[str] = None):
        params = EndpointsBase.params_for({
            "market": market,
            "additional_types": additional_types
        })
        return self.get_request(f"me/player/currently-playing{params}")

    def get_recently_played_tracks(self, limit: Optional[int] = None, query_range: Optional[QueryRange] = None):
            param_obj = {"limit": limit}

            if query_range:
                if query_range.type == "before":
                    param_obj["before"] = query_range.timestamp
                elif query_range.type == "after":
                    param_obj["after"] = query_range.timestamp

            params = EndpointsBase.params_for(param_obj)
            return self.get_request(f"me/player/recently-played{params}")

    def get_users_queue(self):
        return self.get_request("me/player/queue")

    def transfer_playback(self, device_ids: list[str], play: Optional[bool] = None):
        if len(device_ids) > 1:
            raise "Although a list is accepted, only a single device_id is currently supported. Supplying more than one will return 400 Bad Request"

        self.put_request("me/player", {
            "device_ids": device_ids,
            "play": play
        })

    def start_resume_playback(self, device_id: str, context_uri: Optional[str] = None, uris: Optional[list[str]] = None, offset: Optional[Any] = None, position_ms: Optional[int] = None):
        params = EndpointsBase.params_for({
            "device_id": device_id
        })
        self.put_request(f"me/player/play{params}", {
            "context_uri": context_uri,
            "uris": uris,
            "offset": offset,
            "position_ms": position_ms
        })

    def pause_playback(self, device_id: str):
        params = EndpointsBase.params_for({
            "device_id": device_id
        })
        self.put_request(f"me/player/pause{params}")

    def skip_to_next(self, device_id: str):
        params = EndpointsBase.params_for({
            "device_id": device_id
        })
        self.post_request(f"me/player/next{params}")

    def skip_to_previous(self, device_id: str):
        params = EndpointsBase.params_for({
            "device_id": device_id
        })
        self.post_request(f"me/player/previous{params}")

    def seek_to_position(self, position_ms: int, device_id: Optional[str] = None):
        params = EndpointsBase.params_for({
            "position_ms": position_ms,
            "device_id": device_id
        })
        self.put_request(f"me/player/seek{params}")

    def set_repeat_mode(self, state: Literal["track", "context", "off"], device_id: Optional[str] = None):
        params = EndpointsBase.params_for({
            "state": state,
            "device_id": device_id
        })
        self.put_request(f"me/player/repeat{params}")

    def set_playback_volume(self, volume_percent: int, device_id: Optional[str] = None):
        params = EndpointsBase.params_for({
            "volume_percent": volume_percent,
            "device_id": device_id
        })
        self.put_request(f"me/player/volume{params}")

    def toggle_playback_shuffle(self, state: bool, device_id: Optional[str] = None):
        params = EndpointsBase.params_for({
            "state": state,
            "device_id": device_id
        })
        self.put_request(f"me/player/shuffle{params}")

    def add_item_to_playback_queue(self, uri: str, device_id: Optional[str] = None):
        params = EndpointsBase.params_for({
            "uri": uri,
            "device_id": device_id
        })
        self.post_request(f"me/player/queue{params}")


