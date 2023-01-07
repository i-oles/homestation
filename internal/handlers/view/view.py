from flask import request

from internal.domain import domain
from internal.service.service import ServiceInterface


class View:
    def __init__(self, service: ServiceInterface):
        self.service = service

    def turn_on(self):
        if request.is_json:
            req = request.get_json()

            tag = domain.LightParams(tag=req.tag)
            bulb_settings = self.service.turn_on(tag)
            print(bulb_settings)
            pass
