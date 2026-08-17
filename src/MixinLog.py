class MixinLog:

    def __init__(self) -> None:
        print(self.__repr__())

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', '{self.description}', {self.price}, {self.quantity})"
