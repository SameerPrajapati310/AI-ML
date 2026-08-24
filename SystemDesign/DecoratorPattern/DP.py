from abc import ABC, abstractmethod

class Character(ABC):
    @abstractmethod
    def get_abilities(self):
        pass


class Mario(Character):
    def get_abilities(self):
        return "Mario"


class CharacterDecorator(Character):
    def __init__(self, character):
        self.character = character


class HeightUp(CharacterDecorator):
    def get_abilities(self):
        return self.character.get_abilities() + " + Height Up"


class StarPower(CharacterDecorator):
    def get_abilities(self):
        return self.character.get_abilities() + " + Star Power"


mario = Mario()
print(mario.get_abilities())

mario = HeightUp(mario)
print(mario.get_abilities())

mario = StarPower(mario)
print(mario.get_abilities())