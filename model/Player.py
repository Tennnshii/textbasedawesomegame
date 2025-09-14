class Stats:
    def __init__(self, health=100, mana=50, strength=10, agility=10):
        self.health = health
        self.mana = mana
        self.strength = strength
        self.agility = agility

    def display_stats(self):
        return f"Health: {self.health}, Mana: {self.mana}, Strength: {self.strength}, Agility: {self.agility}"


class Player:
    def __init__(self, name, stats=None):
        self.name = name
        self.stats = stats if stats else Stats()

    def attack(self, enemy):
        damage = self.stats.strength
        enemy.stats.health -= damage
        if enemy.stats.health < 0:
            enemy.stats.health = 0
        print(f"{self.name} attacked {enemy.name} for {damage} damage!")
        if enemy.stats.health == 0:
            print(f"{enemy.name} is dead!")

    def slash(self, enemy):
        if self.stats.mana >= 10:
            damage = int(self.stats.strength * 1.25)
            enemy.stats.health -= damage
            self.stats.mana -= 10
            if enemy.stats.health < 0:
                enemy.stats.health = 0
            print(f"{self.name} used Slash! {enemy.name} took {damage} damage!")
            if enemy.stats.health == 0:
                print(f"{enemy.name} is dead!")
        else:
            print(f"{self.name} does not have enough mana to use Slash!")

    def display_stats(self):
        return f"{self.name}'s Stats -> {self.stats.display_stats()}"