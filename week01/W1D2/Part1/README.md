# Day2Part1

Control Structures

## Assignment

1. Consider the following code

x = 1
y = 2
def f1(x):
    def f2(y):
        print(x + y)
    return f2 

z = f1(10)
z(90)

What will be the output?
What variables and values are present in the closure?
How can we verify this i.e where inside z function are they stored?

2. Write a function that takes 3 parameters the birth year of a man, woman and their child and calculates the ages of the father and mother when the child was born. Perform some checking to see that the birth year of the father and mother are atleast 18 years when the child was born but the age of the either parent cannot be greater than 60 when the child was born.
Ouput the appropriate message when the ages are out of these bounds.

3. Given a list ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
generate another list using list comprehension.
This new list consists of 2 element tuples with the 1st element being the length of the string and the the 2nd element the first 3 letters.
[(6, 'Mon'), (7, 'Tue') and so on...]

4. Write a decorator function that gives you the time when a function was started and when it finsihed and how much time it took to execute.
(Hint: You will need to use the datetime module )

from datetime import datetime

datetime.now() gives you the current time.

Decorate this test function

def multiply_a_lot(a_number):
    sum = 0
    for i in range(a_number):
        sum = sum + i * i
    return sum

Run the decorated multiply_a_lot function with larger and larger numbers.
What is the number when the time taken is very close to 5 seconds? 
