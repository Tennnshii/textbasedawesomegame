from model.Player import Player, Stats

player = Player("Rudeus", Stats(100, 50, 15, 10))
enemy = Player("Slime", Stats(30, 0, 5, 5))

while player.stats.health > 0 and enemy.stats.health > 0:
    action = input("Choose your action: (1) Attack (2) Slash\n")
    if action == "1":
        player.attack(enemy)
    elif action == "2":
        player.slash(enemy)
    else:
        print("Invalid action.")

    # Enemy's turn to attack
    if enemy.stats.health > 0:
        enemy.attack(player)
