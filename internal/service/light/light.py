import time

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

    def turn_on(self, params: domain.TurnOnParams) -> list[domain.BulbSettings]:
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

    def turn_off(self, params: domain.TurnOffParams) -> list:
        ips_to_turn_off = self.repo.turn_off(params)

        [Bulb(bulb).turn_off() for bulb in ips_to_turn_off]

        return ips_to_turn_off

db = TinyDB(DB_PATH)
x = Light(TinyDbRepo(db))

# print(x.turn_on(domain.TurnOnParams(tag="cleaning")))
print(x.turn_off(domain.TurnOffParams(ids=["table_lamp", "sofa_lamp", "salon_main_lamp"])))
