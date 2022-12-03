from internal.domain import domain
from yeelight import Bulb, discover_bulbs

from internal.repository.tiny_db import tiny_db
from internal.repository.tiny_db.tiny_db import LightTag, BulbSettings


def turn_on(tag: LightTag) -> list[BulbSettings]:
    bulb_settings = tiny_db.turn_on(tag)

    active_bulb_ips = [bulb['ip'] for bulb in discover_bulbs()]

    for setting in bulb_settings:
        if setting.ip in active_bulb_ips:
            active_bulb_ips.remove(setting.ip)

        bulb = Bulb(setting.ip)
        bulb.set_brightness(setting.luminance)
        bulb.set_default()
        bulb.turn_on()

    # turning off bulbs which are still working.
    # TODO: check if there is no working bulb if the code breaks
    for bulb_ip in active_bulb_ips:
        Bulb(bulb_ip).turn_off()

    return bulb_settings
