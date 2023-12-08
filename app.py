from flask import Flask, request, json, Response, render_template
from tinydb import TinyDB
from yeelight import discover_bulbs

from internal.domain import domain
from config import config
from internal.light.repo.tiny_db.tiny_db import TinyDbRepo
from internal.light.service.light.light import Light
import os

from internal.repository.tinydb.repository import TinyDBRepository

# TODO: make tests to all layers
# TODO: add handling errors in all layers
homestation_app = Flask(__name__)

absolute_path = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(absolute_path, config.DB_FILE_NAME)
db = TinyDB(db_path)

# todo: here should be only one repo
repo = TinyDbRepo(db)
light_repo = TinyDBRepository(db)
service = Light(repo)


@homestation_app.route("/")
def home():
    possible_tags = set()

    all_tags_from_db = light_repo.get_all_tags()
    all_active_tags = list()

    active_bulbs = discover_bulbs()
    for bulb in active_bulbs:
        tags = light_repo.get_all_tags_by_ip(bulb.get("ip"))
        [all_active_tags.append(tag) for tag in tags]

    db_tag_count = make_dict_with_counts(all_tags_from_db)
    active_tag_count = make_dict_with_counts(all_active_tags)

    for tag, value in active_tag_count.items():
        if value == db_tag_count.get(tag):
            possible_tags.add(tag)

    return render_template("index.html", possible_tags=possible_tags)

#TODO: turn on, szuould be toggle, and should be able to turn on and off
#TODO: you should also check state of active bulbs.
@homestation_app.route("/turn_on", methods=["POST"])
def turn_on():
    if request.is_json:
        req = request.get_json()
        tag = domain.TurnOnParams(tag=req["tag"])
        bulb_settings = service.turn_on(tag)

        return Response(
            response=json.dumps(bulb_settings), status=200, mimetype="text/plain"
        )


@homestation_app.route("/turn_off", methods=["POST"])
def turn_off():
    if request.is_json:
        req = request.get_json()
        tag = domain.TurnOffParams(ids=req["ids"])
        ips_to_turn_off = service.turn_off(tag)

        return Response(
            response=json.dumps(ips_to_turn_off), status=200, mimetype="text/plain"
        )


def make_dict_with_counts(some_list: list) -> dict:
    dict_with_counts = dict()
    for item in some_list:
        if item in dict_with_counts:
            dict_with_counts[item] += 1
        else:
            dict_with_counts[item] = 1
    return dict_with_counts


if __name__ == "__main__":
    homestation_app.run(debug=True)
