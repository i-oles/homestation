from flask import Flask
from tinydb import TinyDB

from internal.handlers.view.view import View
from config import config
from internal.repo.tiny_db.tiny_db import TinyDbRepo
from internal.service.light.light import Light

# TODO: make tests to all layers
# TODO: add handling errors in all layers
homestation_app = Flask(__name__)


@homestation_app.route("/")
def home():
    return "<html><body><h1 style='color:blue'>I am hosted on Raspberry Pi !!!</h1></body></html>"


db = TinyDB(config.DB_PATH)

repo = TinyDbRepo(db)
service = Light(repo)
view = View(service)

homestation_app.add_url_rule(
    "/turn_on", "turn_on", view.turn_on, methods=["POST"]
)
homestation_app.add_url_rule(
    "/turn_off", "turn_off", view.turn_off, methods=["POST"]
)

if __name__ == "__main__":
    homestation_app.run(host="0.0.0.0", debug=True)
