import random
random_num=random.randint(1,99)
print("Hello, this game is guess number game, we consider a random 1,100 number")
print("and you should guess what is the number. enjoy!")
print("")
name=input('what is your nickname my friend? ')
guess=int(input("What's your guess: "))
count=1
lives=10
#while count<=5:
while guess!=random_num and count<=9:
    lives=lives-1
    print("you have",lives,"live")
    if guess>random_num:
        print("The number is smaller")
    else:
        print("the number is bigger")
    count=count+1
    guess=int(input("What's your guess:"))
if count==5:
    print("you lost",name,", sorry!")
else:
    print("Thats the number!!! Welldone",name,"!")
    print("with",lives,"lives left")
input()

        