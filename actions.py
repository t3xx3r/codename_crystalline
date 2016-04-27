__author__ = 'Hunter Coleman'

# Actions should drive the player somewhere.
# Movement, attack, flee, examine, use an item to further examine something, etc.

class Actions()

class Player(Actions)

class Enemy(Actions)

class Monster(Actions)

class Aim(Player)

class Attack(Player)

class Consume(Player)

class Examine(Player)

class Holster(Player)

class Retreat(Player)

class Aim(Enemy)

class Attack(Enemy)

class Retreat(Enemy)

class Spit(Monster)

class Claw_Atk(Monster)

class Lunge(Monster)

class Cannibalize(Monster)

class Run(Monster)
