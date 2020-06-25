import random
guess=random.randint(1,99)
print("consider a number in 1,100 range")
print(guess)

answer=input()
a=1
b=99
while answer!='d':
    if answer=="b":   
        a=guess
        guess=random.randint((a+1),(b-1))
    elif answer=="k":
        b=guess
        guess=random.randint((a+1),(b-1))
    print(guess)
    answer=input()
print(guess)