from abc import ABC, abstractmethod


class Elf(ABC):

    def __init__(self, name, mus_instrument, favorite_song):
        self.name = name
        self.mus_instrument = mus_instrument
        self.favorite_song = favorite_song

    def play_song(self):
        print(f"Elf {self.name} playing {self.favorite_song} "
              f"on {self.mus_instrument}")

    @abstractmethod
    def fight(self):
        pass


class ElfRanger(Elf):

    def __init__(self, name, mus_instrument, favorite_song, bow: dict):
        super().__init__(name, mus_instrument, favorite_song)
        self.damage = bow["damage"]
        self.bow = bow["name"]

    def fight(self):
        print(f"Elf {self.name} kills his opponent with {self.bow}")


bob = ElfRanger("Bob",
                "lute",
                "Bad Romance",
                {"name": "M249", "damage": 999})
bob.play_song()
bob.fight()
