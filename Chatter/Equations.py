#!/usr/bin/env python3.8

import random

class Generator():
    def __init__(self):
        pass

    def equation(self) -> str:
        operators = ['+', '-', '/', '*']
        operator = random.choice(operators)
        a = random.randint(0, 10)
        b = random.randint(0 if(a > 0) else 1, 10)
        if(operator == '/'):
            b = a * random.randint(1, 10)
            a, b = max(a, b), min(a, b)

        return f'{a} {operator} {b}'

    def check(self, answer: int, expression: str) -> bool:
        return (answer == eval(expression))
