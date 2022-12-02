from flask import request
from internal.domain import domain

def turn_on():
    if request.is_json:
        req = request.get_json()

        #preset = LightTag(req.preset)
        pass



