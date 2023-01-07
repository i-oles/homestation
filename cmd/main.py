from flask import Flask
from tinydb import TinyDB

from internal.handlers.view.view import View
from config import config
from internal.repo.tiny_db.tiny_db import TinyDbRepo
from internal.service.light.light import Light

# TODO: make tests to all layers
# TODO: add handling errors in all layers
app = Flask(__name__)

db = TinyDB(config.DB_PATH)

repo = TinyDbRepo(db)
service = Light(repo)
view = View(service)

app.add_url_rule("/turn_on", "turn_on", view.turn_on, methods=["POST"])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8123, debug=True)
