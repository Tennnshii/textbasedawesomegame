from Stats import Stats
from Damage import DamageType


class Character:
    def __init__(
        self,
        name: str,
        stats: Stats,
        resistances: dict | None = None
    ):
        self.name = name
        self.stats = stats
        self.resistances = resistances or {}

    def take_damage(self, base_damage: int, dmg_type: DamageType) -> int:
        """Apply damage, accounting for resistances/weaknesses."""
        mult = self.resistances.get(dmg_type, 1.0)
        final = max(0, int(round(base_damage * mult)))
        old_hp = self.stats.health
        self.stats.health = max(0, self.stats.health - final)
        print(
            f"{self.name} took {final} {dmg_type.value} damage "
            f"(x{mult}). HP {old_hp} -> {self.stats.health}"
        )
        if self.is_dead():
            print(f"{self.name} is dead!")
        return final

    def is_dead(self) -> bool:
        return self.stats.health <= 0
