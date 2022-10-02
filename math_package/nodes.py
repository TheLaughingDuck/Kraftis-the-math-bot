from dataclasses import dataclass

@dataclass
class NumberNode:
    value: float

    def __repr__(self):
        return f"{self.value}"

@dataclass
class VariableNode:
    name: str
    
    def __repr__(self):
        return f"{self.name}"

@dataclass
class FunctionNode:
    name: str
    input: any #? A numbernode?

    def __repr__(self) -> str:
        return f"{self.name}({self.input})"

@dataclass
class AddNode:
    node_a: any
    node_b: any

    def __repr__(self) -> str:
        return f"({self.node_a} + {self.node_b})"


@dataclass
class SubtractNode:
    node_a: any
    node_b: any

    def __repr__(self) -> str:
        return f"({self.node_a} - {self.node_b})"


@dataclass
class MultiplyNode:
    node_a: any
    node_b: any

    def __repr__(self) -> str:
        return f"({self.node_a} * {self.node_b})"


@dataclass
class DivideNode:
    node_a: any
    node_b: any

    def __repr__(self) -> str:
        return f"({self.node_a} / {self.node_b})"

# Unitary operator +
@dataclass
class PlusNode:
    node: any

    def __repr__(self) -> str:
        return f"(+{self.node})"


# Unitary operator -
@dataclass
class MinusNode:
    node: any

    def __repr__(self) -> str:
        return f"(-{self.node})"