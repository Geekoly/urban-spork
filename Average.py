num=1
nums=[]
nums_float=[]
x=0
while num != '':
    num=input("enter a num:")
    nums.append(num)		
nums.remove(num)
for i in nums:
    float_i=float(i)
    x=x+float_i
ave=x/len(nums)
print("the total of the nums: ",x)
print("the average of the numbers is",ave)
input()