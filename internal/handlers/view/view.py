from flask import request
from internal.domain import model


def turn_on():
    if request.is_json:
        req = request.get_json()

        params = model.LightParams(tag=req.tag)

