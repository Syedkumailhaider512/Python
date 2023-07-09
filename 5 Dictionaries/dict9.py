fav_languages = {'jen': ['python', 'ruby'], 'sarah': ['c'], 'edward': ['ruby', 'go'], 'phil': ['python', 'haskell']}
# Show all responses for each person.
for name, langs in fav_languages.items():
    print(name + ": ")
    for lang in langs:
        print("- " + lang)
