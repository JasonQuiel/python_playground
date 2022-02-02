#Hourly wage calculator with the ability to calculate over time, but within a function that is being called instead.


def hours_cal(hrw, wge):

    if hrw <= 40:
        print("Regular hours")
        reg_pay = hrw * wge
        print("Your pay is:" , reg_pay)
    if hrw > 40:
        print("Overtime")
        reg_pay = hrw * wge
        ot_pay = (hrw - 40) * (wge * 0.5) 
        print("Your pay is:", reg_pay + ot_pay)

# Python starts here because the function has yet to be called.

hours_worked = input("How many hours: ")
wage_rate = input("Your current wage: ")

try:
    hrw = float(hours_worked)
    wge = float(wage_rate)

except:
    print("This is not a valid input") 
    quit()

hours_cal(hrw, wge)
