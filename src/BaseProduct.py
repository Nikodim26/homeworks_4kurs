from abc import ABC
from abc import abstractmethod


class BaseProduct(ABC):

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def __add__(self, other) -> float:
        pass


class MixinLog:

    def __init__(self) -> None:
        print(self)

    def __repr__(self) -> str:
        return str(self)
