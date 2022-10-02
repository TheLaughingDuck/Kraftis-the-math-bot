from .tokens import Token, TokenType

WHITESPACE = " \n\t"
DIGITS = "1234567890"
VARNAMES = "X"
LETTERS = "abcdefghijklmnopqrstuvwxyz"

class Lexer:
    def __init__(self, text, var_value=None):
        self.text = iter(text)
        self.advance() #Advance to first character
        self.var_value=var_value
    

    def advance(self):
        try:
            self.current_char = next(self.text)
        except StopIteration:
            self.current_char = None
    
    def generate_tokens(self):
        while self.current_char != None:
            # Ignore whitespaces
            if self.current_char in WHITESPACE:
                self.advance()
            
            # Create ordinary tokens (number, signs, parentheses)
            elif self.current_char == "." or self.current_char in DIGITS:
                yield self.generate_number()
            elif self.current_char == "+":
                self.advance()
                yield Token(TokenType.PLUS)
            elif self.current_char == "-":
                self.advance()
                yield Token(TokenType.MINUS)
            elif self.current_char == "*":
                self.advance()
                yield Token(TokenType.MULTIPLY)
            elif self.current_char == "/":
                self.advance()
                yield Token(TokenType.DIVIDE)
            elif self.current_char == "(":
                self.advance()
                yield Token(TokenType.LPAREN)
            elif self.current_char == ")":
                self.advance()
                yield Token(TokenType.RPAREN)
            
            # Create VARIABLE token
            elif self.current_char in VARNAMES:
                thisname = self.current_char
                self.advance()
                yield Token(TokenType.VARIABLE, name=thisname, value=self.var_value)
            
            # Create FUNCTION token
            elif self.current_char in LETTERS:
                # Collect the whole supposed function name
                func_name = self.current_char
                self.advance()
                
                while self.current_char != None and (self.current_char in LETTERS):
                    func_name += self.current_char
                    self.advance()
                
                # Maybe check if function exists?
                yield Token(TokenType.FUNCTION, name=func_name)

                #Proceed to yield parentheses and input
                #Do this in parser_.py instead
                #if self.current_char != "(":
                #    raise Exception("Incorrect format. Expected: \"(\" but Received: " + self.current_char)
                #self.advance()


            
            else:
                raise Exception(f"Un-interpretable character: '{self.current_char}'")


    def generate_number(self):
        decimal_point_count = 0
        number_str = self.current_char
        self.advance()

        while self.current_char != None and (self.current_char == "." or self.current_char in DIGITS):
            # Check that there is only one decimal point
            if self.current_char == ".":
                decimal_point_count += 1
                if decimal_point_count > 1:
                    break
            
            number_str += self.current_char
            self.advance()
        
        # Handling some special cases
        if number_str.startswith("."):
            number_str = "0" + number_str
        if number_str.endswith("."):
            number_str += "0"
        
        # Number is finished, time to return it
        return Token(TokenType.NUMBER, value=float(number_str))
        
