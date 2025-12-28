#Demonstrate how to convert from one number type to another

# converted to int

print (int(3.14))  #float to int
a = int('845')  #numeric string to int
b = int ('955')  #numeric string to int
c = a+b

print(c)
print(int('1011', 2))  #binary to decimal int
print(int('314', 8))   #octal to decimal int
print(int('21', 16))   #hex to decimal int



# converted to float

print(float(314)) #int to float
a = float('845') #numeric string to float
b = float ('955') #numeric string to float
c = a+b

print(c)



# converted to complex

print(complex(314)) #int to complex
a = complex('845') #numeric string to complex
b = complex ('955') #numeric string to complex
c = a+b

print(c)



# converted to bool

print(int(True))
print(int(False))
print(bool(35))
print(bool(45))