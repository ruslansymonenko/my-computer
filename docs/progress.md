# Progress journal

- **Current stage:** Stage 1 — first bytecode program.
- **Current task:** 1.1 — fixed-size memory.
- **Completed tasks:** Repository preparation only; no virtual-computer exercise is complete.
- **Implementation state:** Storage is instance-owned. Construction, zero initialization, public size, valid boundary reads, and invalid boundary reads are covered by four passing tests. No write operation, CPU, bytecode, or runner yet.
- **Decisions:** Use Python 3.11+; standard library for educational components; Ruff, mypy, and pytest for development. For memory, new cells start at 0; invalid addresses and values outside 0–255 produce clear errors. Other machine details remain learner decisions during Stage 1.
- **Open bugs/issues:** The now-unconditional bytearray makes the `is not None` branch in `get_memory_cell()` redundant. The upper-bound condition works but expresses `index >= size` as two separate comparisons. These are cleanup items rather than behavior failures. Pytest (four tests), Ruff format/lint, and mypy pass.
- **Concepts struggled with:** Distinguishing the capacity of the whole memory from the allowed value in one byte needs clarification.
- **Concepts covered:** Project layers and the first milestone at planning level; the learner correctly identified that writing 7 at address 2 makes reading address 2 return 7, and that address 4 does not exist in a four-cell memory. The learner chose an explicit error for both reading and writing a nonexistent address. The learner confirmed that 0 and 255 are valid byte values, while -1 and 256 must raise an error.
- **Next recommended task:** Add the smallest write operation: write one valid byte to one valid address, then test that reading the same address returns it. Defer invalid values and invalid write addresses to separate steps.
- **Learning preference:** Break exercises into short steps and explain computer concepts in simple language with concrete examples before introducing technical terms.
- **Previous session stop:** Repository scaffold prepared and local virtual environment installed. Package import, Ruff format/check, and mypy passed. Pytest reported zero tests (exit code 5). Learner has not started the memory task.

Update this file after meaningful progress. Keep entries factual and brief; link to an issue or test when detail grows.
