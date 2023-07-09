# Using Positional Arguments

def describe_pet(animal = 'hamster', name = 'None'):
    """Display information about a pet."""
    print("\nI have a " + animal + ".")
    print("Its name is " + name + ".")


describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

describe_pet()
describe_pet(animal='lion', name='Simba')