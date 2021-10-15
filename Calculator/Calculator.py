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

MISSING_OPERAND: str = "Missing or bad operand"
DIV_BY_ZERO: str = "Division with 0"
MISSING_OPERATOR: str = "Missing operator or parenthesis"
OP_NOT_FOUND: str = "Operator not found"
OPERATORS: str = "+-*/^"


def infix_to_postfix(infix):    #TODO
    postfix = []
    stack = []
    for char in infix:
        if isinstance(char, int):
            postfix.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1] != '(' and get_precedence(char) <= get_precedence(stack[-1]):
                postfix.append(stack.pop())
            stack.append(char)
    while stack:
        postfix.append(stack.pop())
    return postfix


#

# -----  Evaluate RPN expression -------------------
def eval_postfix(postfix_tokens):   #TODO
    postfix_stack = []
    for _ in postfix_tokens:
        if not isinstance(_, int):
            d1 = postfix_stack.pop()
            d2 = postfix_stack.pop()
            postfix_stack.append(apply_operator(_, d1, d2))
        else:
            postfix_stack.append(_)
    postfix_evaluated = sum(postfix_stack)
    return postfix_evaluated


# Method used in REPL
def eval_expr(expr: str):
    if len(expr) == 0:
        return nan
    infix_tokens = tokenize(expr)   #TODO
    infix = infix_str_to_int(infix_tokens)  #TODO
    postfix_tokens = infix_to_postfix(infix)    #TODO
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

# ---------- Tokenize -----------------------
def tokenize(expr: str):    #TODO
    return list(expr)


def infix_str_to_int(infix_prereference):   #TODO
    infix_separated = separate_char(infix_prereference)
    combine_int(infix_separated)
    return infix_separated


def combine_int(infix_combined):    #TODO
    for num in range(0, len(infix_combined)):
        str_list = ['']
        if isinstance(infix_combined[num], list):
            for str_to_int in range(0, len(infix_combined[num])):
                str_list[0] += infix_combined[num][str_to_int]
            infix_combined[num] = int(str_list[0])


def separate_char(infix_tokens):    #TODO
    infix_separated = []
    infix_cut_start = 0
    infix_cut_end = 0
    infix_tokens.append('=')
    for char in infix_tokens:
        if char in '+-*/^=()':
            infix_separated.append(infix_tokens[infix_cut_start:infix_cut_end])
            if not infix_separated[-1]:
                infix_separated.pop()
            infix_separated.append(char)
            infix_cut_start = infix_cut_end + 1
        infix_cut_end += 1
    infix_separated.pop()
    return infix_separated



