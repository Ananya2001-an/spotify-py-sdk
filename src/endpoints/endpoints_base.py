from typing import Optional


class EndpointsBase:

    def __init__(self, api):
        self.api = api

    def get_request(self, url: str):
        return self.api.make_request("GET", url)

