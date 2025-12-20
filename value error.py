 
try :
  num = int(input("enter your number :"))
except ValueError as ex:
  print("Exception:",ex)

  print("I am outside the try block")