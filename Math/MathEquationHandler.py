from sympy import *
from sympy.abc import t
from sympy.parsing.sympy_parser import parse_expr


class MathEquationHandler:
    def __init__(self, equation, precision):
        self.equation = parse_expr(equation)
        self.derivEquation = diff(equation)
        self.precision = precision
    
    def getValue(self, time):
        subsEquation = self.equation.subs(t, time)
        return subsEquation.evalf(self.precision)
    
    def getDerivValue(self, time):
        subsEquation = self.derivEquation.subs(t, time)
        return subsEquation.evalf(self.precision)
    
    def printEquation(self, prefix):
        printString = prefix + str(self.equation)
        print printString
    
    def printDerivEquation(self, prefix):
        printString = prefix + str(self.derivEquation)
        print printString