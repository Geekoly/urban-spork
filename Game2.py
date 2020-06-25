import random
guess=random.randint(1,1000)
name=input("What is your nickname mi Amigo: ")
print()
print("consider a number in 1,1000 range")
print("")
enter=input("did you consider it ?(press enter key)")
print("my guess is",guess)
if enter=="":
    answer=input("your number is bigger (b) , smaller (s) or it is the number you consider(i)? ")
    a=1
    b=1000
while answer!='i':
    if answer=="b":   
        a=guess
        guess=random.randint((a+1),(b-1))
    elif answer=="s":
        b=guess
        guess=random.randint((a+1),(b-1))
    print("my guess is",guess)
    answer=input("your number is bigger (b) , smaller (s) or it is the number you consider(i)? ")
print("yay i did it",name,"!!!"," its",guess)
input()