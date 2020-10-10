#!/usr/bin/env python3.8

import random

class Generator():
    def __init__(self):
        pass

    def equation(self, n=10) -> str:
        operators = ['+', '-', '/', '*']
        operator = random.choice(operators)
        a = random.randint(0, n)
        b = random.randint(0 if(a > 0) else 1, n)
        if(operator == '/'):
            b = a * random.randint(1, n)
            a, b = max(a, b), min(a, b)
        if(operator == '-'):
            a, b = max(a, b), min(a, b)

        return f'{a} {operator} {b}'

    def check(self, answer: int, expression: str) -> bool:
        return (answer == eval(expression))
