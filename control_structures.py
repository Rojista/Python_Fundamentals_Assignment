""" 2.In control_structures.py, write a function classify_number:
○ Prompt the user to enter a number.
○ Use if statements to classify the number as positive, negative, or zero.
○ Use a while loop to allow the user to classify additional numbers until they type
"exit."
 """
def classify_number(): #function to classify number as positive, negative or zero
    while True: #while loop to allow user to classify additional numbers until they type 'exit'
        number=input('Enter a number: ')
        number=number.lower() #converting input to lower case
        if number=='exit': #Break Condition
            break
        number=int(number)
        if number>0:
            print('The number is positive')
        elif number<0:
            print('The number is negative')
        else:
            print('The number is zero')

classify_number() #calling the function