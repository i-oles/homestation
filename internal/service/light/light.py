from tinydb import TinyDB
from yeelight import Bulb

from config.config import DB_PATH
from internal.domain import domain
from internal.repo.repo import RepoInterface
from internal.repo.tiny_db.tiny_db import TinyDbRepo
from internal.service.service import ServiceInterface


class Light(ServiceInterface):
    def __init__(self, repo: RepoInterface):
        self.repo = repo

    def turn_on(self, params: domain.LightParams) -> list[domain.BulbSettings]:
        repo_response = self.repo.turn_on(params)
        # FIXME: check empty repo response

        # FIXME: code breaks when bulb is switched off
        [Bulb(bulb).turn_off() for bulb in repo_response.to_turn_off]

        bulb_settings = repo_response.settings

        # TODO: add slow turning on the light
        # TODO: check how bulbs works when type RGB
        for setting in bulb_settings:
            bulb = Bulb(setting.ip, effect="smooth")
            bulb.set_brightness(setting.luminance)
            bulb.turn_on()

        return bulb_settings


# db = TinyDB(DB_PATH)
# x = Light(TinyDbRepo(db))
# print(x.turn_on(domain.LightParams(tag="cozy")))
