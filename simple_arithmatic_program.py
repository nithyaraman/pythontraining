#!/bin/bash
########################################################################
#@file           : simple_arithmetic_operation.py
#@Brief          :write a program for simple arithmetic operations like
#                  add,subtraction,multiplication,division
#@Authour        :Nithyaraman
#########################################################################    
print "Basic arithmatic operation between two numbers"
n1=float(raw_input("enter first number="))
n2=float(raw_input("enter second number="))
print "addition of this two number =%r"%(n1+n2)
print"subtraction of this two numbers=",(n1-n2)
print "multiplication of this two number=%d"%(n1*n2)
print "division of this two number=",(float(n1/n2))

