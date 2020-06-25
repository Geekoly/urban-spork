def USD_to_Rial():
    USD=float(input("Enter the USD Value: "))
    Rial=USD*170700
    Toman=Rial/10
    print("The",USD,"Doller is",Rial,"Rial")
    print("or",Toman,"Toman(Side Currency in IRAN)")
    return Toman
def Toman_or_Rial_to_USD():
    iran=input("do you wanna convert from TOMAN or RIAL?(in CAPS): ")
    if iran=='TOMAN':
        Toman=float(input("Enter the TOMAN Value: "))
        USD=Toman/17070
        print("The",Toman,"Toman is",USD,"Doller")
    elif iran=='RIAL':
        Rial=float(input("Enter the RIAL Value: "))
        USD=Rial/170700
        print("The",Rial,"Rial is",USD,"Doller")     
def main():
    des=input("do you want to convert USD to Rial(1) or reverse(2) an put any number fo exit? ")                                                 
    if des=='1':
        USD_to_Rial()
    elif des=='2':
        Toman_or_Rial_to_USD()   
    else:
        print("Have a Good Day! ")
main()
while True:
    print()
    i=input("do you wanna reconvert(y/n)? ")
    if i=='y':
    	main()
    elif i=='n':
        break
print()
print('thanks for using this proggram')
input()