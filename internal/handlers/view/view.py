from flask import request

from internal.domain import domain
from internal.service.light.light import Light


def turn_on():
    if request.is_json:
        req = request.get_json()

        tag = domain.LightParams(tag=req.tag)
        bulb_settings = Light().turn_on(tag)
        pass






