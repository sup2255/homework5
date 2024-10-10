from main import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

def test_add_command():
    command = AddCommand(2, 3)
    assert command.execute() == 5

def test_subtract_command():
    command = SubtractCommand(5, 3)
    assert command.execute() == 2

def test_multiply_command():
    command = MultiplyCommand(2, 3)
    assert command.execute() == 6

def test_divide_command():
    command = DivideCommand(6, 3)
    assert command.execute() == 2
