from tinydb import where, TinyDB
from dataclasses import dataclass


@dataclass(frozen=True)
class LightTag:
    name: str


@dataclass(frozen=True)
class BulbSettings:
    ip: str
    luminance: int


def turn_on(tag: LightTag) -> list[BulbSettings]:

    settings = []

    db = TinyDB("/Users/ioles/PycharmProjects/homestation/db/db.json")

    bulbs = db.search(where('preset').any(where(tag.name) > 1))

    for bulb in bulbs:
        for i in bulb["preset"]:
            try:
                bulb_settings = BulbSettings(
                    ip=bulb["ip"],
                    luminance=i[tag.name]
                )

                settings.append(bulb_settings)
            finally:
                continue

    return settings


x = turn_on(LightTag(name="cinema"))
print(x)

