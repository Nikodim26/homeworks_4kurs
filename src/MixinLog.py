class MixinLog:

    def __init__(self) -> None:
        print(self)

    def __repr__(self) -> str:
        return str(self)
