from tinydb import where, TinyDB
from internal.domain import domain
from internal.repository.repository import RepositoryInterface, PRESET, IP


class TinyDbRepo(RepositoryInterface):
    def turn_on(self, params: domain.LightParams) -> list[domain.BulbSettings]:
        settings = []

        db = TinyDB("/Users/ioles/PycharmProjects/homestation/db/db.json")

        bulbs = db.search(where(PRESET).any(where(params.tag) > 1))

        for bulb in bulbs:
            for preset in bulb[PRESET]:
                try:
                    bulb_settings = domain.BulbSettings(
                        ip=bulb[IP],
                        luminance=preset[params.tag]
                    )

                    settings.append(bulb_settings)
                finally:
                    continue

        return settings


x = TinyDbRepo()
print(x.turn_on(domain.LightParams(tag="cinema")))
