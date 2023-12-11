from tinydb import TinyDB, Query, where

from internal.domain import domain
from internal.repository.bulb.repository import BulbRepoInterface


class BulbRepo(BulbRepoInterface):
    def __init__(self, db: TinyDB):
        self.db = db

    def get_bulb(self, ip: str) -> domain.BulbModel:
        bulb = Query()
        bulb_data = self.db.search(bulb.ip == ip)

        if not bulb_data:
            raise Exception("Bulb not found")

        return domain.BulbModel(
            id=bulb_data[0].get("id"),
            ip=bulb_data[0].get("ip"),
            type=bulb_data[0].get("type"),
            active=bulb_data[0].get("active"),
            luminance=bulb_data[0].get("luminance"),
            preset=bulb_data[0].get("preset"),
        )

    def get_all_tags_by_ip(self, ip: str) -> list[str]:
        bulb = Query()
        bulb_data = self.db.search(bulb.ip == ip)

        if not bulb_data:
            raise Exception("Bulb not found")

        presets = bulb_data[0].get("preset")
        return presets.keys()

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
    def update_bulb_state(self, is_on: bool, ip: str):
        bulb = Query()
        self.db.update({"is_on": is_on}, bulb.ip == ip)

    def update_bulb_luminance(self, luminance: int, ip: str):
        bulb = Query()
        self.db.update({"luminance": luminance}, bulb.ip == ip)

    def get_all_ips(self) -> list[str]:
        return [bulb.get("ip") for bulb in self.db.all()]

    # def is_bulb_active(self, ip: str) -> bool:
    #     bulb = Query()
    #     bulb_data = self.db.search(bulb.ip == ip)
    #
    #     if not bulb_data:
    #         raise Exception("Bulb not found")
    #
    #     return bulb_data[0].get("active")
    def get_id_by_ip(self, ip: str):
        bulb = Query()
        bulb_data = self.db.search(bulb.ip == ip)

        if not bulb_data:
            raise Exception("Bulb not found")

        return bulb_data[0].get("id")



