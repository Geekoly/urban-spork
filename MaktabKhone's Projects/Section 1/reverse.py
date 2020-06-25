num=int(input())
num2=num%100
num3=str(num2%10)+str(num2//10)+str(num//100)
print(int(num3)*2)