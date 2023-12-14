from yeelight import Bulb
from internal.domain import domain
from internal.repository.bulb.repository import BulbRepoInterface
from internal.service.service import ServiceInterface


class Light(ServiceInterface):
    def __init__(self, repo: BulbRepoInterface):
        self.repo = repo

    def toggle_single_bulb(
        self, params: domain.ToggleSingleParams
    ) -> domain.BulbSettings:
        bulb_model = self.repo.get_bulb(params.ip)

        if bulb_model is None:
            raise Exception(f"could not find bulb with ip: {params.ip}")

        bulb = Bulb(params.ip)
        bulb.toggle()

        self.repo.update_bulb_state(params.is_on, params.ip)

        return domain.BulbSettings(
            ip=params.ip,
            is_active=params.is_on,
        )
