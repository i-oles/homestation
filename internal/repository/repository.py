from abc import abstractmethod, ABCMeta

from internal.domain import domain

PRESET = "preset"
IP = "ip"


class RepositoryInterface(metaclass=ABCMeta):
    @abstractmethod
    def turn_on(self, params: domain.LightParams) -> list[domain.BulbSettings]:
        raise NotImplementedError
