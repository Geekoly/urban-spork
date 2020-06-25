import math

friends=[1,10,20]
count=0
for i in friends:
    print(i,("|"),math.sqrt(i),("|"),i**2)
    count=count+1

print("i printed",count,"numbers")
input()