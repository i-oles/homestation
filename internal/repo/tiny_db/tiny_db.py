import logging

from tinydb import TinyDB

from config.config import DB_PATH
from internal.domain import domain
from internal.repo.repo import RepoInterface, IP, PRESET, TYPE


class TinyDbRepo(RepoInterface):
    def __init__(self, db: TinyDB):
        self.db = db

    def turn_on(self, params: domain.LightParams) -> domain.RepoResponse:
        settings = []
        ips_to_turn_off = []

        for bulb in self.db:
            bulb_type = bulb.get(TYPE, "white")

            try:
                bulb_ip = bulb[IP]
            except KeyError:
                logging.error(f"could not find 'ip_address' of bulb: {bulb}")
            else:
                try:
                    presets = bulb[PRESET]
                except KeyError:
                    logging.error(f"could not find 'preset' of bulb: {bulb}")
                else:
                    tag = presets.get(params.tag)
                    if not tag:
                        ips_to_turn_off.append(bulb_ip)
                        continue
                    else:
                        setting = domain.BulbSettings(
                            ip=bulb_ip,
                            type=bulb_type,
                            luminance=tag,
                        )

                    settings.append(setting)

        return domain.RepoResponse(
            settings=settings,
            to_turn_off=ips_to_turn_off,
        )

# x = TinyDbRepo(TinyDB(DB_PATH))
# print(x.turn_on(domain.LightParams(tag="cozy")))
