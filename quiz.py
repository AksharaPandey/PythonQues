print("Welcome to the Quiz session!")

playing=input("Do you want to play? ")

if playing!="yes":
    print("Uh-oh")
    quit()

print("Okay! let's play o.o")

answer=input("What does ALU stands for? ")
if answer=="Arithmetic Logic Unit":
    print("Correct Answer!")
else:
    print("Oops,Incorrect!")

answer1=input("What does CPU stands for? ")
if answer1=="Central Processing Unit":
    print("Correct Answer!")
else:
    print("Oops,try again")

answer2=input("Who does Akshara loves the most? ")
if answer2=="Chhotu":
    print("True!")
else:
    print("Wrong,Try Again")

answer3=input("What does AM stands for? ")
if answer3=="Anti-Meridian":
    print('You got that right!')
else:
    print("Nooo! Try again")

answer4=input("Who is the PM of India? ")
if answer4=="Narendra Modi":
    print('Right!')
else:
    print("Wrong Answer!")
print("You played well")
print("That was it for the session, Bye!")