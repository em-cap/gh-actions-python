# Calculator Package

A simple calculator demonstration project for GitHub Actions CI/CD workshop.

## Features

- Basic mathematical operations (add, subtract, multiply, divide)
- Advanced operations using NumPy (power, square root)
- External API integration for random number generation
- Comprehensive error handling
- Full test coverage with pytest

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### As a script:
```bash
python calculator.py
```

### As a module:
```python
from calculator import Calculator

calc = Calculator()
result = calc.add(5, 3)
print(result)  # Output: 8
```

## Testing

Run all tests:
```bash
pytest test_calculator.py
```

Run tests with coverage:
```bash
pytest --cov=calculator test_calculator.py
```

## Development

Install development dependencies:
```bash
pip install -r requirements-dev.txt
```

Format code:
```bash
black calculator.py test_calculator.py
```

Lint code:
```bash
flake8 calculator.py test_calculator.py
```

Type checking:
```bash
mypy calculator.py
```

## GitHub Actions Workshop

This project is designed for a 1-hour GitHub Actions workshop where students learn to:

1. Set up automated testing
2. Add code quality checks
3. Build and package Python projects
4. Deploy to package repositories

## License

MIT License