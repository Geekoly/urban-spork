def s_to_b():
    num=1
    nums=[]
    nums_float=[]
    while num != '':
        num=input("enter a num:")
        nums.append(num)
    nums.remove(num)
    for i in nums:
        nums_float.append(float(i))
    nums2=[]
    count=1
    x=len(nums_float)
    while count<=x:
        i=min(nums_float)
        nums_float.remove(i)
        nums2.append(i)
        count=count+1
    print(nums2)
    print("length of the list:",x)
def b_to_s():
    num=1
    nums=[]
    nums_float=[]
    while num != '':
        num=input("enter a num:")
        nums.append(num)
    nums.remove(num)
    for i in nums:
        nums_float.append(float(i))
    nums2=[]
    count=1
    x=len(nums_float)
    while count<=x:
        i=max(nums_float)
        nums_float.remove(i)
        nums2.append(i)
        count=count+1
    print(nums2)
    print("length of the list:",x)
def whole():
    choice=input("bigger to smaller(1) or reverse (2): ")
    if choice=="1":
        b_to_s()
    elif choice=="2":
        s_to_b()
    else:
        print("we dont have anything for ",choice)
print("Created by Roham")
print("for starting the orginazition, you need to just press enter without any typing.")
whole()
while True:
    print()
    i=input("Do you want to reorganize? y/n: ")
    if i=="y":
        whole()
    elif i=="n":
        print()
        print("i hope this was useful :)")
        break 
    else:
        print()
        print("i consider this as a 'no' :(")
        break
print()
print("Created by Roham")
input()