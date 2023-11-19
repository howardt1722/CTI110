   # CTI-110

   # P3HW2 - Salary

   # Tiffany Howard

   # 11/8/2023

   #pseudocode

hours = float(input("Enter Hours:"))
hours = float(hours)
rate = float(input("Enter pay rate"))
rate = float(rate)
if (hours > 40):
    h = hours - 40
    pay = (hours * rate) + (rate / 2 * h)
else:
    pay = hours * rate
print (pay)
hrs = raw_input('Enter hours ')
h= float(hrs) #why use float?
rate = float(10.5)

if h <= 40:
    pay = h*rate
elif h > 40:
    pay = ((h-40)*rate*1.5)+rate*40   

print ("Your pay is %.2f" %pay)
