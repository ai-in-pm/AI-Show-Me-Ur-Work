class AIAgent:
    def __init__(self):
        self.scratchpad = []
        self.input = None
        self.output = None
        self.supported_operations = {
            '+': self.solve_addition,
            '-': self.solve_subtraction,
            '*': self.solve_multiplication
        }

    def receive_input(self, problem):
        """Step 1: Receive the input problem"""
        self.input = problem
        self.scratchpad = []  # Reset scratchpad for new problem
        self.scratchpad.append(f"Input received: {problem}")
        return self

    def show_scratchpad(self):
        """Display the current contents of the scratchpad"""
        print("\nScratchpad Contents:")
        for idx, step in enumerate(self.scratchpad, 1):
            print(f"Step {idx}: {step}")

    def parse_input(self, problem):
        """Parse input string into numbers and operation"""
        if not problem or not isinstance(problem, str):
            raise ValueError("Input must be a non-empty string")

        # Find the operation
        operation = None
        for op in self.supported_operations:
            if op in problem:
                if operation:  # Multiple operations found
                    raise ValueError("Only one operation allowed per problem")
                operation = op

        if not operation:
            raise ValueError("No supported operation found")

        # Split and convert numbers
        try:
            num1, num2 = map(str.strip, problem.split(operation))
            return int(num1), int(num2), operation
        except ValueError:
            raise ValueError("Invalid number format")

    def solve_addition(self, num1, num2):
        """Solve addition problems with step-by-step tracking"""
        num1_str = str(num1)
        num2_str = str(num2)
        max_len = max(len(num1_str), len(num2_str))
        num1_str = num1_str.zfill(max_len)
        num2_str = num2_str.zfill(max_len)
        
        carry = 0
        result = []
        
        for i in range(max_len - 1, -1, -1):
            digit1 = int(num1_str[i])
            digit2 = int(num2_str[i])
            current_sum = digit1 + digit2 + carry
            carry = current_sum // 10
            current_digit = current_sum % 10
            
            position = "units" if i == max_len - 1 else f"position {max_len - i}"
            self.scratchpad.append(
                f"Adding {position}: {digit1} + {digit2} + carry({carry}) = {current_sum}"
            )
            if carry:
                self.scratchpad.append(f"Set carry to {carry}")
            
            result.insert(0, str(current_digit))
        
        if carry:
            result.insert(0, str(carry))
            self.scratchpad.append(f"Final carry: {carry}")
        
        final_result = int(''.join(result))
        self.output = final_result
        self.scratchpad.append(f"Final result: {final_result}")
        return final_result

    def solve_subtraction(self, num1, num2):
        """Solve subtraction problems with step-by-step tracking"""
        if num2 > num1:
            raise ValueError("First number must be greater than or equal to second number")

        num1_str = str(num1)
        num2_str = str(num2).zfill(len(num1_str))
        borrow = 0
        result = []
        
        for i in range(len(num1_str) - 1, -1, -1):
            digit1 = int(num1_str[i])
            digit2 = int(num2_str[i])
            
            if borrow:
                digit1 -= 1
                self.scratchpad.append(f"Applied borrow: {int(num1_str[i])} becomes {digit1}")
            
            if digit1 < digit2:
                digit1 += 10
                borrow = 1
                self.scratchpad.append(f"Need to borrow: {digit1-10} becomes {digit1}")
            else:
                borrow = 0
            
            current_diff = digit1 - digit2
            position = "units" if i == len(num1_str) - 1 else f"position {len(num1_str) - i}"
            self.scratchpad.append(f"Subtracting {position}: {digit1} - {digit2} = {current_diff}")
            
            result.insert(0, str(current_diff))
        
        final_result = int(''.join(result))
        self.output = final_result
        self.scratchpad.append(f"Final result: {final_result}")
        return final_result

    def solve_multiplication(self, num1, num2):
        """Solve multiplication problems with step-by-step tracking"""
        num1_str = str(num1)
        num2_str = str(num2)
        
        # Initialize the partial results
        partial_results = []
        
        # Process each digit of num2 from right to left
        for i in range(len(num2_str) - 1, -1, -1):
            digit2 = int(num2_str[i])
            carry = 0
            current_result = []
            zeros = '0' * (len(num2_str) - 1 - i)  # Add trailing zeros for position
            
            self.scratchpad.append(f"\nMultiplying by {digit2} at position {len(num2_str) - i - 1}:")
            
            # Multiply digit2 with each digit of num1
            for j in range(len(num1_str) - 1, -1, -1):
                digit1 = int(num1_str[j])
                product = digit1 * digit2 + carry
                carry = product // 10
                current_digit = product % 10
                
                self.scratchpad.append(
                    f"  {digit1} × {digit2} + carry({carry}) = {product}"
                )
                
                current_result.insert(0, str(current_digit))
            
            if carry:
                current_result.insert(0, str(carry))
                self.scratchpad.append(f"  Final carry: {carry}")
            
            current_result.extend(zeros)
            partial_result = int(''.join(current_result))
            partial_results.append(partial_result)
            self.scratchpad.append(f"Partial result: {partial_result}")
        
        # Sum all partial results
        final_result = sum(partial_results)
        self.output = final_result
        self.scratchpad.append(f"\nFinal result: {final_result}")
        return final_result

    def solve_problem(self):
        """Generic problem-solving method"""
        try:
            num1, num2, operation = self.parse_input(self.input)
            return self.supported_operations[operation](num1, num2)
        except ValueError as e:
            self.scratchpad.append(f"Error: {str(e)}")
            return None
        except Exception as e:
            self.scratchpad.append(f"Error: Unexpected error occurred - {str(e)}")
            return None

if __name__ == "__main__":
    # Create an instance of AIAgent
    agent = AIAgent()
    
    # Example 1: Simple addition
    print("\nExample 1: 123 + 456")
    agent.receive_input("123+456")
    result = agent.solve_problem()
    agent.show_scratchpad()
    print(f"Final Result: {result}\n")
    
    # Example 2: Addition with carry
    print("\nExample 2: 999 + 1")
    agent = AIAgent()
    agent.receive_input("999+1")
    result = agent.solve_problem()
    agent.show_scratchpad()
    print(f"Final Result: {result}\n")
    
    # Example 3: Invalid input
    print("\nExample 3: Invalid input (abc + def)")
    agent = AIAgent()
    agent.receive_input("abc+def")
    result = agent.solve_problem()
    agent.show_scratchpad()
    print(f"Final Result: {result}\n")
