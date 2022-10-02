from .nodes import *
from .values import Number, Variable

import math

class Interpreter:
    def visit(self, node):
        method_name = f'visit_{type(node).__name__}'
        method = getattr(self, method_name)

        return method(node)
    
    def visit_NumberNode(self, node):
        return Number(node.value)
    
    def visit_FunctionNode(self, node):
        num = math.sin(self.visit(node.input.value).value)
        return Number(num)
    
    def visit_VariableNode(self, node):
        return Variable()
    
    def visit_AddNode(self, node):
        return Number(self.visit(node.node_a).value + self.visit(node.node_b).value)
    
    def visit_SubtractNode(self, node):
        return Number(self.visit(node.node_a).value - self.visit(node.node_b).value)
    
    def visit_MultiplyNode(self, node):
        return Number(self.visit(node.node_a).value * self.visit(node.node_b).value)
    
    def visit_DivideNode(self, node):
        try:
            return Number(self.visit(node.node_a).value / self.visit(node.node_b).value)
        except:
            raise Exception("Runtime math error")
    
    def visit_PlusNode(self, node):
        return self.visit(node.node)
    
    def visit_MinusNode(self, node):
        return Number(-self.visit(node.node).value)
