from abc import abstractmethod, ABCMeta
from internal.domain import domain

DEFAULT_TYPE = "white"


class ServiceInterface(metaclass=ABCMeta):
    @abstractmethod
    def toggle_single_bulb(
        self, params: domain.ToggleSingleParams
    ) -> domain.BulbSettings:
        raise NotImplementedError
