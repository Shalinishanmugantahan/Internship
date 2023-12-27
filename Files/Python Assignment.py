#!/usr/bin/env python
# coding: utf-8

# In[2]:


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)


number = int(input("Enter a number: "))



if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    result = factorial(number)
    print(f"The factorial of {number} is: {result}")


# In[3]:


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


number = int(input("Enter a number: "))


if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is a composite number.")


# In[4]:


def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print(f"{input_string} is a palindrome.")
else:
    print(f"{input_string} is not a palindrome.")


# In[5]:


def find_hypotenuse(side1, side2):
    hypotenuse = (side1**2 + side2**2)**0.5
    return hypotenuse
side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
if side1 >= 0 and side2 >= 0:
    hypotenuse = find_hypotenuse(side1, side2)
    print(f"The length of the hypotenuse is: {hypotenuse:.2f}")
else:
    print("Invalid input. Side lengths should be non-negative.")


# In[8]:


def character_frequency(input_string):
    frequency_dict = {}
    for char in input_string:
        if char != ' ':
            frequency_dict[char] = frequency_dict.get(char, 0) + 1
    for char, count in frequency_dict.items():
        print(f"Character '{char}' occurs {count} times.")
input_string = input("Enter a string: ")

character_frequency(input_string)


# In[ ]:




