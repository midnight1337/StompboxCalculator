"""
Transistor is initialised in Circuit class. It initialises and represents all transistors dataclasses(Bjt)
TransistorMeta is metaclass used to make sure, only one Transistor instance was initialised in Circuit.
"""
from bjt import Bjt


class TransistorMeta(type):
    __instance = None

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__call__(*args, **kwargs)
            return cls.__instance
        else:
            raise Exception("Only one Transistor object is allowed!")


class Transistor(metaclass=TransistorMeta):
    def __init__(self, transistors_blueprint: dict[str, dict[str, str | int]]):
        self.__transistors: dict[str, Bjt] = {}
        self.transistors_blueprint: dict[str, dict[str, str | int]] = transistors_blueprint
        self.initialise_bjt_transistors()

    def __call__(self, model: str) -> Bjt:
        """Can use object as function"""
        return self.__transistors[model]

    @property
    def transistors(self) -> dict[str, Bjt]:
        return self.__transistors

    def initialise_bjt_transistors(self):
        for q in self.transistors_blueprint:
            new_transistor: Bjt = Bjt(**self.transistors_blueprint[q])

            if new_transistor.model not in self.__transistors.keys():
                self.__transistors[new_transistor.model] = new_transistor

    def sort_transistors_by_name(self):
        # TODO: use some sorting algorithm (quick sort??)
        for model, transistor in self.__transistors:
            pass

    def sort_transistors_by_hfe(self):
        pass