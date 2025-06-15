while True:
    print("The commands for the operations are: add, subtract, multiply, and divide")
    Num1=float(input("Number 1: "))
    Num2=float(input("Number 2: "))
    operation=input("Enter the operation you wish to use: ")
  
    if operation == "add":
        addition= Num1 + Num2
        print( str(Num1) + "  + " + str(Num2) + " = " + str(addition) )

    elif operation == "multiply":
        product= Num1 * Num2
        print( str(Num1) + " * " + str(Num2) + " = " + str(product) )

    elif operation == "subtract":
        difference= Num1 - Num2
        print( str(Num1)+ " - " + str(Num2) + " ="  + str(difference))

    elif operation == "divide":
        try:
            division= Num1 / Num2
            print( str(Num1) + " / " + str(Num2) + " = " +str(division))
        except ZeroDivisionError:
            print("You can't divide by zero")

    else:
        print("there is an error with your input. Please try again. ")
    
    print("Do you wish to continue? Y/N ")
    prompt=input("")
    if prompt != "Y":
        print("Exiting Calculator")    
        break

    


