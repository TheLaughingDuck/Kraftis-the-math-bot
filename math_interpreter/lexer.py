from tokens import Token, TokenType

WHITESPACE = " \n\t"
DIGITS = "1234567890"

class Lexer:
    def __init__(self, text):
        self.text = iter(text)
        self.advance() #Advance to first character
    

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
                yield Token(TokenType.LAPREN)
            elif self.current_char == ")":
                self.advance()
                yield Token(TokenType.RPAREN)
            elif self.current_char == "x":
                self.advance()
                yield Token(TokenType.VARIABLE)
            
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
        return Token(TokenType.NUMBER, float(number_str))
