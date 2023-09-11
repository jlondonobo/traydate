from datetime import datetime
from typing import Any

import requests


class Pydel:
    def __init__(
        self,
        headers: dict[str, str] | None = None
    ):
        self.prefix =  "https://www.easycancha.com/api/sports/7"
        if headers is not None:
            self._build_session(headers)
        else:
            self._session = requests.Session()
    
    def _build_session(self, headers: dict[str, str]):
        self._session = requests.Session()
        self._session.headers.update(headers)
    
    def _get(self, url: str, params: dict[str, Any]| None = None):
        url = self.prefix + url
        return self._session.get(url, params=params).json()
    
    def timeslots(self, slot: datetime):
        date = slot.date().strftime("%Y-%m-%d")
        time = slot.time().strftime("%H:%M:%S")
        params = {"date": date, "time": time}
        return self._get("/timeslots", params)


    