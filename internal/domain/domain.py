from dataclasses import dataclass
from typing import List


@dataclass
class TurnOnParams:
    # TODO: here will be another field for bulb color settings
    tag: str


@dataclass
class TurnOffParams:
    ids: List[str]


@dataclass
class BulbSettings:
    ip: str
    luminance: int
    type: str


@dataclass
class RepoResponse:
    settings: List[BulbSettings]
    to_turn_off: List[str]
