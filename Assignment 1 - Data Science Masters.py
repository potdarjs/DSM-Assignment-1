# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Assignment 1 - Data Science Masters

# 1. Install Jupyter notebook and run the first program and share the screenshot of the output.

# Identify Odd or Even 
x = 3

if x%2 == 0:
    print("Even")
else:
    print("Odd")  
    print ("Finish")

# Identify Positive , Negative or Zero
x = 0

if x > 0:
    print ("Positive")
elif x < 0:
    print ("negative")
else:
    print("Zero")


# Print elements of List
a = [1,2,3,4,5]
i = 0
while i < len(a):
    print (a[i])
    i = i + 1

# 2. Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, 
# between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.

l=[]
for i in range(2000, 3200):
    if (i % 7 == 0) and (i % 5 != 0):
        l.append(str(i))
print (','.join(l))
    

# 3. Write a Python program to accept the user's first and last name and then getting them printed in the the reverse order 
#with a space between first name and last name.

fname = input("Input your First Name : ")
lname = input("Input your Last Name : ")
print (fname[::-1] + " " + lname[::-1])

fname = input("Input your First Name : ")
lname = input("Input your Last Name : ")
print (lname + " " + fname)


# 4. Write a Python program to find the volume of a sphere with diameter 12 cm. Formula: V=4/3 π r 3

print ("Volume of Shpere with dia 12 cm is " + str ('%.2f' % ((4/3)* (22/7)* (12/2)**3)) + " CM3")
