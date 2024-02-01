number1 = 0
number2 = 0
try:
    number1 = int(input("Enter a number"))
    number2 = int(input("Enter a number"))
except ValueError:
     print("an integer wasn't given")  
      
else:
    print("No value error detected")
finally:
    print("Values taken care of")

try:
    answer =(number1/number2)
    print("answer equals")

    
except ZeroDivisionError:
   print("Cannot divide by zero")

   else:print("number were divdie")
    pass 