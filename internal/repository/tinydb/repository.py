from tinydb import TinyDB, Query


class TinyDBRepository:
    def __init__(self, db: TinyDB):
        self.db = db

    def get_all_tags_by_ip(self, ip: str) -> list:
        bulb = Query()
        bulb_data = self.db.search(bulb.ip == ip)

        if not bulb_data:
            raise Exception("Bulb not found")

        presets = bulb_data[0].get("preset")
        return presets.keys()

    def get_all_tags(self) -> list:
        all_bulbs = self.db.all()

        if not all_bulbs:
            raise Exception("Could not found any bulb")

        for bulb in all_bulbs:
            presets = bulb.get("preset")
            [all_bulbs.append(tag) for tag in presets.keys()]

        return all_bulbs
