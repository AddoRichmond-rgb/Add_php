
day = "morning"

if day == "morning":
    print("Good morning")
elif day == "afternoon":
    print("Good Afternoon")
else:
    print = ("good evening")


#EXample2
weather = "Sunny"
if weather == "Sunny":
    print("Wear something simple")
else:
    print("Wear anything you are comfortable in")
    
#Grading system
#First_class = 80 - 100
#Second_class_upper = 70 - 79.999
#Second_class_lower = 60 - 69.999
#Third_class = 50 - 59.999
#Fail = 0 - 49.999


CWA = 80
if CWA >= 80:
    print("First class")
elif CWA >=70:
    print("Second class upper")
elif CWA >= 60:
    print("Second class lower")
elif CWA >= 50:
    print("Pass")
else:
    print("Fail")

#exercise
price = float(input("Enter the price of the item:, "))
discounted_price = 0.0
if price >=50000:
    discounted_price = price * 0.25
elif price >= 35000:
    discounted_price = price * 0.15
elif price >= 20000:
    discounted_price = price * 0.10
else:
    discounted_price = price * 0.05 

final_price = price - discounted_price
print(f"The final price after discount is: GH¢{final_price: .2f}")


#Example
day = int(input("Enter the day of the week"))
match day:
    case 1:
          print("Monday")
    case 2:
          print("Tuesday")
    case 3:
          print("Wednesday")
    case 4:
          print("Thursday")
    case 5:
          print("Friday")
    case 6:
          print("saturday")
    case 7:
          print("Sunday")
    case _:
          print("Invalid Day Number")


          


#Example
num = int(input("Enter your number"))
match num:

#Asssignment 1 py-club
Employees_salary = float(input("Enter your salary: GHC."))
tax = 0.0
if Employees_salary >= 5000:
    tax = Employees_salary * 0.15
elif Employees_salary >= 3500:
    tax = Employees_salary * 0.11
elif Employees_salary >= 2000 <= 3500:
    tax = Employees_salary * 0.08
else:
    tax = 0.0
final_takehome = Employees_salary - tax
print(f"Your final takehome is: GH¢{final_takehome: .2f}")








