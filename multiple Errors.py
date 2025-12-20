try:
    num1 = int(input("ENTER A NUMBER"))
    num2 = int(input("ENTER A NUMBER"))
    result = num1/num2
    print("Result is : ",result)
except ZeroDivisionError:
    print("Division by zero is not allowed")
except ValueError:
    print("Please enter numerical value")
except NameError as ex:
    print("The exeption is",ex)

except:
    print("Some error occurred")
finally:
    print("I WILL EXECUTE NO MATTER WHAT HAPPENS")