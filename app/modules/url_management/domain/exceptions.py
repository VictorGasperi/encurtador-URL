class UrlNotFoundException(Exception):
    def __init__(self, code: str):
        self.message = f"URL with code '{code}' not found."
        super().__init__(self.message)

class InvalidUrlException(Exception):
    def __init__(self, url: str):
        self.message = f"The given URL '{url}' is not valid."
        super().__init__(self.message)

class InvalidCodeException(Exception):
    def __init__(self, code: str):
        self.message = f"The given code '{code}' is not valid."
        super().__init__(self.message)