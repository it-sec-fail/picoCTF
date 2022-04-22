#!/usr/bin/env python

print("The assembler code will check which number is the bigger one and print this number!")
print("This script will give you the flag :)")

number1=int(input("First number? > "))
number2=int(input("Second number? > "))

if number1 > number2:
    print("Bigger number is " + str(number1))
    result=hex(number1)
else:
    print("Bigger number is " + str(number2))
    result=hex(number2)

print("picoCTF{"+result.strip("0x")+"}")
