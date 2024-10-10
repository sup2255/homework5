"""
This module implements a command-line calculator application using the Command pattern.
It provides basic arithmetic operations and a menu system for user interaction.
"""

import os
import importlib
import multiprocessing
from typing import Dict, Union
from calculator import Calculator

Number = Union[int, float]

class Command:
    """Base class for all commands."""

    def execute(self) -> Number:
        """Execute the command."""
        raise NotImplementedError("Subclass must implement abstract method")

class AddCommand(Command):
    """Command to perform addition."""

    def __init__(self, a: Number, b: Number):
        """
        Initialize the AddCommand.

        Args:
            a (Number): The first number.
            b (Number): The second number.
        """
        self.calculator = Calculator()
        self.a = a
        self.b = b

    def execute(self) -> Number:
        """Execute the addition command."""
        return self.calculator.add(self.a, self.b)

class SubtractCommand(Command):
    """Command to perform subtraction."""

    def __init__(self, a: Number, b: Number):
        """
        Initialize the SubtractCommand.

        Args:
            a (Number): The number to subtract from.
            b (Number): The number to subtract.
        """
        self.calculator = Calculator()
        self.a = a
        self.b = b

    def execute(self) -> Number:
        """Execute the subtraction command."""
        return self.calculator.subtract(self.a, self.b)

class MultiplyCommand(Command):
    """Command to perform multiplication."""

    def __init__(self, a: Number, b: Number):
        """
        Initialize the MultiplyCommand.

        Args:
            a (Number): The first number.
            b (Number): The second number.
        """
        self.calculator = Calculator()
        self.a = a
        self.b = b

    def execute(self) -> Number:
        """Execute the multiplication command."""
        return self.calculator.multiply(self.a, self.b)

class DivideCommand(Command):
    """Command to perform division."""

    def __init__(self, a: Number, b: Number):
        """
        Initialize the DivideCommand.

        Args:
            a (Number): The dividend.
            b (Number): The divisor.
        """
        self.calculator = Calculator()
        self.a = a
        self.b = b

    def execute(self) -> float:
        """
        Execute the division command.

        Raises:
            ValueError: If attempting to divide by zero.
        """
        return self.calculator.divide(self.a, self.b)

class MenuCommand(Command):
    """Command to display the menu of available operations."""

    def __init__(self, commands: Dict[str, type]):
        """
        Initialize the MenuCommand.

        Args:
            commands (Dict[str, type]): A dictionary of available commands.
        """
        self.commands = commands

    def execute(self) -> None:
        """Display the menu of available commands."""
        print("Available commands:")
        for command in self.commands:
            print(f"- {command}")

def get_number_input(prompt: str) -> Number:
    """
    Get a number input from the user.

    Args:
        prompt (str): The prompt to display to the user.

    Returns:
        Number: The number entered by the user.

    Raises:
        ValueError: If the input cannot be converted to a float.
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def load_plugins():
    """
    Dynamically load plugins from the 'plugins' directory.

    Returns:
        Dict[str, type]: A dictionary of plugin commands.
    """
    plugins = {}
    plugin_dir = 'plugins'
    if os.path.exists(plugin_dir):
        for filename in os.listdir(plugin_dir):
            if filename.endswith('.py'):
                module_name = filename[:-3]
                module = importlib.import_module(f'{plugin_dir}.{module_name}')
                if hasattr(module, 'load'):
                    plugins.update(module.load())
    return plugins

def execute_command(command):
    """Execute a command in a separate process."""
    return command.execute()

def main():
    """Main function to run the calculator application."""
    commands: Dict[str, Union[type, MenuCommand]] = {
        'add': AddCommand,
        'subtract': SubtractCommand,
        'multiply': MultiplyCommand,
        'divide': DivideCommand,
    }
    
    # Load plugins
    commands.update(load_plugins())

    menu_command = MenuCommand(commands)
    commands['menu'] = menu_command

    print("Welcome to the Calculator App!")
    menu_command.execute()

    while True:
        user_input = input("\nEnter command (add/subtract/multiply/divide/menu) or 'quit' to exit: ").lower()
        
        if user_input == 'quit':
            print("Thank you for using the Calculator App. Goodbye!")
            break

        if user_input in commands:
            if user_input == 'menu':
                menu_command.execute()
            else:
                try:
                    a = get_number_input("Enter first number: ")
                    b = get_number_input("Enter second number: ")
                    command = commands[user_input](a, b)
                    
                    with multiprocessing.Pool(1) as pool:
                        result = pool.apply(execute_command, (command,))
                    
                    print(f"Result: {result}")
                except ValueError as e:
                    print(f"Error: {e}")
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
