import pytest

from my_computer.memory import Memory


def test_memory_initialization():
    """Check that memory right size."""
    memory = Memory(4)

    assert memory.get_memory_size() == 4
    assert memory.read_memory() == bytearray(b"\x00\x00\x00\x00")


def test_get_size():
    """Check get size function."""
    memory = Memory(4)

    assert memory.get_memory_size() == 4


def test_get_memory():
    """Memory cell should return right value."""
    memory = Memory(4)

    assert memory.read_memory_index(0) == 0
    assert memory.read_memory_index(3) == 0


def test_write_memory():
    """Memory should write right value."""
    memory = Memory(4)

    memory.write_value(7, 2)
    assert memory.read_memory_index(2) == 7


def test_error_memory_index():
    """Memory cell should raise error if index is wrong."""
    memory = Memory(4)

    with pytest.raises(ValueError, match="Wrong memory index"):
        memory.read_memory_index(-1)

    with pytest.raises(ValueError, match="Wrong memory index"):
        memory.read_memory_index(4)


def test_error_memory_write_value():
    """Memory cell should raise error if value is wrong."""
    memory = Memory(4)

    with pytest.raises(ValueError, match="Wrong memory value"):
        memory.write_value(-1, 3)

    with pytest.raises(ValueError, match="Wrong memory value"):
        memory.write_value(256, 3)


def test_memory_write_value():
    """Memory cell should save value."""
    memory = Memory(4)

    memory.write_value(0, 0)
    assert memory.read_memory_index(0) == 0

    memory.write_value(255, 3)
    assert memory.read_memory_index(3) == 255


def test_error_memory_write_index():
    """Memory cell should raise error if index is wrong."""
    memory = Memory(4)

    with pytest.raises(ValueError, match="Wrong memory index"):
        memory.write_value(1, 4)

    with pytest.raises(ValueError, match="Wrong memory index"):
        memory.write_value(1, -1)


def test_memory_not_append():
    """Memory should not append new memory cells."""
    memory = Memory(4)
    memory_data = memory.read_memory()

    assert memory.get_memory_size() == 4

    memory_data.append(1)

    assert memory.get_memory_size() == 4
