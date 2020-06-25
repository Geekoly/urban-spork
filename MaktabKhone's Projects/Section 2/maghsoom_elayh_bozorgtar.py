numbers = []
counter = []


for i in range(20):
    numbers.append(input())
    
def count_divisor(a_number):
    count = 0
    a_number = int(a_number)
    for i in range(1,a_number+1):
        if a_number % i == 0:
            count += 1
    return count
            
    
for number in numbers:
    counter.append(count_divisor(number))
    
    
shomarande = 0
jaygahe_max_ha = []
for i in counter:
    if i == max(counter):
        jaygahe_max_ha.append(shomarande)
    shomarande += 1
    
    
list_akahr = []    
for i in jaygahe_max_ha:
    list_akahr.append(numbers[i])
   

print(max(list_akahr),max(counter))