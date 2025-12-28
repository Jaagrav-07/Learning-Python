#Write a program that swaps the values of a and b. You are not allowed to use a third variable. You are not allowed to perform arithmetic on a and b

a = 5
b = 10

print(f"Before swap: a = {a}, b = {b}")

a, b = b, a # Swapping values using tuple unpacking

print(f"After swap: a = {a}, b = {b}")