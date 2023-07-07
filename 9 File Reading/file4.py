# Creating and add data in txt file

file = "new_file.txt"

with open(file, 'w+') as f:
    f.write("Hello World!")