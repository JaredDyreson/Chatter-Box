#!/usr/bin/env python3.8

import math
from backend.stack import stack
from backend.lexer import lexer, operand_codes
import backend.maths as maths
from signal import signal, SIGINT
from sys import exit


"""
Variables available for all processes in program
"""

stack_ = stack()
lex = lexer()

variable_map_ = {
    "variable": 10.0
}

def sigint_handler(signal_received, frame):
    exit(0)

def assign_value_(string: str):
  variable_ = string[1:]
  if(variable_.strip() in lex.keywords):
    print("cannot use {} as a variable name!".format(variable_))
    stack_.clear_contents()
  else:
    print("assigning {} with value of {}".format(string[1:], stack_.peek()))
    variable_map_[variable_] = stack_.peek()

def retrieve_value_(string: str):
  variable_ = string[1:]
  try:
      value_retrieved_ = variable_map_[variable_]
      stack_.push(value_retrieved_)
  except KeyError as error:
      print("cannot retrieve value of {}, it is not in the table".format(variable_))
      # print("full error log: {}")


def get_constant_(string: str):
    look_up_ = -1
    for i, element in enumerate(lex.constant_names_):
      if(element == string): 
        look_up_ = i
        break
    try:
      stack_.push(maths.constant_map_[look_up_])
    except KeyError:
      print("could not find constant: {}".format(string))
def math_operation_(string: str):
  try:
    # this is only for list operations
    multi_argument_code = lex.operand_map[string]
    contents_ = stack_.pop_n(2)
    try:
      stack_.push(maths.math_function(contents_, multi_argument_code))
    except TypeError as error:
      print("error value of: {}".format(error))
      print("invalid syntax: {}".format(string))
  except KeyError:
    value_ = [stack_.pop()]
    if(operand_codes.POW.value == lex.tokenize(string)):
      value_.append(stack_.pop())
    stack_.clear_contents()
    try:
      stack_.push(float(maths.math_function(value_, lex.tokenize(string))))
    except Exception as error:
      print("oops, got a math error ey there bud!: {}".format(error))


def rpn_calculator(expression: str) -> None:
  for index, token in enumerate(expression.split()):
    try:
      operand_code = lex.tokenize(token)
      if(operand_code == operand_codes.GARBAGE.value):
        print("got garbage with operand: {}".format(token))
      elif(operand_code == operand_codes.CONSTANT.value):
        get_constant_(token)

      elif(operand_code == operand_codes.NUMBER.value):
        stack_.push(float(token))

      elif(operand_code == operand_codes.ASSIGN.value):
        assign_value_(token)

      elif(operand_code == operand_codes.RETRIEVE.value):
        retrieve_value_(token)

      elif(operand_code == operand_codes.COMMENT.value):
          return operand_codes.COMMENT.value

      else:
        math_operation_(token)
    except Exception as error:
      print("Malformed expression: \"{}\" at token \'{}\' (index: {})".format(expression, token, index))
      print("exception: {}".format(error))
      stack_.clear_contents()
      break

def unit_test_():
  expression = "10 SIN\n18 9 *"
  for element in expression.split('\n'):
    print(">>> {}".format(element))
    rpn_calculator(element)

    if(not stack_.is_empty()):
      try: print("\t{0:.15f}".format(stack_.peek()))
      except IndexError: print("\tstack is empty")
    stack_.clear_contents()

def read_from_file(path: str) -> None:
    with open(path) as fd: content = fd.readlines()
    for line in content:
      line = line.replace('\n', '')
      if(not line): pass
      code_ = rpn_calculator(line)
      if(not stack_.is_empty() and code_ != operand_codes.COMMENT.value and len(line) != 0):
        print(">>> {}".format(line))
        try: print("\t{0:.15f}".format(stack_.peek()))
        except IndexError: print("stack is empty")
    stack_.clear_contents()

# read_from_file("./formulas/pokeball_shake")
# print("="*80)
# read_from_file("./formulas/pythagorean")
# print("="*80)
# read_from_file("./formulas/some_trig")
# signal(SIGINT, sigint_handler)

# while(True):
  # exp = input(">>> ")
  # rpn_calculator(exp)
  # if(not stack_.is_empty()):
    # try: print("\t{0:.15f}".format(stack_.peek()))
    # except IndexError: print("\tstack is empty")
  # stack_.clear_contents()
