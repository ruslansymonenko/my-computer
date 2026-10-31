# Progress journal

- **Current stage:** Stage 1 — first bytecode program.
- **Current task:** 1.1 — fixed-size memory.
- **Completed tasks:** Repository preparation only; no virtual-computer exercise is complete.
- **Implementation state:** Storage is instance-owned. Construction, zero initialization, public size, valid boundary reads, invalid boundary reads, ordinary and boundary-value write/read round-trips, invalid boundary writes, and rejection of byte values below 0 and above 255 are covered. `read_memory()` returns an independent copy, and nine tests pass. Direct public access to `storage` still permits changing capacity. No CPU, bytecode, or runner yet.
- **Decisions:** Use Python 3.11+; standard library for educational components; Ruff, mypy, and pytest for development. For memory, new cells start at 0; invalid addresses and values outside 0–255 produce clear errors. Other machine details remain learner decisions during Stage 1.
- **Open bugs/issues:** Public `storage` still lets a caller change fixed capacity with `memory.storage.append(...)`. The initialized `bytearray` also makes the `is not None` branches redundant. Pytest (nine tests), Ruff format/lint, and mypy pass in the project virtual environment.
- **Concepts struggled with:** Distinguishing the capacity of the whole memory from the allowed value in one byte needs clarification.
- **Concepts covered:** Project layers and the first milestone at planning level; the learner implemented and tested that writing 7 at address 2 makes reading address 2 return 7, and that address 4 does not exist in a four-cell memory. The learner chose explicit errors for invalid addresses and values, and confirmed the byte range 0–255. Returning a copy prevents callers from mutating the internal `bytearray` through `read_memory()`. Tests import the installed `my_computer` package and run inside the project virtual environment.
- **Next recommended task:** Rename the internal `storage` attribute to `_storage` throughout `Memory` so callers are clearly directed to the fixed-size public API.
- **Learning preference:** Break exercises into short steps and explain computer concepts in simple language with concrete examples before introducing technical terms.
- **Previous session stop:** Repository scaffold prepared and local virtual environment installed. Package import, Ruff format/check, and mypy passed. Pytest reported zero tests (exit code 5). Learner has not started the memory task.

Update this file after meaningful progress. Keep entries factual and brief; link to an issue or test when detail grows.
