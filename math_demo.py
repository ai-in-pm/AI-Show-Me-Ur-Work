"""
This is a demo program that shows how to use our Math Problem Solver!
It can solve different types of math problems and show you all the steps,
just like a math tutor would do.
"""

# Import our math solver - it's like getting a calculator ready
from math_solver import MathProblemSolver

def demonstrate_math_solver():
    """
    This function shows examples of solving different types of math problems.
    It's like having a mini math class!
    """
    # Create our math solver - think of this as turning on your calculator
    solver = MathProblemSolver()
    
    # Example 1: Solving a Simple Linear Equation
    # These are equations like: 2x + 3 = 7
    print("\n[Example 1] Solving Linear Equation: 2x + 3 = 7")
    print("------------------------------------------------")
    result = solver.solve_equation("2x + 3 = 7")  # Give it the equation to solve
    solver.show_work()  # Show all the steps (like showing your work in class!)
    print(f"\n>>> Final Answer: x = {result}")
    
    # Example 2: Solving a Quadratic Equation
    # These are equations with x² in them, like: x² - 5x + 6 = 0
    print("\n[Example 2] Solving Quadratic Equation: x² - 5x + 6 = 0")
    print("-------------------------------------------------------")
    result = solver.solve_quadratic("1x^2-5x+6=0")
    solver.show_work()
    print(f"\n>>> Final Answer: x = {result}")
    
    # Example 3: Solving a Geometry Problem
    # Here we'll find the area of a triangle
    print("\n[Example 3] Calculating Triangle Area")
    print("------------------------------------")
    # We give it the base (6) and height (4) of the triangle
    result = solver.solve_geometry("triangle_area", {"base": 6, "height": 4})
    solver.show_work()
    print(f"\n>>> Final Answer: Area = {result}")

# This is where our program starts running
if __name__ == "__main__":
    print("Welcome to the Math Problem Solver Demo!")
    print("This program will show you how to solve different math problems.")
    demonstrate_math_solver()
    print("\nThat's all! Try changing the numbers to solve your own problems!")
