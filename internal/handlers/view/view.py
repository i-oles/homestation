from flask import request


def turn_on():
    if request.is_json:
        req = request.get_json()
        return req
