from .endpoints_base import EndpointsBase
from src.types import *


class CurrentUser(EndpointsBase):
    """Get current user info. Make calls to me api endpoint.
    """
    def __init__(self, api):
        """Constructor method
        """
        super().__init__(api)
        self.albums = CurrentUserAlbums(api)
        self.audiobooks = CurrentUserAudiobooks(api)
        self.episodes = CurrentUserEpisodes(api)
        self.playlists = CurrentUserPlaylists(api)
        self.shows = CurrentUserShows(api)
        self.tracks = CurrentUserTracks(api)

    def profile(self):
        """Get profile of the current user
        """
        return self.get_request("me")

    def top_items(self, type: Literal["artists", "tracks"], time_range: Optional[Literal["short_term", "medium_term", "long_term"]] = None, limit: Optional[int] = None, offset: Optional[int] = None):
        """Get top items of the current user

        :param type: pass a type from ["artists", "tracks"]
        """
        params = EndpointsBase.params_for({"time_range": time_range, "limit": limit, "offset": offset})
        return self.get_request(f"me/top/{type}{params}")

    def followed_artists(self, after: Optional[str] = None, limit: Optional[int] = None):
        """Get artists followed by the current user
        """
        params = EndpointsBase.params_for({"type": "artist", "after": after, "limit": limit})
        return self.get_request(f"me/following{params}")

    def follow_artists_or_users(self, ids: list[str], type: Literal["artist", "user"]):
        """Follow a new artist or user

        :param ids: pass list of ids
        :param type: pass a type from ["artist", "user"]
        """
        params = EndpointsBase.params_for({"type": type})
        self.put_request(f"me/following{params}", {"ids": ids})

    def unfollow_artists_or_users(self, ids: list[str], type: Literal["artist", "user"]):
        """Unfollow artist or user

        :param ids: pass list of ids
        :param type: pass a type from ["artist", "user"]
        """
        params = EndpointsBase.params_for({"type": type})
        self.delete_request(f"me/following{params}", {"ids": ids})

    def follows_artists_or_users(self, ids: list[str], type: Literal["artist", "user"]):
        """Get followings of the current user

        :param ids: pass list of ids
        :param type: pass a type from ["artist", "user"]
        """
        params = EndpointsBase.params_for({"ids": ids, "type": type})
        return self.get_request(f"me/following/contains{params}")


class CurrentUserAlbums(EndpointsBase):
    """Has methods for albums of the current user
    """
    def saved_albums(self, limit: Optional[int] = None, offset: Optional[int] = None, market: Optional[MARKET] = None):
        """Get all saved albums of the current user
        """
        params = EndpointsBase.params_for({"limit": limit, "offset": offset, "market": market})
        return self.get_request(f"me/albums{params}")

    def save_albums(self, ids: list[str]):
        """Save new albums

        :param ids: pass list of ids
        """
        self.put_request("me/albums", ids)

    def remove_saved_albums(self, ids: list[str]):
        """Remove saved albums

        :param ids: pass list of ids
        """
        self.delete_request("me/albums", ids)

    def has_saved_albums(self, ids: list[str]):
        """Check if current user has these saved albums or not

        :param ids: pass list of ids
        """
        params = EndpointsBase.params_for({"ids": ids})
        return self.get_request(f"me/albums/contains{params}")


class CurrentUserAudiobooks(EndpointsBase):
    """Has methods for audiobooks of the current user
    """
    def saved_audiobooks(self, limit: Optional[int] = None, offset: Optional[int] = None):
        """Get all saved audiobooks of the current user
        """
        params = EndpointsBase.params_for({"limit": limit, "offset": offset})
        return self.get_request(f"me/audiobooks{params}")

    def save_audiobooks(self, ids: list[str]):
        """Save new audiobooks

        :param ids: pass list of ids
        """
        self.put_request("me/audiobooks", ids)

    def remove_saved_audiobooks(self, ids: list[str]):
        """Remove saved audiobooks

        :param ids: pass list of ids
        """
        self.delete_request("me/audiobooks", ids)

    def has_saved_audiobooks(self, ids: list[str]):
        """Check if current user has these saved audiobooks or not

        :param ids: pass list of ids
        """
        params = EndpointsBase.params_for({"ids": ids})
        return self.get_request(f"me/audiobooks/contains{params}")


class CurrentUserEpisodes(EndpointsBase):
    """Has methods for episodes of the current user
    """
    def saved_episodes(self, market: Optional[MARKET] = None, limit: Optional[int] = None, offset: Optional[int] = None):
        """Get all saved episodes of the current user
        """
        params = EndpointsBase.params_for({"market": market, "limit": limit, "offset": offset})
        return self.get_request(f"me/episodes{params}")

    def save_episodes(self, ids: list[str]):
        """Save new episodes

        :param ids: pass list of ids
        """
        self.put_request("me/episodes", ids)

    def remove_saved_episodes(self, ids: list[str]):
        """Remove saved episodes

        :param ids: pass list of ids
        """
        self.delete_request("me/episodes", ids)

    def has_saved_episodes(self, ids: list[str]):
        """Check if current user has these saved episodes or not

        :param ids: pass list of ids
        """
        params = EndpointsBase.params_for({"ids": ids})
        return self.get_request(f"me/episodes/contains{params}")


class CurrentUserPlaylists(EndpointsBase):
    """Has methods for playlists of the current user
    """
    def playlists(self, limit: Optional[int] = None, offset: Optional[int] = None):
        """Get playlists of the current user
        """
        params = EndpointsBase.params_for({"limit": limit, "offset": offset})
        return self.get_request(f"me/playlists{params}")

    def follow(self, playlist_id: str):
        """Follow a new playlist

        :param playlist_id: pass playlist id
        """
        self.put_request(f"playlists/{playlist_id}/followers")

    def unfollow(self, playlist_id: str):
        """Unfollow a playlist

        :param playlist_id: pass playlist id
        """
        self.delete_request(f"playlists/{playlist_id}/followers")

    def is_following(self, playlist_id: str, ids: list[str]):
        """Check if current user is following the given playlist

        :param playlist_id: pass playlist id
        :param ids: pass user ids as list
        :return:
        """
        params = EndpointsBase.params_for({"ids": ids})
        return self.get_request(f"playlists/{playlist_id}/followers/contains{params}")


class CurrentUserShows(EndpointsBase):
    """Has methods for shows of the current user
    """
    def saved_shows(self, limit: Optional[int] = None, offset: Optional[int] = None):
        """Get all saved shows of the current user
        """
        params = EndpointsBase.params_for({ "limit": limit, "offset": offset })
        return self.get_request(f"me/shows{params}")

    def save_shows(self, ids: list[str]):
        """Save new shows

        :param ids: pass list of ids
        """
        params = EndpointsBase.params_for({"ids": ids})
        return self.put_request(f"me/shows{params}")

    def remove_saved_shows(self, ids: list[str], market: Optional[MARKET] = None):
        """Remove saved shows

        :param ids: pass list of ids
        """
        params = EndpointsBase.params_for({"ids": ids, "market": market})
        return self.delete_request(f"me/shows{params}")

    def has_saved_show(self, ids: list[str]):
        """Check if current user has these saved shows or not

        :param ids: pass list of ids
        """
        params = EndpointsBase.params_for({"ids": ids})
        return self.get_request(f"me/shows/contains{params}")


class CurrentUserTracks(EndpointsBase):
    """Has methods for tracks of the current user
    """
    def saved_tracks(self, limit: Optional[int] = None, offset: Optional[int] = None, market: Optional[MARKET] = None):
        """Get all saved tracks of the current user
        """
        params = EndpointsBase.params_for({"limit": limit, "offset": offset, "market": market })
        return self.get_request(f"me/tracks{params}")

    def save_tracks(self, ids: list[str]):
        """Save new tracks

        :param ids: pass list of ids
        """
        self.put_request("me/tracks", ids)

    def remove_saved_tracks(self, ids: list[str]):
        """Remove saved tracks

        :param ids: pass list of ids
        """
        self.delete_request("me/tracks", ids)

    def has_saved_tracks(self, ids: list[str]):
        """Check if current user has these saved tracks or not

        :param ids: pass list of ids
        """
        params = EndpointsBase.params_for({"ids": ids})
        return self.get_request(f"me/tracks/contains{params}")
