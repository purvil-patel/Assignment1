class CalculatorView:
    @staticmethod
    def show_menu() -> None:
        print("Calculator Menu:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exponentiation")
        print("6. Sine")
        print("7. Cosine")
        print("8. Tangent")
        print("9. Logarithm")
        print("0. Clear")
        print("q. Quit")

    @staticmethod
    def get_user_input() -> str:
        return input("Enter your choice: ")

    @staticmethod
    def display_result(result: float) -> None:
        print("Result:", result)

    @staticmethod
    def display_error(message: str) -> None:
        print("Error:", message)
