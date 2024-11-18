while True:
 print("Hi ! Welcome to the Calculator Application ! We hope you like it. 😊")
 print("Select an option ! ")
 print("1. Addition")
 print("2. Subtraction")
 print("3. Multiplication")
 print("4. Division")
 print("5. Exit")
 choice = input("Enter the number for the operation you want"
                " to perform:")
 if choice == '5':
  print("Bye Bye ! ")
  break

#this ask the user to input a number for the operation
 a = float(input("Enter a digit : "))
 b = float(input("Enter another digit : "))
 if choice == '1':
    print("The addition of",a,"and",b, "is : " ,a+b)
 elif choice == '2':
    print("The subtraction of", a, 'and', b, 'is: ', a-b)
 elif choice == '3':
    print("The multiplication of" ,a, 'and', b, 'is : ', a*b)
 elif choice == '4':
    print('The division of', a, 'and', b, 'is : ', a/b)
 else:
    print("Invalid Syntax")

input("Press enter to exit:")
