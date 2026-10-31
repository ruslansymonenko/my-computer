class Memory:
    _storage: bytearray

    def __init__(self, cells: int) -> None:
        self._storage = bytearray(cells)

    def get_memory_size(self) -> int:
        return len(self._storage)

    def check_memory_index(self, index: int) -> None:
        if index >= self.get_memory_size() or index < 0:
            raise ValueError("Wrong memory index")

    def read_memory_index(self, index: int) -> int:
        self.check_memory_index(index)

        if self._storage is not None:
            return self._storage[index]

        raise ValueError("Memory not initialized")

    def read_memory(self) -> bytearray:
        if self._storage is not None:
            return self._storage.copy()

        raise ValueError("Memory not initialized")

    def write_value(self, value: int, index: int) -> None:
        self.check_memory_index(index)

        if value < 0 or value > 255:
            raise ValueError("Wrong memory value")

        if self._storage is not None:
            self._storage[index] = value
