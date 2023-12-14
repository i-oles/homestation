def get_all_ips(self) -> list[str]:
    bulb = Query()
    bulb_data = self.db.search(bulb.active is True)

    if not bulb_data:
        raise Exception("Could not found any bulb")

    ips = []

    for bulb in bulb_data:
        ip = bulb.get("ip")
        if ip is "":
            raise Exception(f"Could not found any ip for bulb: {bulb}")

        ips.append(ip)

    return ips


def old_home():
    # TODO: here somewhere should be a state update
    possible_tags = set()

    all_tags_from_db = light_repo.get_all_tags()
    all_active_tags = list()

    active_bulbs = mock_discover_bulbs()
    if not MOCK_BULBS:
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

def make_dict_with_counts(some_list: list) -> dict:
    dict_with_counts = dict()
    for item in some_list:
        if item in dict_with_counts:
            dict_with_counts[item] += 1
        else:
            dict_with_counts[item] = 1
    return dict_with_counts

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



    def turn_on_preset(self, params: domain.TurnOnParams) -> list[domain.BulbSettings]:
        pass

    #
    #     # TODO: implement this method
    #
    #     settings: List[domain.BulbSettings] = []
    #     ips_to_turn_off: List[str] = []
    #
    #     for bulb in self.db:
    #         if bulb is None:
    #             continue
    #
    #         bulb_type = bulb.get(TYPE, DEFAULT_TYPE)
    #
    #         bulb_ip = bulb.get(IP)
    #         if bulb_ip is None:
    #             continue
    #
    #         tag = bulb.get(PRESET).get(params.tag)
    #         if not tag:
    #             ips_to_turn_off.append(bulb_ip)
    #             continue
    #
    #         settings.append(
    #             domain.BulbSettings(
    #                 ip=bulb_ip,
    #                 type=bulb_type,
    #                 luminance=tag,
    #             )
    #         )
    #
    #     repo_response = domain.RepoResponse(
    #         settings=settings,
    #         to_turn_off=ips_to_turn_off,
    #     )
    #
    #     # FIXME: code breaks when bulb is switched off
    #     [Bulb(bulb).turn_off() for bulb in repo_response.to_turn_off]
    #
    #     bulb_settings = repo_response.settings
    #
    #     # TODO: add slow turning on the light
    #     # TODO: check how bulbs works when type RGB
    #     for setting in bulb_settings:
    #         bulb = Bulb(setting.ip, effect="smooth")
    #         bulb.set_brightness(setting.luminance)
    #         bulb.turn_on()
    #
    #     return bulb_settings
    #
    def turn_off_all(self, params: domain.TurnOffParams) -> list[domain.BulbSettings]:
        pass
    #
    #     # TODO: implement this method
    #
    #     ips_to_turn_off = []
    #
    #     for bulb in self.db:
    #         bulb_ip = bulb.get(IP)
    #         if not bulb_ip:
    #             logging.error(f"could not find 'ip_address' of bulb: {bulb}")
    #
    #         bulb_id = bulb.get(ID)
    #         if not bulb_id:
    #             logging.error(f"could not find 'id' of bulb: {bulb}")
    #
    #         for param in params.ids:
    #             if param == bulb_id:
    #                 ips_to_turn_off.append(bulb_ip)
    #
    #     [Bulb(bulb).turn_off() for bulb in ips_to_turn_off]
    #
    #     return ips_to_turn_off


    # def get_all_tags(self) -> list:
    #     all_bulbs = self.db.all()
    #
    #     if not all_bulbs:
    #         raise Exception("Could not found any bulb")
    #
    #     for bulb in all_bulbs:
    #         presets = bulb.get("preset")
    #         [all_bulbs.append(tag) for tag in presets.keys()]
    #
    #     return all_bulbs
    #

    # def is_bulb_active(self, ip: str) -> bool:
    #     bulb = Query()
    #     bulb_data = self.db.search(bulb.ip == ip)
    #
    #     if not bulb_data:
    #         raise Exception("Bulb not found")
    #
    #     return bulb_data[0].get("active")



    def validate_bulb_state(is_active_model: bool, is_active_param: bool):
        if is_active_model != is_active_param:
            raise Exception(f"bulb is active: {is_active_model} but param is: {is_active_param}")




    def update_bulb_luminance(self, luminance: int, ip: str):
        bulb = Query()
        self.db.update({"luminance": luminance}, bulb.ip == ip)

    def get_all_tags_by_ip(self, ip: str) -> list[str]:
        bulb = Query()
        bulb_data = self.db.search(bulb.ip == ip)

        if not bulb_data:
            raise Exception("Bulb not found")

        presets = bulb_data[0].get("preset")
        return presets.keys()

    @dataclass
    class TurnOnParams:
        # TODO: here will be another field for bulb color settings
        tag: str

    @dataclass
    class TurnOffParams:
        ids: List[str]

    @dataclass
    class RepoResponse:
        settings: List[BulbSettings]
        to_turn_off: List[str]

