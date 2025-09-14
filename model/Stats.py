class Stats:
    def __init__(self, health=100, mana=50, strength=10, agility=10):
        self.health = health
        self.mana = mana
        self.strength = strength
        self.agility = agility

    def display(self) -> str:
        return (
            f"HP:{self.health} MP:{self.mana} "
            f"STR:{self.strength} AGI:{self.agility}"
        )
