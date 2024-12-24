"""
Math Problem Solver
This is like having a super-smart calculator that can solve different types of math problems!
It not only gives you the answer but also shows you how it got there, step by step.
"""

# Import the tools we need
import math  # For mathematical operations like square root
from typing import List, Dict, Any, Union  # These help us organize our code better
import re  # This helps us work with equations written as text

class MathProblemSolver:
    """
    This is our main problem solver class. Think of it as a smart calculator
    that can solve different types of math problems and show its work!
    """
    def __init__(self):
        """
        Getting ready to solve problems:
        - scratchpad: where we write down our work
        - steps: detailed explanation of each step
        """
        self.scratchpad: List[str] = []  # Like scratch paper for calculations
        self.problem: str = ""  # The problem we're trying to solve
        self.solution: Any = None  # Where we'll store the final answer
        self.steps: List[Dict[str, str]] = []  # List of steps we take
        
    def log_step(self, description: str, work: str = "", result: str = ""):
        """
        This is like writing down each step in your math homework
        so you can show how you got your answer!
        """
        self.steps.append({
            "description": description,  # What we're doing
            "work": work,               # How we're doing it
            "result": result           # What we got
        })
        self.scratchpad.append(f"{description}: {work} => {result}")

    def solve_equation(self, equation: str) -> Union[float, str]:
        """
        Solves simple equations like: 2x + 3 = 7
        Returns the value of x
        """
        if not isinstance(equation, str):
            return "Error: Please provide the equation as a string"
            
        self.log_step("[START] Solving equation", equation)
        
        # Clean up the equation by removing spaces
        equation = equation.replace(" ", "")
        self.log_step("Making equation easier to read", f"Original: {equation}")
        
        # Split into left and right sides of the equals sign
        if "=" not in equation:
            return "Error: Invalid equation format - missing equals sign (=)"
            
        left, right = equation.split("=")
        if not left or not right:
            return "Error: Invalid equation format - empty side of equation"
            
        self.log_step("Breaking equation into two parts", f"Left: {left}, Right: {right}")
        
        # Sort terms: put x terms on left, numbers on right
        left_terms = []   # Will hold coefficients of x terms
        right_terms = []  # Will hold regular numbers
        
        # Look at the left side of the equation
        terms = re.findall(r'[+-]?\s*\d*x?', left)
        for term in terms:
            if 'x' in term:  # If this term has an x in it
                coef = term.replace('x', '')
                coef = '1' if coef in ['+', ''] else '-1' if coef == '-' else coef
                left_terms.append(float(coef))
                self.log_step("Found an x term", f"Term: {term}", f"Coefficient: {coef}")
            else:
                if term:  # If it's a regular number
                    right_terms.append(-float(term))
                    self.log_step("Moving number to right side", term, f"Added {-float(term)} to right side")

        # Look at the right side of the equation
        terms = re.findall(r'[+-]?\s*\d*x?', right)
        for term in terms:
            if 'x' in term:  # If this term has an x in it
                coef = term.replace('x', '')
                coef = '1' if coef in ['+', ''] else '-1' if coef == '-' else coef
                left_terms.append(-float(coef))
                self.log_step("Moving x term to left side", term, f"Added {-float(coef)}x to left side")
            else:
                if term:  # If it's a regular number
                    right_terms.append(float(term))
                    self.log_step("Found a number on right side", term)

        # Add up all the x terms and all the numbers
        x_coef = sum(left_terms)
        num_sum = sum(right_terms)
        
        self.log_step("Adding like terms", 
                     f"x terms: {left_terms}, numbers: {right_terms}",
                     f"{x_coef}x = {num_sum}")

        # Find x by dividing both sides by coefficient of x
        if x_coef == 0:
            if num_sum == 0:
                return "This equation has infinite solutions!"
            else:
                return "This equation has no solution!"
        
        solution = num_sum / x_coef
        self.log_step("Solving for x", 
                     f"{x_coef}x = {num_sum}",
                     f"x = {solution}")
        
        return solution

    def solve_quadratic(self, equation: str) -> Union[tuple, str]:
        """
        Solves quadratic equations like: x² - 5x + 6 = 0
        Uses the quadratic formula: x = (-b ± √(b² - 4ac)) / (2a)
        """
        if not isinstance(equation, str):
            return "Error: Please provide the equation as a string"
            
        self.log_step("[START] Solving quadratic equation", equation)
        
        # Clean up the equation
        equation = equation.replace(" ", "").replace("²", "^2")
        self.log_step("Making equation easier to read", equation)
        
        # Ensure equation is in standard form (= 0)
        if not equation.endswith("=0"):
            return "Error: Quadratic equation must be in standard form (ax² + bx + c = 0)"
        
        # Find a, b, and c in ax² + bx + c = 0
        # More robust pattern matching that handles various formats
        equation = equation[:-2]  # Remove "=0"
        parts = re.findall(r'[+-]?\s*\d*x\^2|[+-]?\s*\d*x|[+-]?\s*\d+', equation)
        
        if not parts:
            return "Error: Invalid quadratic equation format"
            
        a = b = c = 0
        for part in parts:
            if 'x^2' in part:
                coef = part.replace('x^2', '').strip('+-')
                a = float(coef if coef and coef != '+' else '1' if part[0] != '-' else '-1')
            elif 'x' in part:
                coef = part.replace('x', '').strip('+-')
                b = float(coef if coef and coef != '+' else '1' if part[0] != '-' else '-1')
            else:
                c = float(part)
                
        if a == 0:
            return "Error: This is not a quadratic equation (coefficient of x² is 0)"
        
        self.log_step("Found the important numbers", 
                     f"From: {equation}",
                     f"a={a}, b={b}, c={c}")

        # Calculate b² - 4ac (called the discriminant)
        discriminant = b**2 - 4*a*c
        self.log_step("Calculating discriminant", 
                     f"b² - 4ac = {b}² - 4({a})({c})",
                     str(discriminant))

        if discriminant < 0:
            return "This equation has no real solutions (the answers would be imaginary numbers)"
        
        # Use the quadratic formula to find both solutions
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        
        self.log_step("Using the quadratic formula", 
                     f"x = (-{b} ± √{discriminant}) / (2*{a})",
                     f"x₁ = {x1}, x₂ = {x2}")

        return (x1, x2)

    def solve_geometry(self, problem_type: str, values: Dict[str, float]) -> Union[float, str]:
        """
        Solves geometry problems like finding areas of shapes
        Currently supports:
        - Triangle area (½ × base × height)
        - Circle area (πr²)
        """
        if not isinstance(problem_type, str) or not isinstance(values, dict):
            return "Error: Invalid input types"
            
        self.log_step("[START] Solving geometry problem", 
                     f"Type: {problem_type}, Values: {values}")
        
        if problem_type == "triangle_area":
            if not all(key in values for key in ["base", "height"]):
                return "Error: Triangle area calculation requires both 'base' and 'height' values"
            if not all(isinstance(values[key], (int, float)) for key in ["base", "height"]):
                return "Error: Base and height must be numbers"
            if any(values[key] <= 0 for key in ["base", "height"]):
                return "Error: Base and height must be positive numbers"
                
            area = 0.5 * values["base"] * values["height"]
            self.log_step("Calculating triangle area",
                        f"Area = ½ × base × height = ½ × {values['base']} × {values['height']}",
                        str(area))
            return area
                
        elif problem_type == "circle_area":
            if "radius" not in values:
                return "Error: Circle area calculation requires a 'radius' value"
            if not isinstance(values["radius"], (int, float)):
                return "Error: Radius must be a number"
            if values["radius"] <= 0:
                return "Error: Radius must be a positive number"
                
            area = math.pi * values["radius"]**2
            self.log_step("Calculating circle area",
                        f"Area = πr² = π × {values['radius']}²",
                        str(area))
            return area
        
        return f"Error: Unsupported geometry problem type '{problem_type}'. Supported types: triangle_area, circle_area"

    def show_work(self) -> None:
        """
        Shows all the steps we took to solve the problem,
        just like showing your work in math class!
        """
        print("\n[Solution Steps]")
        for i, step in enumerate(self.steps, 1):
            print(f"\nStep {i}:")
            print(f"What we're doing: {step['description']}")
            if step['work']:
                print(f"How we're doing it: {step['work']}")
            if step['result']:
                print(f"What we got: {step['result']}")
        print("\n[All our work]")
        for i, note in enumerate(self.scratchpad, 1):
            print(f"{i}. {note}")
