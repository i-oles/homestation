from flask import Flask, request, json, Response
from tinydb import TinyDB

from internal.domain import domain
from config import config
from internal.repo.tiny_db.tiny_db import TinyDbRepo
from internal.service.light.light import Light
import os

# TODO: make tests to all layers
# TODO: add handling errors in all layers
homestation_app = Flask(__name__)

absolute_path = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(absolute_path, config.DB_FILE_NAME)
db = TinyDB(db_path)

repo = TinyDbRepo(db)
service = Light(repo)


@homestation_app.route("/")
def home():
    return "<h1 style='color:blue'>I am hosted on Raspberry Pi !!!</h1>"


@homestation_app.route("/turn_on", methods=["POST"])
def turn_on():
    if request.is_json:
        req = request.get_json()
        tag = domain.TurnOnParams(
            tag=req['tag']
        )
        bulb_settings = service.turn_on(tag)

        return Response(
            response=json.dumps(bulb_settings),
            status=200,
            mimetype="text/plain"
        )


@homestation_app.route("/turn_off", methods=["POST"])
def turn_off():
    if request.is_json:
        req = request.get_json()
        tag = domain.TurnOffParams(ids=req['ids'])
        ips_to_turn_off = service.turn_off(tag)

        return Response(
            response=json.dumps(ips_to_turn_off),
            status=200,
            mimetype="text/plain"
        )


if __name__ == "__main__":
    homestation_app.run(debug=True)
