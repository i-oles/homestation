from abc import abstractmethod, ABCMeta

from internal.domain import domain

PRESET = "preset"
IP = "ip"


class RepoInterface(metaclass=ABCMeta):
    @abstractmethod
    def turn_on(self, params: domain.LightParams) -> domain.RepoResponse:
        raise NotImplementedError