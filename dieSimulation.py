#! /usr/bin/env python
import random

print("This program simulates rolling several dice.\n The user can choose how many dice are rolled.\n")
print ("Start throw a dice!")
dice = int(raw_input("How many dice would you like to roll?"))


for i in range(dice):
	sides = int(raw_input("How many sides on your " + str(i) + " die? "))
	if sides > 1:
		dice = random.randint(1,sides)
		print("The die shows " + str(dice) + ". ")
	else: 
		print("There's no dice with < 2 sides.")