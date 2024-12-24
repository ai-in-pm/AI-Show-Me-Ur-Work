# AI Show Work Agent

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

This project implements an AI agent that demonstrates its problem-solving process by showing its work step by step. The agent uses a scratchpad to record intermediate computations and reasoning steps, making it ideal for educational purposes or understanding complex calculations.

The development of this GitHub Repository was inspired by the "SHOW YOUR WORK: SCRATCHPADS FOR INTERMEDIATE COMPUTATION WITH LANGUAGE MODELS" Paper, Paper can be found by clicking this link: https://arxiv.org/pdf/2112.00114

## 🌟 Features

- Step-by-step computation display
- Scratchpad mechanism for tracking intermediate steps
- Support for multiple arithmetic operations:
  - Addition with carry handling
  - Subtraction with borrow handling
  - Multiplication with partial products
- Detailed explanation of each computation step
- Robust error handling and input validation
- Comprehensive test suite

## 🚀 Quick Start

### Prerequisites

- Python 3.11 or higher
- pip (Python package installer)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/AI-Show-me-ur-work.git
cd AI-Show-me-ur-work
```

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the virtual environment:
   - Windows:
   ```bash
   .\venv\Scripts\activate
   ```
   - Unix/MacOS:
   ```bash
   source venv/bin/activate
   ```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Set up environment variables:
   - Copy `.env.sample` to `.env`
   - Update the values in `.env` according to your needs

## 🔧 Configuration

### Environment Variables

- `OPENAI_API_KEY`: Your OpenAI API key (required)
- `DEBUG`: Enable/disable debug mode (True/False)
- `LOG_LEVEL`: Set logging level (INFO, DEBUG, WARNING, ERROR)
- `MAX_STEPS`: Maximum number of computation steps
- `SHOW_INTERMEDIATE_STEPS`: Show intermediate computation steps (True/False)

## 📖 Usage

1. Import the AIAgent class:
```python
from ai_agent import AIAgent
```

2. Create an instance of the agent:
```python
agent = AIAgent()
```

3. Solve arithmetic problems:
```python
# Addition
agent.receive_input("123+456")
result = agent.solve_problem()
agent.show_scratchpad()  # Shows step-by-step solution

# Subtraction
agent.receive_input("1000-999")
result = agent.solve_problem()
agent.show_scratchpad()

# Multiplication
agent.receive_input("12*34")
result = agent.solve_problem()
agent.show_scratchpad()
```

## 📝 Example Output

```python
# Addition with carry
agent.receive_input("999+1")
result = agent.solve_problem()
agent.show_scratchpad()

# Output:
Scratchpad Contents:
Step 1: Input received: 999+1
Step 2: Adding units: 9 + 1 + carry(0) = 10
Step 3: Set carry to 1
Step 4: Adding position 2: 9 + 0 + carry(1) = 10
Step 5: Set carry to 1
Step 6: Adding position 3: 9 + 0 + carry(1) = 10
Step 7: Set carry to 1
Step 8: Final carry: 1
Step 9: Final result: 1000
```

## 🧪 Testing

Run the test suite:
```bash
pytest test_ai_agent.py -v
```

The test suite includes:
- Basic operation tests
- Carry/borrow operation tests
- Edge cases
- Invalid input handling
- Complex calculations

## ⚠️ Error Handling

The agent handles various error cases:
- Invalid input format
- Unsupported operations
- Multiple operations in one input
- Negative results in subtraction
- Empty or non-string input

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Please make sure to update tests as appropriate and adhere to the existing coding style.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Special thanks to the Python community for the amazing tools and libraries

## 📬 Contact

If you have any questions or suggestions, please open an issue or submit a pull request.
