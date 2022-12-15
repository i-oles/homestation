from yeelight import Bulb, discover_bulbs
from internal.domain import domain
from internal.domain.domain import IP
from internal.repo.tiny_db.tiny_db import TinyDbRepo
from internal.service.service import ServiceInterface


class Light(ServiceInterface):
    def turn_on(self, params: domain.LightParams) -> list[domain.BulbSettings]:
        repo_response = TinyDbRepo().turn_on(params)

        # TODO: check if when is no working bulb if the code breaks
        [Bulb(bulb.ip).turn_off() for bulb in repo_response.to_turn_off]

        bulb_settings = repo_response.settings

        # TODO: add slow turning on the light
        # TODO: check how bulbs works when type RGB
        for setting in bulb_settings:
            bulb = Bulb(setting.ip)
            bulb.set_brightness(setting.luminance)
            bulb.turn_on()

        return bulb_settings

#
# x = Light()
# print(x.turn_on(domain.LightParams(tag="cozy")))
