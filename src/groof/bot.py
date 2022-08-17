from dataclasses import dataclass

import requests

from . import types


@dataclass
class DefaultRequestParams:
    parse_mode: types.ParseMode = None
    disable_web_page_preview: bool = False


class BaseBot:

    def __init__(self, api_token: str, default_request_params: DefaultRequestParams = None):
        self._api_token = api_token
        self._validate_token()
        self._default_request_params = default_request_params or DefaultRequestParams()
        self.session = requests.Session()

    def _validate_token(self):
        if not isinstance(self._api_token, str):
            raise ValueError('Invalid token')

        parts = self._api_token.split(':')

        if len(parts) != 2:
            raise ValueError('Invalid token')

    def set_default_request_params(
            self,
            parse_mode: types.ParseMode = None,
            disable_web_page_preview: bool = False,
    ):
        self._default_request_params = DefaultRequestParams(parse_mode, disable_web_page_preview)


class Bot(BaseBot):

    def get_updates(
            self,
            offset: int = None,
            limit: int = None,
            timeout: int = None,
            allowed_updates: list[types.UpdateType] = None,
    ) -> list[types.Update]:  # TODO
        host = 'https://api.telegram.org'
        base_url = host + f'/bot{self._api_token}'
        endpoint = base_url + '/getUpdates'
        resp = self.session.post(endpoint, json={'offset': offset})
        result = resp.json()['result']
        return [types.Update(u['update_id']) for u in result]
