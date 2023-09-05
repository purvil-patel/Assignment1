# Task 1

Medium Article Link: https://medium.com/@purvildipakbhai.patel/unleashing-the-power-of-gpt-4-for-exploratory-data-analysis-eda-6ea6659bddda

**PDF of the chatgpt chat**

[chatgpt1.pdf](https://github.com/purvil-patel/Assignment1/files/12508825/chatgpt1.pdf)


# Task 2

Created the calculator with the below functionality

**Calculator Functionalities**: 

The calculator application should primarily support basic arithmetic operations like addition, subtraction, multiplication, and division. Additionally, it would be beneficial to include advanced functionalities such as trigonometric functions, logarithms, exponentiation, and support for parentheses to manage the order of operations. A history function to recall previous calculations and a clear function to reset the calculator might also be beneficial.

**MVC Components Split:**

Model: This would include the core logic for calculations. It can be in a separate file named model.py.

View: This would deal with the user interface, both the display of results and the input buttons. This can be in a file named view.py.
Controller: This would handle user inputs, process them using the model, and update the view accordingly. This can be kept in a file named controller.py.

Keyboard Control: For a seamless user experience, the calculator should support both mouse clicks and keyboard inputs. The basic number keys (0-9) and arithmetic operators (+, -, *, /) should correspond to their respective functions on the calculator. Special keys like Enter can be used for equals, Backspace for delete or clear last entry, and Esc to clear all.

**Pytest Use Cases:**

Addition:

Test with positive numbers.

Test with negative numbers.

Test with a mix of positive and negative numbers.

Test with large numbers.

Test with zero.


Subtraction:

Test with a larger number subtracted from a smaller one.

Test with two negative numbers.

Test subtracting a negative number from a positive one.

Test subtracting zero.

Division:

Test with a standard division case.

Test division by zero (should handle exceptions).

Test division of a negative number by a positive one and vice versa.

Test with large numbers.

Test division resulting in a repeating decimal.

https://github.com/purvil-patel/Assignment1/assets/67355397/4eff76ec-7cea-4444-88cc-16a82a9b67ff


