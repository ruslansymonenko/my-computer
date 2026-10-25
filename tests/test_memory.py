import pytest
from src.my_computer.memory import Memory


def test_memory_initialization():
    """Check that memory right size."""
    memory = Memory(4)

    assert len(memory.shared_storage) == 4
    assert memory.shared_storage == bytearray(b"\x00\x00\x00\x00")


def test_get_size():
    """Check get size function."""
    memory = Memory(4)

    assert memory.get_memory_size() == 4


def test_get_memory_cell():
    """Memory cell should return right value."""
    memory = Memory(4)

    assert memory.get_memory_cell(0) == 0
    assert memory.get_memory_cell(3) == 0


def test_error_memory_cell():
    """Memory cell should raise error if value is wrong."""
    memory = Memory(4)

    with pytest.raises(ValueError, match="Wrong memory value"):
        memory.get_memory_cell(-1)

    with pytest.raises(ValueError, match="Wrong memory value"):
        memory.get_memory_cell(4)
