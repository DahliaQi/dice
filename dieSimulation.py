#! /usr/bin/env python
import random

print ("Start throw a dice!")

dice = int(raw_input("How many dice would you like to roll?"))
sides = int(raw_input("How many sides on your die? "))

for number in range(1, dice + 1):
	die = random.randint(1,sides)
	print("The die shows " + str(die) + ". ")