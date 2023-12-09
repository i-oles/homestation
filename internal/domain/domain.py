from dataclasses import dataclass
from typing import List


@dataclass
class TurnOnParams:
    # TODO: here will be another field for bulb color settings
    tag: str


@dataclass
class ToggleSingleParams:
    ip: str
    is_active: bool
    luminance: int


@dataclass
class TurnOffParams:
    ids: List[str]


@dataclass
class BulbSettings:
    ip: str
    is_active: bool
    luminance: int


@dataclass
class RepoResponse:
    settings: List[BulbSettings]
    to_turn_off: List[str]


@dataclass
class BulbModel:
    id: str
    ip: str
    type: str
    active: bool
    luminance: int
    preset: dict[str, int]
