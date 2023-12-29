from typing import Union

from .endpoints_base import EndpointsBase
from src.types import *


class RecommendationsRequestRequiredArguments:
    def __init__(self, seed_artists: Optional[str] = None, seed_genres: Optional[str] = None, seed_tracks: Optional[str] = None):
        self.seed_artists = seed_artists
        self.seed_genres = seed_genres
        self.seed_tracks = seed_tracks


class RecommendationsRequest(RecommendationsRequestRequiredArguments):
    def __init__(self):
        # TODO
        super().__init__()
        pass
    
    
class RecommendationSeed:
    def __init__(self, id: str, href: str, type: str, initial_pool_size: int, after_filtering_size: int, after_relinking_size: int):
        self.id = id
        self.href = href
        self.type = type
        self.initial_pool_size = initial_pool_size
        self.after_filtering_size = after_filtering_size
        self.after_relinking_size = after_relinking_size


class RecommendationsResponse:
    def __init__(self, seeds: list[RecommendationSeed], tracks: list[Track]):
        self.seeds = seeds
        self.tracks = tracks


class Recommendations(EndpointsBase):
    def __init__(self, api):
        super().__init__(api)

    def get(self, request: Union[RecommendationsRequestRequiredArguments, RecommendationsRequest]):
        param_obj = {}
        for prop, value in request.__dict__.items():
            param_obj[prop] = value
        params = EndpointsBase.params_for(param_obj)
        return self.get_request(f"recommendations{params}")

    def genre_seeds(self):
        return self.get_request("recommendations/available-genre-seeds")

