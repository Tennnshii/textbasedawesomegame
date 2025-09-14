# Text-Based RPG (Python)

This is a simple text-based role-playing game built in Python.  
It demonstrates object-oriented programming concepts such as classes, inheritance, and reusable components.  
Players and enemies share common stats (health, mana, strength, agility), and enemies can have resistances or weaknesses to different damage types.

---

## Project Structure

```
textbasedawesomegame/
│
├── model/
│   ├── __init__.py
│   ├── stats.py          # Stats class (HP, MP, STR, AGI)
│   ├── damage.py         # DamageType enum (PHYSICAL, FIRE, etc.)
│   ├── characters.py     # Base Character class with damage logic
│   ├── player.py         # Player class (attack, slash, fireball)
│   └── enemy.py          # Enemy class (inherits from Character)
│
├── MainApplication.py    # Main game loop and entry point
└── README.md             # Project documentation
```

---

## Features

- **Reusable Stats**: Both players and enemies use the same `Stats` class.  
- **Damage Types**: Implemented using an enum (`DamageType`).  
- **Resistances & Weaknesses**: Enemies can take reduced or increased damage based on type.  
  - Example: `DamageType.PHYSICAL: 0.7` → takes 70% of physical damage.  
  - Example: `DamageType.FIRE: 1.5` → takes 150% of fire damage.  
- **Player Actions**:  
  - `Attack`: basic physical hit.  
  - `Slash`: stronger physical hit, costs MP.  
  - `Fireball`: magic fire attack, costs MP.  
- **Simple Enemy AI**: Enemies attack back with their base strength.  

---

## Requirements

- Python 3.10+ recommended  
- Install dependencies:

```bash
pip install pyfiglet
```

---

## Running the Game

From the project root, run:

```bash
python MainApplication.py
```

---

## Example Gameplay

```
NO MAN'S LAND

--- Status ---
Player  [Rudeus]  HP:100 MP:50 STR:15 AGI:10
Enemy   [Slime]   HP:60 MP:0 STR:5 AGI:5
--------------------------------

Choose your action:
  1) Attack (Physical)
  2) Slash  (1.25x, -10 MP)
  3) Fireball (Fire, -12 MP)
> 1

Rudeus attacks (15 base).
Slime took 10 physical damage (x0.7). HP 60 -> 50
Slime attacks! (5 base)
Rudeus took 5 physical damage. HP 100 -> 95
```
