from flask import request

from internal.domain import domain
from internal.service.service import ServiceInterface


class View:
    def __init__(self, service: ServiceInterface):
        self.service = service

    def turn_on(self):
        if request.is_json:
            req = request.get_json()

            tag = domain.TurnOnParams(tag=req.tag)
            bulb_settings = self.service.turn_on(tag)
            print(bulb_settings)

    def turn_off(self):
        if request.is_json:
            req = request.get_json()

            ids = domain.TurnOffParams(ids=req.ids)
            ids_to_turn_off = self.service.turn_off(ids)
            print(ids_to_turn_off)
