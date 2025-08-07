from abc import ABC
from datetime import datetime, timedelta, timezone
import time
from typing import Optional


class ShortUrl(ABC):
    code: str
    original_url: str
    created_at: Optional[datetime]
    ttl: Optional[int] = None

    def __init__(self, code: str, original_url: str, created_at: Optional[datetime] = None, ttl: Optional[int] = None):
        self.code = code
        self.original_url = original_url
        self.created_at = datetime.now(timezone(timedelta(hours=-3)))
        self.ttl = (int(time.time()) + ttl) if ttl is not None else None

    def to_dict(self):
        item = {
            "code": self.code,
            "original_url": self.original_url,
            "created_at": self.created_at,
        }
        
        if self.ttl is not None:
            item["ttl"] = self.ttl
        return item
    
    def __eq__(self, value):
        if not isinstance(value, ShortUrl):
            return False
        return self.__dict__ == value.__dict__