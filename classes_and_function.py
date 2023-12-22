#!/usr/bin/env python
# coding: utf-8

# # CLASSES AND FUNCTION IN PYTHON

# In[1]:


#  1.Definition and Object Creation Create a Python class called "Student" that has the following attributes: name, age, and grade. Define an initialization method to initialize these attributes when an object of tClass he class is created. Create an instance of the class and set the attributes. Finally, print the attributes of the student object.
   
class Student:
   def __init__(self,name,age,grade):
       self.name = name
       self.age = age 
       self.grade = grade

student_1 = Student('Arun','12',5)
student_2 = Student('Kumar','15',7)
student_3 = Student('Nura','25',9)

print(student_1.grade)
print(student_3.name)
print(student_2.age)


# In[5]:


# 2.Methods in a Class Extend the "Student" class from the previous question. Add a method called "is_passing" that returns True if the student's grade is greater than or equal to 50 and False otherwise. Create an instance of the class and use this method to check if the student is passing. Display the result.

class Student:
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade
        
    def is_passing(self):
        return self.grade >50
    

Arun = Student('Arun' ,70)

result=Arun.is_passing()

print(f"Is {Arun.name} passed? {result}")


# In[6]:


# 3.Inheritance and Subclasses Create a new class called "HighSchoolStudent" that inherits from the "Student" class. Add an additional attribute called school_name to the "HighSchoolStudent" class. Create an instance of the "HighSchoolStudent" class and set both the attributes, including the inherited attributes from the "Student" class. Print all the attributes of the high school student.

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

class HighSchoolStudent(Student):
    def __init__(self, name, grade, school_name):
        super().__init__(name, grade)
        self.school_name = school_name

    def __str__(self):
        return f"High School Student: {self.name}, Grade: {self.grade}, School: {self.school_name}"

# Create an instance of the HighSchoolStudent class
student = HighSchoolStudent("Arun Kumar", "12", "Government Higher Secondary School")

# Print all the attributes of the high school student
print(student)


# # FUNCTION IN PYTHON

# In[2]:


# 4.Function with Parameters Write a Python function called "calculate_rectangle_area" that takes two parameters, length and width, and returns the area of a rectangle. Call the function with different sets of values and display the results.

def calculate_rectangle_area(length, width):
   area = length * width
   return area


print(calculate_rectangle_area(10, 20))

print(calculate_rectangle_area(5, 10))

print(calculate_rectangle_area(3, 10))


# In[7]:


# 5.Function with Default Parameters Create a Python function called "greet" that takes a name as a parameter and a greeting message as an optional parameter with a default value of "Hello". The function should return a formatted greeting message. Test the function by calling it with and without the optional parameter and display the results.

def greet(name, greeting_message="Hello"):
       return f"{greeting_message}, {name}!"

# Testing the function by calling it with and without the optional parameter
print(greet("Arun Kumar"))
print(greet("Arun Kumar", "Good Morning"))


# In[6]:


# 6.Function with Variable Number of Arguments Write a Python function called "calculate_average" that takes a variable number of arguments and calculates the average of those numbers. Use this function to find the average of 5, 10, 15, and 20, and display the result.

def calculate_average(*args):
    total = sum(args)
    average = total / len(args)
    return average

result = calculate_average(5, 10, 15, 20)
print("The average is:", result)


# In[ ]:





# In[ ]:




