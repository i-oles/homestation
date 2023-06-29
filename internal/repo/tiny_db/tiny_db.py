import logging
from typing import List

from tinydb import TinyDB

from internal.domain import domain
from internal.repo.repo import RepoInterface, IP, ID, PRESET, TYPE
from internal.service.service import DEFAULT_TYPE


class TinyDbRepo(RepoInterface):
    def __init__(self, db: TinyDB):
        self.db = db

    def turn_on(self, params: domain.TurnOnParams) -> domain.RepoResponse:
        settings: List[domain.BulbSettings] = []
        ips_to_turn_off: List[str] = []

        for bulb in self.db:
            if bulb is None:
                continue

            bulb_type = bulb.get(TYPE, DEFAULT_TYPE)

            bulb_ip = bulb.get(IP)
            if bulb_ip is None:
                continue

            # if not bulb_ip:
            #     logging.error(f"could not find 'ip_address' of bulb: {bulb}")

            tag = bulb.get(PRESET).get(params.tag)
            if not tag:
                ips_to_turn_off.append(bulb_ip)
                continue

            settings.append(
                domain.BulbSettings(
                    ip=bulb_ip,
                    type=bulb_type,
                    luminance=tag,
                )
            )

        return domain.RepoResponse(
            settings=settings,
            to_turn_off=ips_to_turn_off,
        )

    def turn_off(self, params: domain.TurnOffParams) -> list:
        ips_to_turn_off = []

        for bulb in self.db:
            bulb_ip = bulb.get(IP)
            if not bulb_ip:
                logging.error(f"could not find 'ip_address' of bulb: {bulb}")

            bulb_id = bulb.get(ID)
            if not bulb_id:
                logging.error(f"could not find 'id' of bulb: {bulb}")

            for param in params.ids:
                if param == bulb_id:
                    ips_to_turn_off.append(bulb_ip)

        return ips_to_turn_off