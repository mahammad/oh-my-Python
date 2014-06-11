#! /usr/bin/python
# -*- coding: utf-8 -*-

#calculator process menu
print ("""Wellcome simple calculator...
1: ADDITION
2: SUBTRACTION
3: MULTIPLICATION
4: DIVISION
""")
#CHOICE control that user when do not enter integer valuge
try:
	CHOICE = int(raw_input("Enter CHOICE: "))
	number1 = int(raw_input("Enter 1. number:"))
	number2 = int(raw_input("Enter 2. number:"))
	
	if CHOICE == 1:
		print number1 + number2
	elif CHOICE ==2:
		print number1 - number2
	elif CHOICE == 3:
		print number1 * number2
	elif CHOICE == 4:
		print number1 / number2
except ValueError, e:
	print "Please enter integer valuge!"