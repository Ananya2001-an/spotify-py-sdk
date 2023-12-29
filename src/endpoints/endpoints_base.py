from typing import Optional, Any
from urllib.parse import urlencode


class EndpointsBase:

    def __init__(self, api):
        self.api = api

    @classmethod
    def params_for(cls, args: dict) -> str:
        for key, value in args.copy().items():
            if value is None:
                del args[key]
        return f"?{urlencode(args)}" if args != {} else ""

    def get_request(self, url: str):
        return self.api.make_request("GET", url)

    def post_request(self, url: str, body: Optional[Any] = None, content_type: Optional[str] = None):
        return self.api.make_request("POST", url, body, content_type)

    def put_request(self, url: str, body: Optional[Any] = None, content_type: Optional[str] = None):
        return self.api.make_request("PUT", url, body, content_type)

    def delete_request(self, url: str, body: Optional[Any] = None):
        return self.api.make_request("DELETE", url, body)


