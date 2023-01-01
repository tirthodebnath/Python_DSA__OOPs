#Converting year to in days
def calc_age(age):
    if age < 0:
        print("Invalid age")
    else:    
        days = age * 365
        return days
age=int(input("Enter your age in years: "))    
print(calc_age(age))