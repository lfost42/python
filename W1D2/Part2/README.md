# Day2Part2

OO & Functional Programming

## Assignment

1. You are asked to create a Car class and then three Car objects with certain instance attributes. However, the instance attribute names and values are provided to you as a dictionary of key-value pairs where the key is the attribute name and the corresponding value is the value of the attribute. For example
car1_attr = {"year": 1990, "make":"Ford", "model":"Bronco"}

car2_attr = {"year": 2010, "make":"Chevy", "model":"Blazer", "drive":"RWD"}

car3_attr = {"year": 2020, "make":"Tesla", "model":"Model3", "drive":"AWD", "range": 300}

Create a generic dunder init method that will accept the dictionaries above and create the instance attributes. Your solution must be able to accomodate any future attributes which can be different than the ones above.

Print out each Car objects attributes and the values after creation.

(Hint: You will need the setattr and getattr functions)


2. Create an Employee class which keeps track of the number of instances of employees that have been created.
e1 = Employee() Employee.count ->1
e2 = Employee() Employee.count ->2


3. Create an employee class which takes in the first and last name. Create a method that returns the full name which is the first plus last name seperated by a space. Also return the email address 

firstName = 'John'
lastName = 'Doe'

full name ---> 'John Doe'
email -----> 'john.doe@acme.com'

Notice that the email is all lowercase. Your full name must also have the first letters of the first and last name capitalized whatever the capitalization of the input first and last names. Only the first letters must be capitalized.

firstName --> 'sarah'
lastname --> 'LEE'
full name ---> 'Sarah Lee'
email ---> 'sarah.lee@acme.com'


4. Create a class named myString inheriting from the str class.
Add a append() method which takes a string and appends it at the end.
