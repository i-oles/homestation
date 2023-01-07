from dataclasses import dataclass

IP = "ip"


@dataclass
class LightParams:
    # TODO: here will be another field for bulb color settings
    tag: str


@dataclass
class BulbSettings:
    ip: str
    luminance: int
    type: str


@dataclass
class BulbIP:
    ip: str


@dataclass
class RepoResponse:
    settings: list[BulbSettings]
    to_turn_off: list[BulbIP]
