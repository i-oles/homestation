from tinydb import TinyDB

from config.config import DB_PATH
from internal.domain import domain
from internal.repo.repo import RepoInterface, IP


class TinyDbRepo(RepoInterface):
    def __init__(self, db: TinyDB):
        self.db = db

    def turn_on(self, params: domain.LightParams) -> domain.RepoResponse:
        settings = []
        to_turn_off = []

        for bulb in self.db:
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
                s = domain.BulbIP(ip=bulb[IP])

                to_turn_off.append(s)

        return domain.RepoResponse(
            settings=settings,
            to_turn_off=to_turn_off,
        )


x = TinyDbRepo(TinyDB(DB_PATH))
print(x.turn_on(domain.LightParams(tag="cozy")))
