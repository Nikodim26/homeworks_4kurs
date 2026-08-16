from abc import ABC, abstractmethod


class BaseProduct(ABC):

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def __add__(self, other) -> float:
        pass

class MixinLog:

    def __init__(self):
        print(self)

    def __repr__(self):
        return str(self)