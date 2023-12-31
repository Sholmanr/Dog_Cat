from typing import Protocol


class Treat(Protocol):

    amount: int

    def create(self):
        pass

    def print(self):
        pass


class dog_Treat:

    amount : int

    def __init__(self, name: str):
        self.name = name

    def create(self):
        pass

    def print(self):
        pass

class cat_Treat:

    amount: int

    def __init__(self, name: str):
        self.name = name

    def create(self):
        pass

    def print(self):
        pass


def print_treat(treat: Treat):
    treat.print()


friskies: Treat = cat_Treat("Friskies")