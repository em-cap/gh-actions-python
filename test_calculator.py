"""
Test suite for the calculator module.
Run with: pytest test_calculator.py
"""

import pytest
import numpy as np
import requests
from unittest.mock import patch, Mock
from calculator import Calculator


class TestCalculator:
    """Test class for Calculator functionality."""
    
    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.calc = Calculator()
    
    def test_add(self):
        """Test addition operation."""
        assert self.calc.add(2, 3) == 5
        assert self.calc.add(-1, 1) == 0
        assert self.calc.add(0, 0) == 0
        assert self.calc.add(2.5, 3.5) == 6.0
    
    def test_subtract(self):
        """Test subtraction operation."""
        assert self.calc.subtract(5, 3) == 2
        assert self.calc.subtract(0, 5) == -5
        assert self.calc.subtract(10, 10) == 0
        assert self.calc.subtract(7.5, 2.5) == 5.0
    
    def test_multiply(self):
        """Test multiplication operation."""
        assert self.calc.multiply(3, 4) == 12
        assert self.calc.multiply(-2, 3) == -6
        assert self.calc.multiply(0, 5) == 0
        assert self.calc.multiply(2.5, 4) == 10.0
    
    def test_divide(self):
        """Test division operation."""
        assert self.calc.divide(10, 2) == 5
        assert self.calc.divide(7, 2) == 3.5
        assert self.calc.divide(-8, 4) == -2
        
        # Test division by zero
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            self.calc.divide(5, 0)
    
    def test_power(self):
        """Test power operation."""
        assert self.calc.power(2, 3) == 8
        assert self.calc.power(5, 2) == 25
        assert self.calc.power(4, 0.5) == 2
        assert self.calc.power(10, 0) == 1
    
    def test_square_root(self):
        """Test square root operation."""
        assert self.calc.square_root(9) == 3
        assert self.calc.square_root(16) == 4
        assert self.calc.square_root(0) == 0
        assert abs(self.calc.square_root(2) - 1.4142135623730951) < 1e-10
        
        # Test square root of negative number
        with pytest.raises(ValueError, match="Cannot calculate square root of negative number"):
            self.calc.square_root(-1)
    
    @patch('calculator.requests.get')
    def test_get_random_number_success(self, mock_get):
        """Test successful API call for random number."""
        # Mock successful API response
        mock_response = Mock()
        mock_response.text = "42\n"
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response
        
        result = self.calc.get_random_number()
        assert result == 42
        
        # Verify the API was called with correct parameters
        mock_get.assert_called_once_with(
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
    
    @patch('calculator.requests.get')
    @patch('calculator.np.random.randint')
    def test_get_random_number_api_failure(self, mock_randint, mock_get):
        """Test fallback to numpy random when API fails."""
        # Mock API failure with requests.RequestException
        mock_get.side_effect = requests.RequestException("API Error")
        mock_randint.return_value = 75
        
        result = self.calc.get_random_number()
        assert result == 75
        
        # Verify numpy random was called as fallback
        mock_randint.assert_called_once_with(1, 101)
    
    def test_integration_random_number_calculation(self):
        """Integration test combining random number with calculation."""
        # This test will actually call the API or use numpy fallback
        random_num = self.calc.get_random_number()
        
        # Verify random number is in expected range
        assert 1 <= random_num <= 100
        
        # Test using the random number in calculations
        squared = self.calc.power(random_num, 2)
        assert squared == random_num ** 2
        
        # Test square root of the squared number should give us back the original
        sqrt_result = self.calc.square_root(squared)
        assert abs(sqrt_result - random_num) < 1e-10


# Additional test functions for pytest discovery
def test_calculator_instance_creation():
    """Test that Calculator can be instantiated."""
    calc = Calculator()
    assert calc is not None


def test_multiple_operations():
    """Test chaining multiple operations."""
    calc = Calculator()
    
    # Test: (10 + 5) * 2 - 3 = 27
    step1 = calc.add(10, 5)  # 15
    step2 = calc.multiply(step1, 2)  # 30
    step3 = calc.subtract(step2, 3)  # 27
    
    assert step3 == 27


if __name__ == "__main__":
    # Run tests if this file is executed directly
    pytest.main([__file__])