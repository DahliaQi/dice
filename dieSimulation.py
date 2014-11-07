#! /usr/bin/env python
import random

print ("Start throw a dice!")

sides = raw_input("How many sides on your die? ")

die = random.randint(1,int(sides))

print("The die shows " + str(die) + ". ")