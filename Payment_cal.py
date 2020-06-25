def payment_per_day(hour,pay_per_hour):
    if hour>8:
        return 0
    else:
        paycheck=hour*pay_per_hour
        return paycheck
           
def payment_per_week(h,pph):
    if h>8:
        return 0
    else:
        paycheck=h*pph
        pay_per_week=paycheck*7
        return pay_per_week

def payment_per_month(h,pph):
    if h>8:
        return 0
    else:
        paycheck=h*pph
        pay_per_week=paycheck*7
        pay_per_month=pay_per_week*4
        return pay_per_month

h=float(input('how many hours do you work?: '))
pph=float(input('how much money do you make in a hour?: '))

print ('you make',payment_per_day(h,pph),"doller per day")
print('you make',payment_per_week(h,pph),'doller per week')
print('you make',payment_per_month(h,pph),'doller per month')
if payment_per_month(h,pph)==0:
    print()
    print("you can't make any money because it's illegal to work")
    print("more than 8 hours!")