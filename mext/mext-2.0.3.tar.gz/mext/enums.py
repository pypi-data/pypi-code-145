from enum import Enum
from typing import List, Dict


class BaseEnum(Enum):

    @classmethod
    def __contains__(cls, name) -> bool:
        return name in [c.name for c in cls]

    @classmethod
    def list(cls) -> List:
        return [c.value for c in cls]

    @classmethod
    def keys(cls) -> List:
        return [c.name for c in cls]

    @classmethod
    def dict(cls) -> Dict:
        return {c.name: c.value for c in cls}

    @classmethod
    def reverse_dict(cls) -> Dict:
        return {c.value: c.name for c in cls}


class AttributeEnum(str, BaseEnum):
    pass


class StatusTypes(AttributeEnum):
    Ongoing = 'Ongoing'
    Completed = 'Completed'
    Haitus = 'Haitus'
    Dropped = 'Dropped'
    ComingSoon = 'Comic Soon'


class ComicTypesLanguage(AttributeEnum):
    manga = 'ja'
    manhua = 'zh'
    manhwa = 'ko'
    webtoon = 'en'