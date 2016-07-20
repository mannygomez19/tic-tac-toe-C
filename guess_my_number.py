#!/usr/bin/python

from random import randint
answer = randint(0, 20)

print("I'm thinking of a number between 1 and 20.")

guess = int(input("Take a guess at what number was randomly generated (type any number to continue)")) 

while 0 < guess < 20:

    guess = int(input("What number am I thinking of?: "))

    if guess == answer:
        print("You got it!")
        break
    
    elif guess > answer:
        print("Your guess was too high, try something lower.")

    elif guess < answer:
        print("Your guess was too low, try something higher.")

    try:
        guess = int(input())
    except:
        raise Exception("Please enter a number inbetween 0 and 20.")   

