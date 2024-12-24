from ai_agent import AIAgent

def demonstrate_addition():
    # Create an instance of the AI Agent
    agent = AIAgent()
    
    # Example 1: Adding 29 + 57 (as shown in the original example)
    print("\nExample 1: 29 + 57")
    agent.receive_input("29+57")
    result = agent.solve_problem()
    agent.show_scratchpad()
    print(f"Final Answer: {result}")
    
    # Example 2: A different addition problem
    print("\nExample 2: 123 + 456")
    agent = AIAgent()  # Create a new instance
    agent.receive_input("123+456")
    result = agent.solve_problem()
    agent.show_scratchpad()
    print(f"Final Answer: {result}")

if __name__ == "__main__":
    demonstrate_addition()
