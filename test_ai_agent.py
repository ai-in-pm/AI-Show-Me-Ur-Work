import pytest
from ai_agent import AIAgent

def test_basic_addition():
    agent = AIAgent()
    
    # Test basic addition
    agent.receive_input("123+456")
    result = agent.solve_problem()
    assert result == 579
    
    # Test with zeros
    agent = AIAgent()
    agent.receive_input("120+340")
    result = agent.solve_problem()
    assert result == 460

def test_basic_subtraction():
    agent = AIAgent()
    
    # Test basic subtraction
    agent.receive_input("456-123")
    result = agent.solve_problem()
    assert result == 333
    
    # Test with zeros
    agent = AIAgent()
    agent.receive_input("500-340")
    result = agent.solve_problem()
    assert result == 160

def test_basic_multiplication():
    agent = AIAgent()
    
    # Test basic multiplication
    agent.receive_input("12*34")
    result = agent.solve_problem()
    assert result == 408
    
    # Test with zeros
    agent = AIAgent()
    agent.receive_input("120*3")
    result = agent.solve_problem()
    assert result == 360

def test_carry_operations():
    # Addition with carries
    agent = AIAgent()
    agent.receive_input("999+1")
    result = agent.solve_problem()
    assert result == 1000
    
    agent = AIAgent()
    agent.receive_input("999+999")
    result = agent.solve_problem()
    assert result == 1998
    
    # Subtraction with borrows
    agent = AIAgent()
    agent.receive_input("1000-1")
    result = agent.solve_problem()
    assert result == 999
    
    agent = AIAgent()
    agent.receive_input("2000-999")
    result = agent.solve_problem()
    assert result == 1001
    
    # Multiplication with carries
    agent = AIAgent()
    agent.receive_input("999*9")
    result = agent.solve_problem()
    assert result == 8991

def test_edge_cases():
    # Addition
    agent = AIAgent()
    agent.receive_input("0+0")
    result = agent.solve_problem()
    assert result == 0
    
    # Subtraction
    agent = AIAgent()
    agent.receive_input("100-100")
    result = agent.solve_problem()
    assert result == 0
    
    # Multiplication
    agent = AIAgent()
    agent.receive_input("0*1000")
    result = agent.solve_problem()
    assert result == 0
    
    agent = AIAgent()
    agent.receive_input("1000*0")
    result = agent.solve_problem()
    assert result == 0

def test_invalid_inputs():
    agent = AIAgent()
    
    # Invalid format
    agent.receive_input("abc+def")
    result = agent.solve_problem()
    assert result is None
    
    # Multiple operations
    agent.receive_input("123+456-789")
    result = agent.solve_problem()
    assert result is None
    
    # Empty input
    agent.receive_input("")
    result = agent.solve_problem()
    assert result is None
    
    # Invalid subtraction (negative result)
    agent.receive_input("100-200")
    result = agent.solve_problem()
    assert result is None

def test_complex_operations():
    agent = AIAgent()
    
    # Large multiplication
    agent.receive_input("999*999")
    result = agent.solve_problem()
    assert result == 998001
    
    # Subtraction with many borrows
    agent.receive_input("1000-999")
    result = agent.solve_problem()
    assert result == 1
    
    # Addition with different lengths
    agent.receive_input("1+9999")
    result = agent.solve_problem()
    assert result == 10000

if __name__ == "__main__":
    print("\nRunning AI Agent Tests...")
    
    # Test basic operations
    print("\nTest Group 1: Basic Operations")
    
    print("\nTest 1.1: Addition (123 + 456)")
    agent = AIAgent()
    agent.receive_input("123+456")
    result = agent.solve_problem()
    agent.show_scratchpad()
    print(f"Expected: 579, Got: {result}")
    assert result == 579
    
    print("\nTest 1.2: Subtraction (456 - 123)")
    agent = AIAgent()
    agent.receive_input("456-123")
    result = agent.solve_problem()
    agent.show_scratchpad()
    print(f"Expected: 333, Got: {result}")
    assert result == 333
    
    print("\nTest 1.3: Multiplication (12 * 34)")
    agent = AIAgent()
    agent.receive_input("12*34")
    result = agent.solve_problem()
    agent.show_scratchpad()
    print(f"Expected: 408, Got: {result}")
    assert result == 408
    
    # Test carry/borrow operations
    print("\nTest Group 2: Carry/Borrow Operations")
    
    print("\nTest 2.1: Addition with Carry (999 + 1)")
    agent = AIAgent()
    agent.receive_input("999+1")
    result = agent.solve_problem()
    agent.show_scratchpad()
    print(f"Expected: 1000, Got: {result}")
    assert result == 1000
    
    print("\nTest 2.2: Subtraction with Borrow (1000 - 1)")
    agent = AIAgent()
    agent.receive_input("1000-1")
    result = agent.solve_problem()
    agent.show_scratchpad()
    print(f"Expected: 999, Got: {result}")
    assert result == 999
    
    print("\nTest 2.3: Multiplication with Carry (999 * 9)")
    agent = AIAgent()
    agent.receive_input("999*9")
    result = agent.solve_problem()
    agent.show_scratchpad()
    print(f"Expected: 8991, Got: {result}")
    assert result == 8991
    
    # Test complex operations
    print("\nTest Group 3: Complex Operations")
    
    print("\nTest 3.1: Large Multiplication (999 * 999)")
    agent = AIAgent()
    agent.receive_input("999*999")
    result = agent.solve_problem()
    agent.show_scratchpad()
    print(f"Expected: 998001, Got: {result}")
    assert result == 998001
    
    print("\nTest 3.2: Multiple Borrows (1000 - 999)")
    agent = AIAgent()
    agent.receive_input("1000-999")
    result = agent.solve_problem()
    agent.show_scratchpad()
    print(f"Expected: 1, Got: {result}")
    assert result == 1
    
    print("\nAll tests passed successfully! ")
