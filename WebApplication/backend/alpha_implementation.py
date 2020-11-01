#!/usr/bin/env python3.8

import math

def pop() -> float:
    op = stack[-1]
    stack.pop()
    return op
def peek() -> float:
    return stack[-1]

def push(element: int):
    stack.append(element)

def print_stack():
    for element in reversed(stack):
      print(element)

assignment_ = "a 5 ="
stack = []

variable_table_ = {}
split_string = assignment_.split()

# variable assignment
if(split_string[0].isalpha() and "=" in assignment_): 
  if(len(split_string[0]) == 1 and split_string[1].isdigit()):
    variable_table_[split_string[0]] = split_string[1]

look_up_ = "a ?"
variable_ = look_up_.split()[0]
if(variable_ in variable_table_.keys()): 
    print(variable_table_[variable_])

pushing_ = "3 2 POW"

for element in pushing_.split():
  if(element.isdigit()):
    push(float(element))
  elif(len(element) == 1):
    if(element == "*"):
      push(pop() * pop())
    elif(element == "+"):
      push(pop() + pop())
    elif(element == "-"):
      op2 = pop()
      push(pop() - op2)
    elif(element == "%"):
      op2 = pop()
      push(pop() % op2)
    elif(element == "/"):
      op2 = pop()
      if(op2 == 0): 
        print("cannot divide by zero, cowardly refusing")
        break
      push(pop() / op2)
  elif(len(element) > 2 and len(element) <= 4):
    if(element == "SIN"):
      push(math.sin(pop()))
    elif(element == "COS"):
      push(math.cos(pop()))
    elif(element == "TAN"):
      push(math.tan(pop()))
    elif(element == "POW"):
      # example: 3 2 POW
      # 3**2 == 9
      op2 = pop()
      push(pop()**op2)
    

print_stack()
