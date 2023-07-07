# Creating txt file and adding data from other txt file

file = "file.txt"

with open(file, 'r') as f:
    lines = f.readlines()


with open("new_file1.txt", 'w+') as f:
    for line in lines:
        f.write(line)