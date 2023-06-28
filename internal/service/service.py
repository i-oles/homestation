from abc import abstractmethod, ABCMeta
from typing import List

from internal.domain import domain

DEFAULT_TYPE = "white"


class ServiceInterface(metaclass=ABCMeta):
    @abstractmethod
    def turn_on(self, params: domain.TurnOnParams) -> List[domain.BulbSettings]:
        raise NotImplementedError

    @abstractmethod
    def turn_off(self, params: domain.TurnOffParams) -> list:
        raise NotImplementedError
