# Removing values using while loop

pets = ['dog', 'cat', 'dog', 'fish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)