from model import Player, Enemy, Stats, DamageType
from pyfiglet import Figlet


def title_screen(text: str) -> None:
    fig = Figlet(font="slant")
    print(fig.renderText(text))


def print_status(player: Player, enemy: Enemy) -> None:
    print("\n--- Status ---")
    print(f"Player  [{player.name}]  {player.stats.display()}")
    print(f"Enemy   [{enemy.name}]   {enemy.stats.display()}")
    print("-" * 32)


def enemy_turn(player: Player, enemy: Enemy) -> None:
    """Very simple enemy AI: basic physical hit using its STR."""
    if enemy.is_dead():
        return
    dmg = enemy.stats.strength
    print(f"\n{enemy.name} attacks! ({dmg} base)")
    player.take_damage(dmg, DamageType.PHYSICAL)


def main() -> None:
    # Fancy title (optional)
    title_screen("NO MAN'S LAND")

    # Create player
    player = Player("Rudeus", Stats(health=100, mana=50, strength=15, agility=10))

    # Enemy: 30% resistant to PHYSICAL (multiplier 0.7)
    slime_resists = {DamageType.PHYSICAL: 0.7}
    # If you also want it weak to fire, add: DamageType.FIRE: 1.5
    enemy = Enemy("Slime", Stats(health=60, mana=0, strength=5, agility=5),
                  resistances=slime_resists)

    print_status(player, enemy)

    while not player.is_dead() and not enemy.is_dead():
        # Player turn
        choice = input(
            "\nChoose your action:\n"
            "  1) Attack (Physical)\n"
            "  2) Slash  (1.25x, -10 MP)\n"
            "  3) Fireball (Fire, -12 MP)\n> "
        ).strip()

        if choice == "1":
            player.attack(enemy)
        elif choice == "2":
            player.slash(enemy)
        elif choice == "3":
            player.fireball(enemy)
        else:
            print("Invalid action.")
            continue  # don’t give enemy a free turn for a bad input

        # Enemy turn (if still alive)
        if not enemy.is_dead():
            enemy_turn(player, enemy)

        print_status(player, enemy)

    # End
    if player.is_dead() and enemy.is_dead():
        print("\nBoth combatants fell. It's a draw!")
    elif enemy.is_dead():
        print(f"\n{enemy.name} is defeated. You win!")
    else:
        print(f"\n{player.name} fell. Game over.")


if __name__ == "__main__":
    main()
# End of MainApplication.py
