from typing import Optional, Any
from urllib.parse import urlencode


class EndpointsBase:
    """Base class for all endpoint classes
    """
    def __init__(self, api):
        """Constructor method

        :param api: :class:`SpotifyApi` instance
        """
        self.api = api

    @classmethod
    def params_for(cls, args: dict) -> str:
        """Converts params from the given dictionary object to url format

        :param args: key value pairs indicating query params for request
        :return: url encoded string
        """
        for key, value in args.copy().items():
            if value is None:
                del args[key]
            elif type(value) is list:
                args[key] = ",".join(value)
            elif type(value) is bool:
                args[key] = "false" if value is False else "true"
        return f"?{urlencode(args)}" if args != {} else ""

    def get_request(self, url: str):
        """Make a GET request to the endpoint
        """
        return self.api.make_request("GET", url)

    def post_request(self, url: str, body: Optional[Any] = None, content_type: Optional[str] = None):
        """Make a POST request to the endpoint
        """
        return self.api.make_request("POST", url, body, content_type)

    def put_request(self, url: str, body: Optional[Any] = None, content_type: Optional[str] = None):
        """Make a PUT request to the endpoint
        """
        return self.api.make_request("PUT", url, body, content_type)

    def delete_request(self, url: str, body: Optional[Any] = None):
        """Make a DELETE request to the endpoint
        """
        return self.api.make_request("DELETE", url, body)


