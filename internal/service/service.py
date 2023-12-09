from abc import abstractmethod, ABCMeta
from internal.domain import domain

DEFAULT_TYPE = "white"


class ServiceInterface(metaclass=ABCMeta):
    @abstractmethod
    def toggle_single_bulb(self, params: domain.ToggleSingleParams) -> domain.BulbSettings:
        raise NotImplementedError

    @abstractmethod
    def turn_on_preset(self, params: domain.TurnOnParams) -> list[domain.BulbSettings]:
        raise NotImplementedError

    @abstractmethod
    def turn_off_all(self, params: domain.TurnOffParams) -> list[domain.BulbSettings]:
        raise NotImplementedError
