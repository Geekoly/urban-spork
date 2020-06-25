def meters_conv(meter):
    print("cm")
    print("inch")
    print("mm")
    print("foot-feet")
    print("km")
    print("mile")
    print("yard")
    print("------")
    des=input("")
    if des=="cm":
        cm=meter*100
        print(cm)



def whole():
    print("do you want to convert from:")
    print("meter")
    print("------")
    des=input("")
    if des=="meter":
        meter=input("enter meter value: ")
        print("convert to: ")
        meters_conv(meter)

whole()