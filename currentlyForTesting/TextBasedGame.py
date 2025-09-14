from pyfiglet import Figlet


def create_and_print_ascii_art(enter_characters):
    f = Figlet(font="slant")
    ascii_art = f.renderText(enter_characters)
    print(ascii_art)

create_and_print_ascii_art("NO MAN'S LAND")

player_name = "Rudeus"
player_hp = 100
player_attack = 15
player_mp = 50 


enemy_name = "Slime"
enemy_hp = 30
enemy_attack = 5


def player_attacks_enemy(playerAttack, enemyHP):
    new_enemy_hp = enemyHP - playerAttack
    if new_enemy_hp < 0: new_enemy_hp = 0
    print(f"enemy took {player_attack} damage")
    if new_enemy_hp == 0: print ("enemy is dead")
    return new_enemy_hp

def slash(playerAttack, player_mp, enemyHP):
    new_enemy_hp = enemyHP - playerAttack * 1.25
    player_mp = player_mp - 10
    if new_enemy_hp < 0: new_enemy_hp = 0
    print(f"You used Slash! Enemy took {player_attack * 1.25} damage")
    if new_enemy_hp == 0: print ("enemy is dead")
    return new_enemy_hp





while player_hp > 0 and enemy_hp > 0:
    playerinput = int(input("1 - Attack\n2 - Slash\n"))
    if playerinput == 1: 
        enemy_hp = player_attacks_enemy (player_attack, enemy_hp)
        create_and_print_ascii_art("l")
    elif playerinput == 2:
        enemy_hp = slash(player_attack, player_mp, enemy_hp)
        create_and_print_ascii_art("X")
    else: 
        print("Invalid Entry")