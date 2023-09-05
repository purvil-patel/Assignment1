from dataclasses import dataclass


@dataclass
class Calculator:
    result: float = 0

    def add(self, num1: float, num2: float) -> float:
        self.result = num1 + num2
        return self.result

    def subtract(self, num1: float, num2: float) -> float:
        self.result = num1 - num2
        return self.result

    def multiply(self, num1: float, num2: float) -> float:
        self.result = num1 * num2
        return self.result

    def divide(self, num1: float, num2: float) -> float:
        if num2 != 0:
            self.result = num1 / num2
            return self.result
        else:
            raise ZeroDivisionError("Cannot divide by zero")

    def exponentiate(self, base: float, exponent: float) -> float:
        self.result = base ** exponent
        return self.result

    def sin(self, angle: float) -> float:
        import math
        self.result = math.sin(math.radians(angle))
        return self.result

    def cos(self, angle: float) -> float:
        import math
        self.result = math.cos(math.radians(angle))
        return self.result

    def tan(self, angle: float) -> float:
        import math
        self.result = math.tan(math.radians(angle))
        return self.result

    def log(self, base: float, num: float) -> float:
        import math
        self.result = math.log(num, base)
        return self.result

    def clear(self) -> None:
        self.result = 0

    def get_result(self) -> float:
        return self.result
