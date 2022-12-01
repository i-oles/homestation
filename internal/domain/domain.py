from dataclasses import dataclass


@dataclass(frozen=True)
class LightPreset:
    preset: str


@dataclass(frozen=True)
class BulbSettings:
    ip: str
    preset: str
    luminance: int
