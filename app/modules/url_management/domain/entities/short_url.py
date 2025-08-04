from abc import ABC


class ShortUrl(ABC):
    code: str
    original_url: str

    def __init__(self, code: str, original_url: str):
        self.code = code
        self.original_url = original_url

    def to_dict(self):
        return {
            "code": self.code,
            "original_url": self.original_url
        }
    
    def __eq__(self, value):
        if not isinstance(value, ShortUrl):
            return False
        return self.__dict__ == value.__dict__