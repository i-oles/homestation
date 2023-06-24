from abc import abstractmethod, ABCMeta

from internal.domain import domain

PRESET = "preset"
IP = "ip"
TYPE = "type"
ID = "id"


class RepoInterface(metaclass=ABCMeta):
    @abstractmethod
    def turn_on(self, params: domain.TurnOnParams) -> domain.RepoResponse:
        raise NotImplementedError

    def turn_off(self, params: domain.TurnOffParams) -> list:
        raise NotImplementedError