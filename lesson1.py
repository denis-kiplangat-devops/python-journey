"""
Variable and Datatypes
#A variable is a label pointing to a value in memory. Python is
dynamically typed, meaning you don't declare a type up front —
Python figures it out from the value you assign
"""
age = 25  #int
price = 19.99 #float
name = "Denis K" #str
is_student = True #bool
nothing = None #NoneType - represent "no value"

#Checking Variable type
print(type(age)) # type() is used to check the datatype of a variable

########### TypeCasting#######
# All the imput are of string type. Type casting convert to other datatypes . e.g int, float etc
age2 = input("Enter Your age : ")
print(type(age2))