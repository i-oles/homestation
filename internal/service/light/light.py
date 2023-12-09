from typing import List
from yeelight import Bulb
from internal.domain import domain
from internal.repository.bulb.repository import BulbRepoInterface
from internal.service.service import ServiceInterface


def validate_bulb_state(is_active_model: bool, is_active_param: bool):
    if is_active_model != is_active_param:
        raise Exception(f"bulb is active: {is_active_model} but param is: {is_active_param}")


class Light(ServiceInterface):
    def __init__(self, repo: BulbRepoInterface):
        self.repo = repo

    def toggle_single_bulb(self, params: domain.ToggleSingleParams) -> domain.BulbSettings:
        bulb_model = self.repo.get_bulb(params.ip)

        if bulb_model is None:
            raise Exception(f"could not find bulb with ip: {params.ip}")

        validate_bulb_state(bulb_model.active, params.is_active)

        if params.is_active:
            if params.luminance != bulb_model.luminance:
                bulb = Bulb(params.ip, effect="smooth")
                bulb.turn_off()

                self.repo.update_bulb_state(False, params.ip)
                self.repo.update_bulb_luminance(params.luminance, params.ip)

                return domain.BulbSettings(
                    ip=params.ip,
                    is_active=False,
                    luminance=params.luminance,
                )

            bulb = Bulb(bulb_model.ip, effect="smooth")
            bulb.set_brightness(params.luminance)

            self.repo.update_bulb_luminance(params.luminance, params.ip)

            return domain.BulbSettings(
                ip=params.ip,
                is_active=True,
                luminance=params.luminance,
            )

        bulb = Bulb(params.ip, effect="smooth")
        bulb.set_brightness(params.luminance)
        bulb.turn_on()

        self.repo.update_bulb_state(True, params.ip)

        return domain.BulbSettings(
            ip=params.ip,
            is_active=True,
            luminance=bulb_model.luminance,
        )

    def turn_on_preset(self, params: domain.TurnOnParams) -> list[domain.BulbSettings]:

        # TODO: implement this method

        settings: List[domain.BulbSettings] = []
        ips_to_turn_off: List[str] = []

        for bulb in self.db:
            if bulb is None:
                continue

            bulb_type = bulb.get(TYPE, DEFAULT_TYPE)

            bulb_ip = bulb.get(IP)
            if bulb_ip is None:
                continue

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

        repo_response = domain.RepoResponse(
            settings=settings,
            to_turn_off=ips_to_turn_off,
        )

        # FIXME: code breaks when bulb is switched off
        [Bulb(bulb).turn_off() for bulb in repo_response.to_turn_off]

        bulb_settings = repo_response.settings

        # TODO: add slow turning on the light
        # TODO: check how bulbs works when type RGB
        for setting in bulb_settings:
            bulb = Bulb(setting.ip, effect="smooth")
            bulb.set_brightness(setting.luminance)
            bulb.turn_on()

        return bulb_settings

    def turn_off_all(self, params: domain.TurnOffParams) -> list[domain.BulbSettings]:

        # TODO: implement this method

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

        [Bulb(bulb).turn_off() for bulb in ips_to_turn_off]

        return ips_to_turn_off
