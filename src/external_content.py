from dataclasses import dataclass
from typing import Optional

import requests


@dataclass
class Content:
    content: Optional[str]


class ContentService:
    _session: requests.Session

    def __init__(self):
        self._session = requests.Session()
        self._session.verify = False

    def get_content(self, url: str) -> Content:
        try:
            response = self._session.get(url)
        except requests.exceptions.ConnectionError:
            c = Content(None)
            return c

        if response.status_code != 200:
            c = Content(None)
            return c

        c = Content(response.text)
        return c
