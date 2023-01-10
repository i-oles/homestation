import logging

from tinydb import TinyDB

from config.config import DB_PATH
from internal.domain import domain
from internal.repo.repo import RepoInterface, IP, PRESET


class TinyDbRepo(RepoInterface):
    def __init__(self, db: TinyDB):
        self.db = db

    def turn_on(self, params: domain.LightParams) -> domain.RepoResponse:
        settings = []
        to_turn_off = []

        # TODO: should be fatal if some of this errors?
        for bulb in self.db:
            bulb_ip = bulb.get(IP)
            if not bulb_ip:
                logging.error(f"could not find 'ip_address' of bulb: {bulb}")

            presets = bulb.get(PRESET)
            if not presets:
                logging.error(f"could not find 'preset' of bulb: {bulb}")
            else:
                tag = presets.get(params.tag)
                if not tag:
                    to_turn_off.append(domain.BulbIP(ip=bulb_ip))
                    continue

                bulb_type = bulb.get("type")
                if not bulb_type:
                    logging.error(f"could not find 'type' of bulb: {bulb}")

                setting = domain.BulbSettings(
                    ip=bulb_ip,
                    type=bulb_type,
                    luminance=tag,
                )

                settings.append(setting)

        return domain.RepoResponse(
            settings=settings,
            to_turn_off=to_turn_off,
        )


# x = TinyDbRepo(TinyDB(DB_PATH))
# print(x.turn_on(domain.LightParams(tag="cozy")))
