firstName = "Kumail"
print(firstName)
fullName = "Syed Kumail Haider"
print(fullName)

score1 = int(input("Enter the score 1: "))
score2 = int(input("Enter the score 2: "))
totalString = score1 + score2
messageString = "Total score is %s "

print(messageString % totalString)

totalInt = int(score1) + int(score2)
messageString = "Total score is %s "
print(messageString % totalInt)

score1 = int(input("Enter the score 1: "))
score2 = int(input("Enter the score 2: "))
total = score1 + score2
messageString = "score1(%s ) + score2[%s ] = %s "
print(messageString % (score1, score2, total))
