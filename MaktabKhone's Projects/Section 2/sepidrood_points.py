points=[]
count=1
while count<=30:
    a=int(input())
    points.append(a)
    count=count+1
print(points)
count2=0
count3=0
for i in points:
    if i==3:
        count2=count2+1        
    elif i==1:
        count3=count3+1        
win_points=count2*3
whole_point=count3+win_points
print(whole_point,"",count2)