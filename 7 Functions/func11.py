# Return Dictionary for a person

def build_person(first, last, age=None):
    person = {'first': first, 'last': last}
    if age:
        person['age'] = age

    return person


musician = build_person('jimi', 'hendrix', 27)
print(musician)
musician = build_person('janis', 'joplin')
print(musician)