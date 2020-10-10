#!/usr/bin/env python3.8

from backend.lexer import operand_codes, lexer, constants
import math
from backend.stack import stack
import functools
import operator
import re

function_map_ = {
    operand_codes.SIN.value: lambda a : math.sin(a),
    operand_codes.COS.value: lambda a: math.cos(a),
    operand_codes.TAN.value: lambda a: math.tan(a),
    operand_codes.ASIN.value: lambda a: math.asin(a),
    operand_codes.ACOS.value: lambda a: math.acos(a),
    operand_codes.ATAN.value: lambda a: math.atan(a),
    operand_codes.SINH.value: lambda a: math.sinh(a),
    operand_codes.COSH.value: lambda a: math.cosh(a),
    operand_codes.TANH.value: lambda a: math.tanh(a),
    operand_codes.EXP.value: lambda a: math.exp(a),
    operand_codes.LOG.value: lambda a: math.log10(a),
    operand_codes.LN.value: lambda a: math.log(a),
    operand_codes.FLOOR.value: lambda a: math.floor(a),
    operand_codes.SQRT.value: lambda a: math.sqrt(a),
    operand_codes.POW.value: lambda a, b: math.pow(a, b),
    operand_codes.ADD.value: lambda a, b: a + b,
    operand_codes.SUB.value: lambda a, b: a - b,
    operand_codes.MUL.value: lambda a, b: a * b,
    operand_codes.DIV.value: lambda a, b: a / b,
    operand_codes.MOD.value: lambda a, b: a % b
# operand_codes.LIST_ADD.value: lambda container: functools.reduce(operator.add, container)
    # operand_codes.ADD.value: lambda container: functools.reduce(operator.add, container),
    # operand_codes.SUB.value: lambda container: functools.reduce(operator.sub, container),
    # operand_codes.MUL.value: lambda container: functools.reduce(operator.mul, container),
    # operand_codes.DIV.value: lambda container: functools.reduce(operator.truediv, container),
    # operand_codes.MOD.value: lambda container: functools.reduce(operator.mod, container)
}

constant_map_ = {
  constants._PI.value: math.pi,
  constants._G.value: 6.67430E-11,
  constants._g.value: 9.81,
  constants._e.value: math.e
}

lexi = lexer()
simple_operands_ = list(lexi.operand_map.values())
print()

class math_helper():
    def __init__(self):
        self.curly_brace_re_ = r"\{(.*?)\}"
        self.lexar = lexer()
        self.simple_operands_ = list(lexar.operand_map.values())

    def range_(self, range_expression: str) -> list:
      """
      We get a list of values from range n to k.
      This needs to be treated as it's own object, like a number and can be pushed to the stack.
      Operations can be applied to containers.

      Example of regular range notation which gives all the values from 1 to 10: 1-10
      Example of bash expansion notation which gives all the values from 1 to 10: {1..10}
      """
      if(('-' in range_expression and range_expression[0] != '-')):
        split = range_expression.split('-')
        range_tuple_ = (int(split[0]), int(split[1])+1)

      else:
        match = re.findall(self.curly_brace_re_, range_expression)[0].split('..')
        range_tuple_ = (int(match[0]), int(match[1])+1)
      
      return [element for element in range(range_tuple_[0], range_tuple_[1])]

    def percent(self, per: str) -> float:
        """
        Give the percent value of a number if in the format of <number>%.
        The number can either be an integer or float.
        """

        try: return float(s.split('%')[0])*0.01
        except ValueError: return None

    def traditional_to_rpn(self, expression: str) -> str:
        """
        Convert regular notation into Reverse Polish Notation.
        Example input: 1 + 2 / 3
        Example output: 1 2 + /
        """
        operands = list(self.lexar.operand_map.keys())
        # s = "x ^ 2"
        rev = expression[::-1].split()
        ops = []
        for index, element in enumerate(rev):
          # if the element is an operand
          if(element in operands): 
            ops.append(element)
            rev.pop(index)
          # if element is a letter, then it has to be a variable
          elif(element == '^'):
            # x ^ 2
            rev[index], rev[index-1] = rev[index-1], rev[index]
            # ^ 2 x
            rev[index-1] = "POW"
            # ?x 2 POW
            if(rev[index+1].isalpha()):
              rev[index+1] = "?{}".format(rev[index+1])
        return ' '.join((rev[::-1] + ops))

def math_function(container: list, operand_code: int) -> float:
    if(container is None): return

    # if it is any of the trig functions
    try:
      if(len(container) == 1):
        return function_map_[operand_code](*container)
      elif(len(container) == 2 or operand_code == operand_codes.POW.value and operand_code in simple_operands_):
        try:
          return function_map_[operand_code](container[1], container[0])
        except Exception as error:
          print("got a math error ey there bud!: {}".format(error))
          return 0
      else:
        return function_map_[operand_code](container)
    except KeyError:
        print("unsupported operand code: {}".format(operand_code))

