#!/usr/bin/env python
# coding: utf-8

# # Python part II
# ## Date: 20th Feb. 2024
# ## Submitted to: Melinda Varo
# ## Submitted by: Bikram Nepal

# ##  1.	Write a lambda expression to get the product of two numbers.
# 
# ### Run test for expression(5,6) Output: 30
# 

# In[3]:


multiply = lambda x, y: x * y
result = multiply(5, 6)
print(result)


# ## 2.	Write a function to get the area of a circle from the radius.
# ### Hint: remember to import the right modul for being able to calculte the area of the circle.
# ### Run test for function(10) Output: 314.1592653589793
# 

# In[8]:


import math

def calculate_circle_area(radius):
    area = math.pi * radius ** 2
    return area

# Test the function
radius = 10
result = calculate_circle_area(radius)
print(result)


# ## 3.	Build a simple calculator which can: add, subtract, multiply, divide.
# ### Hint: solve by writing a function that takes as argument two numbers and the operation and returns the desired output.
# ### Run test for function(2,5,’d’)
# ### Output: 0.4
# 

# In[5]:


def simple_calculator(num1, num2, operation):
    if operation == 'a':
        result = num1 + num2
    elif operation == 's':
        result = num1 - num2
    elif operation == 'm':
        result = num1 * num2
    elif operation == 'd':
        # Check if the divisor is not zero to avoid division by zero
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error: Division by zero is not allowed"
    else:
        return "Invalid operation"
    
    return result

# Test the function
num1 = 2
num2 = 5
operation = 'd'
result = simple_calculator(num1, num2, operation)
print(result)


# ## 4.	Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area.
# ### Run test for	r = Rectangle(5,10)
# ### r.area()
# ### Output: 50

# In[6]:


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

# Test the class
r = Rectangle(5, 10)
result = r.area()
print(result)


# ## 5.	Define a class named Shape and its subclass Square.
# ## Shape objects can be consrtucted by name and length has an area function wich return 0
# ## Square subclass has an init function which take a length and name as argument and has an area method and a describe method what prints the name of the Shape.
# ### Print the area from Square class. Run test for:	s = Square('square',5)
# ### print(s.area()) print(s.describe())
# ### Output:	The area is:
# ### 25
# ### This is a: square

# In[7]:


class Shape:
    def __init__(self, name, length):
        self.name = name
        self.length = length

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, name, length):
        super().__init__(name, length)

    def area(self):
        return self.length ** 2

    def describe(self):
        return f"This is a: {self.name}"

# Test the classes
s = Square('square', 5)
area_result = s.area()
describe_result = s.describe()

print("The area is:")
print(area_result)
print(describe_result)

