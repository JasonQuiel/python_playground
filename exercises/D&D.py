class monster :
   def __init__(self, name, attack, defence):
      self.name = name
      self.attack = attack
      self.defence = defence


enemy = monster('Goblin', 2, 7)

import random
thaco = random.randint(1, 20)


attack_roll = 0

if attack_roll == 0:
   attack_roll = thaco
   print("You rolled a",attack_roll, "on a",enemy.name)
if attack_roll == 20:
   print("Critical Hit!")
if attack_roll == 1:
   print("Critical miss!")

def turn(enemy, thaco):
   if enemy.defence < thaco:
      print("Your attack landed!")
   if enemy.defence > thaco:
      print("Your attack missed!")
turn(enemy, thaco)