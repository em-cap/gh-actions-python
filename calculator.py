"""
Simple calculator module with basic mathematical operations.
Uses the requests library to fetch random numbers and numpy for advanced calculations.
"""

import requests
import numpy as np
from typing import Union


class Calculator:
    """A simple calculator class with basic and advanced operations."""
    
    def add(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Add two numbers."""
        return a + b
    
    def subtract(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Subtract second number from first number."""
        return a - b
    
    def multiply(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Multiply two numbers."""
        return a * b
    
    def divide(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Divide first number by second number."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    def power(self, base: Union[int, float], exponent: Union[int, float]) -> Union[int, float]:
        """Calculate base raised to the power of exponent using numpy."""
        return np.power(base, exponent)
    
    def square_root(self, number: Union[int, float]) -> float:
        """Calculate square root using numpy."""
        if number < 0:
            raise ValueError("Cannot calculate square root of negative number")
        return np.sqrt(number)
    
    def get_random_number(self) -> int:
        """Fetch a random number from an external API."""
        try:
            response = requests.get(
                "https://www.random.org/integers/",
                params={
                    "num": 1,
                    "min": 1,
                    "max": 100,
                    "col": 1,
                    "base": 10,
                    "format": "plain",
                    "rnd": "new"
                },
                timeout=5
            )
            response.raise_for_status()
            return int(response.text.strip())
        except (requests.RequestException, ValueError) as e:
            # Fallback to numpy random if API fails
            print(f"API request failed: {e}. Using numpy random instead.")
            return int(np.random.randint(1, 101))


def main():
    """Main function to demonstrate calculator functionality."""
    calc = Calculator()
    
    print("=== Python Calculator Demo ===")
    print(f"Addition: 10 + 5 = {calc.add(10, 5)}")
    print(f"Subtraction: 10 - 5 = {calc.subtract(10, 5)}")
    print(f"Multiplication: 10 * 5 = {calc.multiply(10, 5)}")
    print(f"Division: 10 / 5 = {calc.divide(10, 5)}")
    print(f"Power: 2^3 = {calc.power(2, 3)}")
    print(f"Square root of 16 = {calc.square_root(16)}")
    
    print("\n=== Random Number Demo ===")
    random_num = calc.get_random_number()
    print(f"Random number from API: {random_num}")
    print(f"Square of random number: {calc.power(random_num, 2)}")


if __name__ == "__main__":
    main()