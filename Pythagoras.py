import math
def Hypotenuse(leg1,leg2):
    x=(leg1*leg1)+(leg2*leg2)
    ans=math.sqrt(x)
    return ans
def leg_cal(leg,hypo):
    b=(hypo*hypo)-(leg*leg)
    ans=math.sqrt(b)
    return ans
def whole():
    print()
    choice=input("do you want to get Hypotenuse length(1) or a leg(2): ")
    if choice=="1":
        num1=float(input("Enter leg1: "))
        num2=float(input("Enter leg2: "))
        print("the hypotenuse length is",Hypotenuse(num1,num2))
    elif choice=="2":
        Hypo=float(input("Enter the Hypotenuse: "))
        num=float(input("Enter the leg: "))
        print("the another leg length is",leg_cal(num,Hypo))
    else:
        print("i dont have any option's for number",choice)
        exit()
print("Created by Roham")
password=input("Enter the PassWord: ")
if password=="Rm12341234!":
    whole()
    while True:
        i = input("do you wanna recalculate?y/n: ")
        if i=="y":
            whole()
        elif i=='n':
            break
else:
    print("password is wrong!!!")
    input()
    exit()
print("have a good Pythagorasy day :)")
input()