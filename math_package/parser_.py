from .tokens import TokenType
from .nodes import *

class Parser:
    def __init__(self, tokens):
        self.tokens = iter(tokens)
        self.advance()


    def raise_error(self, message=""):
        raise Exception("Invalid Syntax " + message)


    def advance(self):
        try:
            self.current_token = next(self.tokens)
        except StopIteration:
            self.current_token = None
    

    def parse(self):
        if self.current_token == None:
            return None
        
        result = self.expr()

        if self.current_token != None:
            self.raise_error()
        
        return result
    

    # CREATE AN EXPRESSION
    def expr(self):
        result = self.term()

        while self.current_token != None and self.current_token.type in (TokenType.PLUS, TokenType.MINUS):
            if self.current_token.type == TokenType.PLUS:
                self.advance()
                result = AddNode(result, self.term())
            elif self.current_token.type == TokenType.MINUS:
                self.advance()
                result = SubtractNode(result, self.term())
        
        return result
    

    # CREATE TERM
    def term(self):
        result = self.factor()

        while self.current_token != None and self.current_token.type in (TokenType.MULTIPLY, TokenType.DIVIDE):
            if self.current_token.type == TokenType.MULTIPLY:
                self.advance()
                result = MultiplyNode(result, self.factor())
            elif self.current_token.type == TokenType.DIVIDE:
                self.advance()
                result = DivideNode(result, self.factor())
        
        return result
    

    # CREATE FACTOR
    def factor(self):
        token = self.current_token

        # Identify a function
        if token.type == TokenType.FUNCTION:
            func = token
            self.advance()

            if self.current_token.type != TokenType.LPAREN:
                self.raise_error("Lparen")
            self.advance()

            # Specify the function input
            result = self.expr()
            #self.advance()
            #while self.current_token.type != TokenType.RPAREN:
            #    self.advance()

            if self.current_token.type != TokenType.RPAREN:
                self.raise_error("Rparen")
            self.advance()
            
            return FunctionNode(name=token.name, input=NumberNode(result))

        # Find Lparentheses
        elif token.type == TokenType.LPAREN:
            self.advance()
            result = self.expr()

            # Next should be Rparentheses
            if self.current_token.type != TokenType.RPAREN:
                self.raise_error()
            
            self.advance()

            return result

        #Create numbernode
        elif token.type == TokenType.NUMBER:
            self.advance()
            return NumberNode(token.value)
        
        elif token.type == TokenType.VARIABLE:
            self.advance()
            return VariableNode(name=token.name, value=token.value)
        
        # Unitary operator
        elif token.type == TokenType.PLUS:
            self.advance()
            return PlusNode(self.factor())
        
        #Unitary operator
        elif token.type == TokenType.MINUS:
            self.advance()
            return MinusNode(self.factor())
        
        self.raise_error()
