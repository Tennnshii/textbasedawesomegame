from Characters import Character
from Damage import DamageType


class Player(Character):
    def attack(self, target: Character):
        """Basic PHYSICAL attack."""
        damage = self.stats.strength
        print(f"{self.name} attacks ({damage} base).")
        target.take_damage(damage, DamageType.PHYSICAL)

    def slash(self, target: Character):
        """Stronger PHYSICAL hit (1.25x), costs 10 MP."""
        if self.stats.mana < 10:
            print("Not enough MP for Slash!")
            return
        self.stats.mana -= 10
        damage = int(self.stats.strength * 1.25)
        print(f"{self.name} uses Slash ({damage} base). MP:{self.stats.mana}")
        target.take_damage(damage, DamageType.PHYSICAL)

    def fireball(self, target: Character):
        """MAGIC fire spell; flat + scaling damage, costs 12 MP."""
        if self.stats.mana < 12:
            print("Not enough MP for Fireball!")
            return
        self.stats.mana -= 12
        damage = int(20 + self.stats.strength * 0.8)
        print(
            f"{self.name} casts Fireball ({damage} base). "
            f"MP:{self.stats.mana}"
        )
        target.take_damage(damage, DamageType.FIRE)
