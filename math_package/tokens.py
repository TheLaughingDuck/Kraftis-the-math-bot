from dataclasses import dataclass
from enum import Enum

class TokenType(Enum):
    NUMBER   = 0
    PLUS     = 1
    MINUS    = 2
    MULTIPLY = 3
    DIVIDE   = 4
    LPAREN   = 5
    RPAREN   = 6

    VARIABLE = 7
    FUNCTION = 8


@dataclass
class Token:
    type: TokenType
    name: any = None #if variable or function
    value: any = None

    def __repr__(self) -> str:
        out = self.type.name
        out += (f":{self.name}" if self.name != None else "")
        out += (f":{self.value}" if self.value != None else "")
        return out
        # return self.type.name + (f":{self.value}" if self.value != None else "")

        #(f":{self.name}" if self.name != None else "")