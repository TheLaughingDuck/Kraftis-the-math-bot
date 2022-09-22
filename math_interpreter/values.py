from dataclasses import dataclass

@dataclass
class Number:
    value: float

    def __repr__(self) -> str:
        return f"{self.value}"