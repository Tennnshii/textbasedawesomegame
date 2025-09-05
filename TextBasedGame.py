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
    if new_enemy_hp == 0: print ("enemy is fucked")
    return new_enemy_hp



enemy_hp = player_attacks_enemy (player_attack, enemy_hp)