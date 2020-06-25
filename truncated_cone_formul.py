def tcf():
    import math
    S1=float(input("masahate ghaede ye aval ra vared konid: "))
    S2=float(input("masahate ghaede ye dovom ra vared konid: "))
    h=float(input("ertefa ra vared konid: "))
    radical=math.sqrt(S1*S2)
    V=h/3*(S1+S2+radical)
    print("hajm makhroot naghes",V,"ast")

while True:
     tcf()
     i = input("dobare az aval?y/n: ")
     if i=='n':
          break
        
print("have a good math day!!!!")
input()