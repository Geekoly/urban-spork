age=[]
a=1
while a!=(-1):
    a=int(input())
    age.append(a)
maximum=age[0]
minimum=age[0]
for i in age:
    if i<maximum:
        maximum=i
print(maximum)