from dataclasses import dataclass

IP = "ip"


@dataclass
class LightParams:
    tag: str


@dataclass
class BulbSettings:
    ip: str
    luminance: int
