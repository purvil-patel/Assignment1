from calculator import Calculator
from view import CalculatorView


class CalculatorController:
    def __init__(self):
        self.calculator = Calculator()

    def start(self) -> None:
        while True:
            CalculatorView.show_menu()
            user_input = CalculatorView.get_user_input()
            if user_input == 'q':
                break
            self.handle_input(user_input)

    def handle_input(self, input: str) -> None:
        try:
            if input == '0':
                self.calculator.clear()
            elif input == '1':
                self.perform_calculation("add")
            elif input == '2':
                self.perform_calculation("subtract")
            elif input == '3':
                self.perform_calculation("multiply")
            elif input == '4':
                self.perform_calculation("divide")
            elif input == '5':
                self.perform_calculation("exponentiate")
            elif input == '6':
                self.perform_calculation("sin")
            elif input == '7':
                self.perform_calculation("cos")
            elif input == '8':
                self.perform_calculation("tan")
            elif input == '9':
                self.perform_calculation("log")
            else:
                CalculatorView.display_error("Invalid input")
        except Exception as e:
            CalculatorView.display_error(str(e))

    def perform_calculation(self, operation: str) -> None:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = getattr(self.calculator, operation)(num1, num2)
        CalculatorView.display_result(result)


if __name__ == "__main__":
    calculator_controller = CalculatorController()
    calculator_controller.start()
