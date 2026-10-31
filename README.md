# My Computer

An educational virtual computer built in Python, one small exercise at a time. 

## Start here

1. Read [the learning guide](docs/learning-guide.md), [architecture](docs/architecture.md), and [roadmap](docs/roadmap.md).
2. Check [progress](docs/progress.md) for the current task.
3. Create a virtual environment and install the development tools:

   ```sh
   python3 -m venv .venv
   source .venv/bin/activate
   python -m pip install -e '.[dev]'
   ```

   On Windows PowerShell, activate with `.venv\Scripts\Activate.ps1`.

4. Implement the current task yourself in `src/my_computer/`, adding focused tests in `tests/` as you go.

## Checks

```sh
ruff format --check .
ruff check .
mypy src
pytest
```

There is no virtual-computer entry point yet. Once the first runnable program exists, its command will be documented here. The package currently contains only an import marker; the first exercise is the memory module.

## Layout

```text
src/my_computer/   Python package; Implementation goes here
tests/             Tests for behavior as exercises are completed
docs/              Architecture, roadmap, learning guide, progress
AGENTS.md          Rules for Codex in this repository
pyproject.toml     Package and tool configuration
```
