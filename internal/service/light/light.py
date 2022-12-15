from yeelight import Bulb, discover_bulbs
from internal.domain import domain
from internal.domain.domain import IP
from internal.repo.tiny_db.tiny_db import TinyDbRepo
from internal.service.service import ServiceInterface


class Light(ServiceInterface):
    def turn_on(self, params: domain.LightParams) -> list[domain.BulbSettings]:
        bulb_settings = TinyDbRepo().turn_on(params)

        # FIXME
        # you can not choose from discover_bulbs because
        # it will not show you the bulbs which are working now
        # consider isActive param in db
        active_bulb_ips = [bulb[IP] for bulb in discover_bulbs()]

        for setting in bulb_settings:
            if setting.ip in active_bulb_ips:
                active_bulb_ips.remove(setting.ip)

            bulb = Bulb(setting.ip)
            bulb.set_brightness(setting.luminance)
            bulb.turn_on()

        # turning off bulbs which are still working.
        # TODO: check if when is no working bulb if the code breaks
        for bulb_ip in active_bulb_ips:
            try:
                Bulb(bulb_ip).turn_off()
            finally:
                print("error tutaj")

        return bulb_settings

#
# x = Light()
# print(x.turn_on(domain.LightParams(tag="cinema")))
