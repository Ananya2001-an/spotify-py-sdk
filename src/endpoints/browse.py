from .endpoints_base import EndpointsBase
from src.types import *


class Browse(EndpointsBase):

    def __init__(self, api):
        super().__init__(api)

    def get_categories(self, country: Optional[COUNTRY_CODE_A2] = None, locale: Optional[str] = None, limit: Optional[int] = None, offset: Optional[int] = None):
        params = EndpointsBase.params_for({"country": country, "locale": locale, "limit": limit, "offset": offset})
        return self.get_request(f"browse/categories{params}")

    def get_category(self, id: str, country: Optional[COUNTRY_CODE_A2] = None, locale: Optional[str] = None):
        params = EndpointsBase.params_for({"country": country, "locale": locale})
        return self.get_request(f"browse/categories/{id}{params}")

    def get_new_releases(self, country: Optional[COUNTRY_CODE_A2] = None, limit: Optional[int] = None, offset: Optional[int] = None):
        params = EndpointsBase.params_for({"country": country, "limit": limit, "offset": offset})
        return self.get_request(f"browse/new-releases{params}")

    def get_featured_playlists(self, country: Optional[COUNTRY_CODE_A2] = None, locale: Optional[str] = None, timestamp: Optional[str] = None, limit: Optional[int] = None, offset: Optional[int] = None):
        params = EndpointsBase.params_for({"country": country, "locale": locale, "timestamp": timestamp, "limit": limit, "offset": offset})
        return self.get_request(f"browse/featured-playlists{params}")

    def get_playlists_for_category(self, id: str, country: Optional[COUNTRY_CODE_A2] = None, limit: Optional[int] = None, offset: Optional[int] = None):
        params = EndpointsBase.params_for({"country": country, "limit": limit, "offset": offset})
        return self.get_request(f"browse/categories/{id}/playlists{params}")
