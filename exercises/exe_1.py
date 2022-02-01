# Hourly wage calculator with the ability to calculate over time.


# Program inputs - No try or excepts 
hours_worked = input("How many hours: ")
wage_rate = input("Your current wage: ")

# Conversions of strings to floats
wge = float(wage_rate)
hrw = float(hours_worked)


reg_pay = hrw * wge
ot_pay = (hrw - 40) * (wge * 0.5) 

if hrw <= 40:
   print("Regular hours")
   print("Your pay is:" , reg_pay)
elif hrw > 40:
   print("Overtime")
   print("Your pay is:", reg_pay + ot_pay)









