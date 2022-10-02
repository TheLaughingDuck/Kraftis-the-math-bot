from .lexer import Lexer
from .tokens import TokenType
from .parser_ import Parser
from .interpreter import Interpreter

# Perform One Calculation
def evaluate(text, var_value=None):
    try:
        # CREATE A TREE
        lexer = Lexer(text, var_value=var_value)
        tokens = lexer.generate_tokens()
        parser = Parser(tokens)
        tree = parser.parse()

        # Resolve the TREE
        if not tree: return("Bad input")
        interpreter = Interpreter()
        value = interpreter.visit(tree)
        return  value
    except Exception as e:
        return e


# For Continuous calculations
while False:
        try:
            # CREATE A TREE
            text = input(">> ")
            lexer = Lexer(text)
            tokens = lexer.generate_tokens()
            parser = Parser(tokens)
            tree = parser.parse()

            # Resolve the TREE
            if not tree: continue
            interpreter = Interpreter()
            value = interpreter.visit(tree)
            print(value)
        except Exception as e:
            print(e)