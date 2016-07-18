from Math.MathEquationHandler import MathEquationHandler
from Math.Vector import Vector

class EquationVectorHandler:
    def __init__(self, mathConfig):
        self.equationXString = mathConfig.getData('equation_x')
        self.equationYString = mathConfig.getData('equation_y')
        self.equationZString = mathConfig.getData('equation_z')
        
        self.precision = mathConfig.getData('precision')
        
        self.equationX = MathEquationHandler(self.equationXString, self.precision)
        self.equationY = MathEquationHandler(self.equationYString, self.precision)
        self.equationZ = MathEquationHandler(self.equationZString, self.precision)
    
    def printEquations(self):
        self.equationX.printEquation("Equation X: ")
        self.equationY.printEquation("Equation Y: ")
        self.equationZ.printEquation("Equation Z: ")

    def printDerivEquations(self):
        self.equationX.printDerivEquation("Derivative Equation X: ")
        self.equationY.printDerivEquation("DerivativeEquation Y: ")
        self.equationZ.printDerivEquation("DerivativeEquation Z: ")
    
    def returnVector(self, t):
        x = self.equationX.getValue(t)
        y = self.equationY.getValue(t)
        z = self.equationZ.getValue(t)
        positionVector = Vector(x, y, z)
        
        return positionVector
    
    def returnDerivVector(self, t):
        x = self.equationX.getDerivValue(t)
        y = self.equationY.getDerivValue(t)
        z = self.equationZ.getDerivValue(t)
        velocityVector = Vector(x, y, z)
        
        return velocityVector