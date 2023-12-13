from flask import Flask, request, json, Response, render_template
from tinydb import TinyDB
from yeelight import discover_bulbs, Bulb
from config.config import MOCK_BULBS
from internal.domain import domain
from config import config
from internal.mock.yeelight.mock import mock_discover_bulbs
from internal.service.light.light import Light
import os
from internal.repository.bulb.tinydb.repository import BulbRepo

homestation_app = Flask(__name__)

absolute_path = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(absolute_path, config.DB_FILE_NAME)
db = TinyDB(db_path)

light_repo = BulbRepo(db)
service = Light(light_repo)


@homestation_app.route("/")
def home():
    # TODO: here somewhere should be a state update
    active_bulbs = mock_discover_bulbs()
    if not MOCK_BULBS:
        active_bulbs = discover_bulbs()

    online_ips = [bulb.get("ip") for bulb in active_bulbs]
    all_ips = light_repo.get_all_ips()
    offline_ips = list(set(all_ips) - set(online_ips))

    bulb_states = dict()

    for ip in online_ips:
        bulb_id = light_repo.get_id_by_ip(ip)

        bulb_state = domain.BulbState(
            ip=ip,
            is_on=False,
            is_online=True,
        )

        power = Bulb(ip).get_capabilities().get("power")
        if power == "on":
            bulb_state.is_on = True

        bulb_states[bulb_id] = bulb_state

    for ip in offline_ips:
        bulb_id = light_repo.get_id_by_ip(ip)
        bulb_state = domain.BulbState(
            ip=ip,
            is_on=False,
            is_online=False,
        )

        bulb_states[bulb_id] = bulb_state

    print(bulb_states)

    return render_template("index.html", bulb_states=bulb_states)


@homestation_app.route("/toggle_single", methods=["POST"])
def toggle_single():
    if request.is_json:
        req = request.get_json()

        params = domain.ToggleSingleParams(
            ip=req["ip"],
            is_on=True,
            # is_on=req["is_on"]
        )

        bulb_settings = service.toggle_single_bulb(params)

        return Response(
            response=json.dumps(bulb_settings), status=200, mimetype="text/plain"
        )


# @homestation_app.route("/turn_on_preset", methods=["POST"])
# def turn_on_preset():
#     if request.is_json:
#         req = request.get_json()
#         tag = domain.TurnOnParams(tag=req["tag"])
#         bulb_settings = service.turn_on(tag)
#
#         return Response(
#             response=json.dumps(bulb_settings), status=200, mimetype="text/plain"
#         )
#
#
# @homestation_app.route("/turn_off_all", methods=["POST"])
# def turn_off_all():
#     if request.is_json:
#         req = request.get_json()
#         tag = domain.TurnOffParams(ids=req["ids"])
#         ips_to_turn_off = service.turn_off(tag)
#
#         return Response(
#             response=json.dumps(ips_to_turn_off), status=200, mimetype="text/plain"
#         )
#

if __name__ == "__main__":
    homestation_app.run(debug=True)
