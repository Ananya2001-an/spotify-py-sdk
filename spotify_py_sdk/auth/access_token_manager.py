import json
import base64
import requests
from datetime import datetime, timedelta


class AccessTokenManager:
    """Manage access token generated by authenticating user using Client Credentials Flow.

    :param client_id: Client_ID for your app
    :type client_id: str
    :param client_secret: Client_Secret for your app
    :type client_secret: str
    """
    def __init__(self, client_id: str, client_secret: str):
        """Constructor method
        """
        self.client_id = client_id
        self.client_secret = client_secret
        self.token_file = "access_token.json"
        self.access_token = None

    def get_access_token(self):
        """Retrieve the access token
        """
        if self.access_token:
            return self.access_token

        saved_token = self._load_saved_token()

        if saved_token and datetime.strptime(json.loads(saved_token.get("expires_in")), "%Y-%m-%d %H:%M:%S.%f") > datetime.now():
            # old token is still valid
            self.access_token = saved_token.get("access_token")
        else:
            self.access_token = self._generate_new_token()

        return self.access_token

    def _load_saved_token(self):
        """Load access token from JSON file
        """
        try:
            with open(self.token_file, "r") as file:
                data = json.load(file)
                return data
        except (FileNotFoundError, json.JSONDecodeError):
            return None

    def _save_token_info(self, access_token: str, expires_in: int):
        """Save access token info inside a JSON file
        """
        data = {"access_token": access_token, "expires_in": json.dumps(datetime.now() + timedelta(seconds=expires_in), default=str)}
        with open(self.token_file, "w") as file:
            json.dump(data, file)

    def _generate_new_token(self):
        """Create new access token using client creds
        """
        url = "https://accounts.spotify.com/api/token"
        headers = {
            "Authorization": "Basic " + base64.b64encode(
                (self.client_id + ":" + self.client_secret).encode()).decode(),
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {"grant_type": "client_credentials"}
        response = requests.post(url, headers=headers, data=data)
        response.raise_for_status()
        response = response.json()
        new_token = response["access_token"]
        self._save_token_info(new_token, response["expires_in"])
        return new_token
