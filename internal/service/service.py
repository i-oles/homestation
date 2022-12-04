from abc import abstractmethod, ABCMeta

from internal.domain import domain


class ServiceInterface(metaclass=ABCMeta):
    @abstractmethod
    def turn_on(self, params: domain.LightParams) -> list[domain.BulbSettings]:
        raise NotImplementedError
