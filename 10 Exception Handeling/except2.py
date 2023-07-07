# Handling the Exception

try:
    a = int(input("Enter First Number: "))
    b = int(input("Enter Divider Number: "))
    c = a / b

    print("Answer: " + str(c))

except:
    print("Error!")