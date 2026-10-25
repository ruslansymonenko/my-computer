class Memory:
    shared_storage: bytearray

    def __init__(self, cells: int) -> None:
        self.shared_storage = bytearray(cells)

    def get_memory_size(self) -> int:
        return len(self.shared_storage)

    def get_memory_cell(self, index: int) -> int:
        if (
            index > self.get_memory_size()
            or index < 0
            or index == self.get_memory_size()
        ):
            raise ValueError("Wrong memory value")

        if self.shared_storage is not None:
            return self.shared_storage[index]

        raise ValueError("Memory not initialized")
