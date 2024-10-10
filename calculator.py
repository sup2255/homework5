"""This module provides a simple Calculator class for basic arithmetic operations."""

from typing import Union

Number = Union[int, float]

class Calculator:
    """A calculator class that provides basic arithmetic operations."""

    @staticmethod
    def add(a: Number, b: Number) -> Number:
        """
        Add two numbers.

        Args:
            a (Number): The first number.
            b (Number): The second number.

        Returns:
            Number: The sum of a and b.
        """
        return a + b

    @staticmethod
    def subtract(a: Number, b: Number) -> Number:
        """
        Subtract one number from another.

        Args:
            a (Number): The number to subtract from.
            b (Number): The number to subtract.

        Returns:
            Number: The result of a - b.
        """
        return a - b

    @staticmethod
    def multiply(a: Number, b: Number) -> Number:
        """
        Multiply two numbers.

        Args:
            a (Number): The first number.
            b (Number): The second number.

        Returns:
            Number: The product of a and b.
        """
        return a * b

    @staticmethod
    def divide(a: Number, b: Number) -> float:
        """
        Divide one number by another.

        Args:
            a (Number): The dividend.
            b (Number): The divisor.

        Returns:
            float: The result of a / b.

        Raises:
            ValueError: If b is zero.
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
