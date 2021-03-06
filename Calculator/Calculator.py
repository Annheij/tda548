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
    postfix_operand = []
    postfix = []
    token_place = 0
    for token in infix:
        if token in ('+-*/^'):
            pass
    return postfix  # TODO


# -----  Evaluate RPN expression -------------------
def eval_postfix(postfix_tokens):
    return 0  # TODO


# Method used in REPL
def eval_expr(expr: str):
    if len(expr) == 0:
        return nan
    infix = tokenize(expr)
    postfix_tokens = infix_to_postfix(infix)
    return eval_postfix(postfix_tokens)


def apply_operator(op: str, d1: float, d2: float):
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
        "+": 2,
        "-": 2,
        "*": 3,
        "/": 3,
        "^": 4
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
    infix = []
    for _ in expr:
        infix_prereference.append(_)
    infix_place = 0
    infix_place_last = 0
    infix_prereference.append('=')
    for _ in infix_prereference:
        if _ in '+-*/^=':
            infix.append(infix_prereference[infix_place_last:infix_place])
            infix.append(_)
            infix_place_last = infix_place + 1
        infix_place += 1
    del infix[-1]
    return infix   # TODO
# TODO Possibly more methods
