from tinydb import where, TinyDB
from internal.domain import domain
from internal.repo.repo import RepoInterface, PRESET, IP


class TinyDbRepo(RepoInterface):
    def turn_on(self, params: domain.LightParams) -> domain.RepoResponse:
        settings = []
        to_turn_off = []

        # TODO: move to main, change to env var
        db = TinyDB("/Users/ioles/PycharmProjects/homestation/db/db.json")

        for bulb in db:
            presets = bulb.get("preset")
            tag = presets.get(params.tag)
            if tag:
                s = domain.BulbSettings(
                    ip=bulb[IP],
                    type=bulb["type"],
                    luminance=tag,
                )

                settings.append(s)
            else:
                s = domain.BulbIP(
                    ip=bulb[IP]
                )

                to_turn_off.append(s)

        return domain.RepoResponse(
            settings=settings,
            to_turn_off=to_turn_off,
        )


x = TinyDbRepo()
print(x.turn_on(domain.LightParams(tag="cleaning")))
