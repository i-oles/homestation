from dataclasses import dataclass


@dataclass
class ToggleSingleParams:
    ip: str
    is_on: bool


@dataclass
class BulbSettings:
    ip: str
    is_active: bool


@dataclass
class BulbModel:
    id: str
    ip: str
    type: str
    active: bool
    luminance: int
    preset: dict[str, int]


@dataclass
class BulbState:
    ip: str
    is_on: bool
    is_online: bool
