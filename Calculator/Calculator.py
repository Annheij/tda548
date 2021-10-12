# package calculator

from math import nan
from enum import Enum
from typing import List

# A calculator for rather simple arithmetic expressions.
# Your task is to implement the missing functions so the
# expressions evaluate correctly. Your program should be
# able to correctly handle precedence (including parentheses)
# and associativity - see helper functions.
# The easiest way to evaluate infix expressions is to transform
# them into postfix expressions, using a stack structure.
# For example, the expression 2*(3+4)^5 is first transformed
# to [ 3 -> 4 -> + -> 5 -> ^ -> 2 -> * ] and then evaluated
# left to right. This is known as Reverse Polish Notation,
# see: https://en.wikipedia.org/wiki/Reverse_Polish_notation
#
# NOTE:
# - You do not need to implement negative numbers
#
# To run the program, run either CalculatorREPL or CalculatorGUI

MISSING_OPERAND:  str = "Missing or bad operand"
DIV_BY_ZERO:      str = "Division with 0"
MISSING_OPERATOR: str = "Missing operator or parenthesis"
OP_NOT_FOUND:     str = "Operator not found"
OPERATORS:        str = "+-*/^"


def infix_to_postfix(infix):
    postfix = []
    stack = []
    for _ in infix:
        if isinstance(_, int):
            postfix.append(_)
        elif _ == '(':
            stack.append(_)
        elif _ == ')':
             while stack and stack[-1]!= '(':
                postfix.append(stack.pop())
             stack.pop()
        else:
                while stack and stack[-1]!='(' and get_precedence(_)<=get_precedence(stack[-1]):
                    postfix.append(stack.pop())
                stack.append(_)
    while stack:                                                   #För att tömma stacken
        postfix.append(stack.pop())
    return postfix

#

# -----  Evaluate RPN expression -------------------
def eval_postfix(postfix_tokens):
    postfix_stack = []
    for _ in range(len(postfix_tokens)):
        if not isinstance(postfix_tokens[_], int):
            d1 = postfix_stack.pop()
            d2 = postfix_stack.pop()
            postfix_stack.append(apply_operator(postfix_tokens[_], d1, d2))
            pass
        else:
            postfix_stack.append(postfix_tokens[_])
    postfix_evaluated = sum(postfix_stack)
    return postfix_evaluated  # TODO


# Method used in REPL
def eval_expr(expr: str):
    if len(expr) == 0:
        return nan
    infix_prereference = tokenize(expr)
    infix = give_reference(infix_prereference)
    postfix_tokens = infix_to_postfix(infix)
    return eval_postfix(postfix_tokens)


def apply_operator(op: str, d1: int, d2: int):
    op_switcher = {
        "+": d1 + d2,
        "-": d2 - d1,
        "*": d1 * d2,
        "/": nan if d1 == 0 else d2 / d1,
        "^": d2 ** d1
    }

    return op_switcher.get(op, ValueError(OP_NOT_FOUND))


def get_precedence(op: str):
    op_switcher = {
        '+': 2,
        '-': 2,
        '*': 3,
        '/': 3,
        '^': 4
    }
    return op_switcher.get(op, ValueError(OP_NOT_FOUND))


class Assoc(Enum):
    LEFT = 1
    RIGHT = 2


def get_associativity(op: str):
    if op in "+-*/":
        return Assoc.LEFT
    elif op in "^":
        return Assoc.RIGHT
    else:
        return ValueError(OP_NOT_FOUND)


# ---------- Tokenize -----------------------
def tokenize(expr: str):
    infix_prereference = []
    for _ in expr:
        infix_prereference.append(_)
    return infix_prereference   # TODO

def give_reference(infix_prereference):
    infix_place = 0
    infix_place_last = 0
    infix_seperated = []
    infix_prereference.append('=')
    for _ in infix_prereference:
        if _ in '+-*/^=()':
            infix_seperated.append(infix_prereference[infix_place_last:infix_place])
            infix_seperated.append(_)
            infix_place_last = infix_place + 1
        infix_place += 1

    infix_combined = []
    for _ in range(0, len(infix_seperated)):
        if not len(infix_seperated[_]) == 0:
            infix_combined.append(infix_seperated[_])
    del infix_combined[-1]

    placeholder = []
    for num in range(0, len(infix_combined)):
        if isinstance(infix_combined[num], list):
            for str_to_int in range(0, len(infix_combined[num])):
                infix_combined[num][str_to_int] = infix_combined[num][str_to_int]
                placeholder.append(infix_combined[num][str_to_int])
            for list_to_int in range(1, len(placeholder)):
                placeholder[0] += placeholder[list_to_int]
            infix_combined[num] = int(placeholder[0])
            placeholder = []
    return infix_combined

def find_d(postfix, placement):
    while not isinstance(postfix[placement], int):
        placement -= 1
    d1 = postfix[placement]
    if not isinstance(postfix[placement-1], int):
        while not isinstance(postfix[placement-1], int):
            placement -= 1
        d2 = postfix[placement]
    else:
        d2=postfix[placement-2]
    return d1,d2

# TODO Possibly more methods
