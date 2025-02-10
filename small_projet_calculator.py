First_number = int(input("Enter your frist digit:"))
operator = input("enter operator (+,-,*,/,%):")
second_number = int(input("Enter your secound digit digit:"))

if operator=="+":
    print(First_number+second_number)
elif operator=="-":
    print(First_number-second_number)
elif operator=="*":
    print(First_number*second_number)
elif operator=="/":
    print(First_number/second_number)
elif operator=="%":
    print(First_number%second_number)
else:
    print("invaild operation ")
except ValueError:
    print("Invalid input! Please enter numeric values.")
except ZeroDivisionError:
    print("Error! Division by zero is not allowed.")
print("Thanks you for your visit")
