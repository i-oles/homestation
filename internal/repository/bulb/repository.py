from abc import abstractmethod, ABCMeta

from internal.domain import domain


class BulbRepoInterface(metaclass=ABCMeta):
    @abstractmethod
    def get_bulb(self, ip: str) -> domain.BulbModel:
        raise NotImplementedError

    @abstractmethod
    def get_all_tags_by_ip(self, ip: str) -> list[str]:
        raise NotImplementedError

    @abstractmethod
    def update_bulb_state(self, is_on: bool, ip: str):
        raise NotImplementedError

    @abstractmethod
    def update_bulb_luminance(self, luminance: int, ip: str):
        raise NotImplementedError

    @abstractmethod
    def get_all_ips(self) -> list[str]:
        raise NotImplementedError
