'''#list
list = [1,2 ,3 ,4 ]
touple = (1, 2, 3, 4)
set = {1, 2, 3, 4}
dictionary = {"Name": "Kumail", "Age":"19","Class":"BS Artificial Intelligence 4th M(B)"}

print(list)
print(type(list))
print(touple)
print(type(touple))
print(set)
print(type(set))
print(dictionary)
print(type(dictionary))
#print(dictionary("Name"))

a= 12
b = "Hasilpur"
name = "Kumail"

#import keyword

#print(keyword.kwlist)

a = input("Enter Your First Number = ")
b = input("Enter Your Sure Number = ")

print(int(a)+int(b)) '''


import random
import click

answer = random.randint(1,100)
counter = 1
guess= int(input("Guess the Number = "))

while guess != answer:

    if guess< answer:
        print("Guess Higher!")

    else:
        print("Guess Lower!")

    click.clear()
    guess = int(input("Again Guess the Number = "))
    counter += 1


print("Correct Answer!")
print(counter,"Times Guesses Attempted")