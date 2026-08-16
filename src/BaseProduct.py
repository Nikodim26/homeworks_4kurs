from abc import ABC, abstractmethod


class BaseProduct(ABC):
    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @abstractmethod
    @property
    def price(self) -> float:
        pass

    @abstractmethod
    @price.setter
    def price(self, new_price) -> None:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def __add__(self, other) -> float:
        pass
