from flask import request
from internal.domain import domain

from internal.repository.tiny_db.tiny_db import LightTag
from internal.service.light import light


def turn_on() -> :
    if request.is_json:
        req = request.get_json()

        preset = LightTag(req.preset)
        bulb_settings = light.turn_on(preset)






