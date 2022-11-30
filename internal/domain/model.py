from dataclasses import dataclass


@dataclass(frozen=True)
class LightParams:
    tag: str
    bulb: dict

