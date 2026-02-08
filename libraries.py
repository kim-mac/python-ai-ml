import random   #can also use "from random import choice" just to be specific and make the code shorter
import statistics #for mean
import sys #for input from the command line/terminal

#coin flip
coin = random.choice(["heads","tails"])
print(coin)

#random number
number = random.randint(1,10)
print(number)

#shuffle the data
cards = ["jack","queen","king"]
random.shuffle(cards)
print(cards)

#mean of numbers
avg = statistics.mean([10,45,78])
print(avg)

#sys.argv example

print("Hello my name is", sys.argv[1])