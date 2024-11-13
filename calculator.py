"""3. Create a file, calculator.py, that defines a simple calculator function:
○ Define four functions for addition, subtraction, multiplication, and division.
○ Allow the user to select an operation, input two numbers, and display the result.
○ Make sure to handle invalid inputs gracefully (e.g., division by zero).
 """
#Creating functions for addition, subtraction, multiplication and division
def add(a:int,b:int)->int:
    return a+b
def sub(a:int,b:int)->int:
    return a-b
def mul(a:int,b:int)->int:
    return a*b
def div(a:int,b:int)->int:
    try:  #defining try block to handle exceptions
        return a/b
    except ZeroDivisionError: #Handling division by zero
        return 'Division by zero is not possible'

#Calculator function to allow user to select operation, input two numbers and display the result
def calculator():
    print("Choose an operations:")
    print("1.Addition \n2.Subtraction \n3.Multiplication \n4.Division")
    choice=input("Your Choice")
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    match choice:
        case '1':
            print(f"The sum of {a} and {b} is {add(a,b)}")
        case '2':
            print(f"The difference of {a} and {b} is {sub(a,b)}")
        case '3':
            print(f"The product of {a} and {b} is {mul(a,b)}")
        case '4':
            print(f"The division of {a} and {b} is {div(a,b)}")
        case '5':
            print("Invalid choice")
            
calculator() #Calling calculator function