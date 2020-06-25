age=[]
a=1
while a!=(-1):
    a=int(input())
    age.append(a)
maximum=age[0]

for i in age:
    if i>maximum:
        maximum=i
age.remove(maximum)
minimum=age[0]

for i in age:
    if i>minimum:
        minimum=i
    
print(maximum,minimum)