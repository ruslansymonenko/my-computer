# Roadmap

This order is a learning path, not a fixed specification. Finish and review one task before moving to the next. Split a task if it exposes too many new ideas. Record chosen machine details in `architecture.md` and the current state in `progress.md`.

## Stage 1 — A bytecode program runs

**Milestone:** A small program represented directly as bytes is loaded into RAM and executed one instruction at a time until it halts. No assembler, filesystem, process scheduler, or display is needed.

### 1.1 Fixed-size memory

- **Objective:** Create an object that stores a fixed number of addressable bytes.
- **Why:** The CPU needs RAM for instructions and, later, data.
- **Expected behavior:** Read and write one address; reject invalid addresses and non-byte values clearly.
- **Acceptance:** Tests cover first and last addresses, an ordinary read/write, an out-of-range address, and an invalid value; capacity cannot change after creation.
- **Study:** `bytearray`, indexing, invariants, exceptions, boundary tests.
- **Hint:** Begin by deciding what state the object owns and which operations callers need.
- **Depends on:** Repository setup only.

### 1.2 Load a sequence of bytes

- **Objective:** Copy a small program into memory at a chosen starting address.
- **Why:** Programs need a reproducible way to enter RAM.
- **Expected behavior:** Bytes appear in order; a program that does not fit is rejected without partial writes.
- **Acceptance:** Tests cover a successful load, an exact fit, and an oversized load with memory unchanged.
- **Study:** Iteration, ranges, preconditions, atomicity at this small scale.
- **Hint:** Check the whole destination range before writing the first byte.
- **Depends on:** 1.1.

### 1.3 CPU state

- **Objective:** Define a minimal CPU state, including a program counter and halted state; choose one data register if the first instructions need it.
- **Why:** Execution needs a place to remember where it is and what it has computed.
- **Expected behavior:** Initial state is documented and can be inspected; reset returns to it.
- **Acceptance:** Tests show the initial and reset states; register and counter ranges follow the chosen machine size.
- **Study:** State, object invariants, registers versus RAM.
- **Hint:** Write down what must persist between two instruction steps.
- **Depends on:** 1.1.

### 1.4 Instruction encoding

- **Objective:** Choose and document the smallest useful bytecode: at least `HALT`, a way to put a byte in a register, and one observable state change.
- **Why:** The CPU and handwritten programs need a shared contract.
- **Expected behavior:** Each instruction has an opcode, length, operand meaning, and stated behavior for unknown or incomplete instructions.
- **Acceptance:** A small instruction table in `architecture.md` lets someone decode a sample byte sequence by hand.
- **Study:** Opcodes, operands, binary representation, tradeoffs of instruction length.
- **Hint:** Keep the first set tiny; add arithmetic and jumps only when the basic loop works.
- **Depends on:** 1.3.

### 1.5 Fetch and decode one instruction

- **Objective:** Read the opcode and any operands at the program counter, then identify the instruction.
- **Why:** This is the bridge from stored bytes to machine actions.
- **Expected behavior:** Valid bytes decode consistently; invalid or truncated instructions fail clearly.
- **Acceptance:** Focused tests cover each first opcode and both error cases; the program counter behavior is documented.
- **Study:** Fetch/decode cycle, bounds, error design.
- **Hint:** Trace the counter on paper for a one-byte and a multi-byte instruction.
- **Depends on:** 1.2, 1.4.

### 1.6 Execute one step

- **Objective:** Make one CPU step apply one decoded instruction to state.
- **Why:** Small steps make execution observable and testable.
- **Expected behavior:** A normal instruction changes only its specified state; `HALT` stops further execution.
- **Acceptance:** Tests show state before and after each first instruction and verify that stepping after halt has a documented result.
- **Study:** State transitions, side effects, test isolation.
- **Hint:** State the before/after effect of each instruction before coding it.
- **Depends on:** 1.5.

### 1.7 Run a complete tiny program

- **Objective:** Repeatedly step a loaded handwritten byte sequence until halt.
- **Why:** This joins memory, loading, and CPU behavior into the first visible result.
- **Expected behavior:** A tiny program produces a predictable final register or memory value and halts; invalid programs report an error.
- **Acceptance:** One integration test loads and runs a byte sequence, checks its final state, and confirms an explicit halt. README gains an actual run command or reproducible invocation.
- **Study:** Execution loops, integration tests, termination.
- **Hint:** Keep the first program short enough to trace on paper.
- **Depends on:** 1.6.

## Stage 2 — Make the CPU useful

### 2.1 Arithmetic and flags

- **Objective:** Add one arithmetic instruction and the minimum status flag it needs.
- **Why:** Programs need to compute and inspect outcomes.
- **Expected behavior:** Results obey the chosen byte-width rule; flags update exactly when specified.
- **Acceptance:** Tests cover normal arithmetic, a boundary result, and flag changes; behavior is documented.
- **Study:** Fixed-width integers, overflow, status flags.
- **Hint:** Decide whether arithmetic wraps before implementing it.
- **Depends on:** 1.7.

### 2.2 Branching

- **Objective:** Add an unconditional jump and one conditional jump.
- **Why:** Programs need choices and loops.
- **Expected behavior:** Taken jumps change the program counter; untaken jumps continue normally; invalid targets fail clearly.
- **Acceptance:** Tests exercise both branch outcomes and a short terminating loop.
- **Study:** Control flow, absolute versus relative addresses, loop invariants.
- **Hint:** Trace the counter after each byte consumed.
- **Depends on:** 2.1.

### 2.3 Stack basics

- **Objective:** Add a stack pointer and push/pop operations.
- **Why:** A stack will later support calls and temporary values.
- **Expected behavior:** Values round-trip in last-in-first-out order; overflow and underflow are explicit errors.
- **Acceptance:** Tests cover ordering, boundaries, and interaction with RAM layout.
- **Study:** Stacks, memory regions, pointer movement.
- **Hint:** Draw the stack's valid address range before choosing its growth direction.
- **Depends on:** 2.2.

## Stage 3 — Write assembly instead of raw bytes

### 3.1 Parse one instruction line

- **Objective:** Translate a single textual instruction and operand into bytes.
- **Why:** Handwriting opcodes becomes error-prone as programs grow.
- **Expected behavior:** Valid lines encode correctly; unknown mnemonics and bad operands have useful errors.
- **Acceptance:** Tests cover every supported mnemonic and representative errors.
- **Study:** Tokenization, numeric formats, error locations.
- **Hint:** Reuse the instruction table as the source of truth.
- **Depends on:** Stage 2 instruction contract.

### 3.2 Assemble multiple lines and labels

- **Objective:** Resolve named jump targets across a whole program.
- **Why:** Labels make branches readable despite changing byte offsets.
- **Expected behavior:** Forward and backward labels resolve; duplicate or missing labels fail clearly.
- **Acceptance:** Tests assemble and execute a small labeled loop.
- **Study:** Symbol tables, two-pass translation, address calculation.
- **Hint:** Consider what must be known before a forward jump can be encoded.
- **Depends on:** 3.1, 2.2.

### 3.3 Constants and diagnostics

- **Objective:** Add named constants and source-line error reporting.
- **Why:** Repeated numeric values and opaque errors slow experimentation.
- **Expected behavior:** Constants substitute predictably; malformed declarations report their line.
- **Acceptance:** Tests cover reuse, redefinition, unknown names, and line numbers.
- **Study:** Namespaces, source locations, validation.
- **Hint:** Keep constants distinct from address labels in your model.
- **Depends on:** 3.2.

## Stage 4 — A small programming language

### 4.1 Expressions and lexer

- **Objective:** Define a tiny expression grammar and turn source text into tokens.
- **Why:** A language needs structured input before it can compile.
- **Expected behavior:** Numbers, names, and operators tokenize; invalid characters report positions.
- **Acceptance:** Tests cover whitespace, representative expressions, and bad characters.
- **Study:** Tokens, grammar, lexical errors.
- **Hint:** Specify a few sample expressions before adding syntax.
- **Depends on:** 3.2.

### 4.2 Parser and AST

- **Objective:** Parse expressions into a small syntax tree with clear precedence.
- **Why:** Structure is needed to preserve meaning during compilation.
- **Expected behavior:** The tree distinguishes grouped and ungrouped expressions; bad syntax reports a location.
- **Acceptance:** Tests show expected tree shapes and syntax errors.
- **Study:** Recursive descent, precedence, tree structures.
- **Hint:** Start with literals and one binary operator.
- **Depends on:** 4.1.

### 4.3 Variables and code generation

- **Objective:** Compile assignments and expressions into assembly or bytecode.
- **Why:** This connects a high-level statement to CPU operations.
- **Expected behavior:** A small source program computes a value observable in machine state.
- **Acceptance:** End-to-end test compiles and runs one assignment plus expression; undefined names fail clearly.
- **Study:** Symbol tables, storage allocation, code generation.
- **Hint:** Decide where each variable lives before emitting instructions.
- **Depends on:** 4.2 and suitable CPU operations.

### 4.4 Conditions and loops

- **Objective:** Compile a simple conditional and loop.
- **Why:** These show how structured control flow becomes jumps.
- **Expected behavior:** Both branches and a terminating loop run correctly.
- **Acceptance:** End-to-end tests cover true/false paths and repeated execution.
- **Study:** Control-flow lowering, labels, termination.
- **Hint:** Sketch the equivalent assembly jump structure first.
- **Depends on:** 4.3, 2.2.

### 4.5 Functions and simple collections

- **Objective:** Add calls and returns, then a small indexed data structure if memory design supports it.
- **Why:** These motivate stack frames and address calculations.
- **Expected behavior:** Calls restore control flow; collection access checks its valid range.
- **Acceptance:** Tests cover nested calls, return values, and an out-of-range access. Split this task before starting if it feels large.
- **Study:** Calling conventions, stack frames, indexing.
- **Hint:** Define the calling convention on paper first.
- **Depends on:** 4.4, 2.3.

## Stage 5 — Persistent virtual files

### 5.1 Block-backed virtual disk

- **Objective:** Store fixed-size virtual blocks inside one host file.
- **Why:** Programs and data should survive a simulator restart.
- **Expected behavior:** A block can be read or replaced; invalid block numbers fail.
- **Acceptance:** Tests reopen the disk and recover written bytes, including boundary blocks.
- **Study:** Binary files, offsets, persistence, block size.
- **Hint:** Decide the exact disk size and block size before writing.
- **Depends on:** Stage 1; may be learned independently after that.

### 5.2 Allocation and file metadata

- **Objective:** Track which blocks belong to a file and its byte length.
- **Why:** Files need identities and space ownership.
- **Expected behavior:** Creating, extending, and reading a file uses allocated blocks without overlap.
- **Acceptance:** Tests cover an empty file, a multi-block file, full disk, and reopen.
- **Study:** Allocation maps, metadata, serialization.
- **Hint:** Start with a deliberately limited file count.
- **Depends on:** 5.1.

### 5.3 Directories and paths

- **Objective:** Map names and simple paths to file metadata.
- **Why:** Users need to find files without knowing block numbers.
- **Expected behavior:** Create, list, resolve, and read named files; reject invalid paths.
- **Acceptance:** Tests cover root, one nested directory, duplicate names, and missing paths.
- **Study:** Trees, path resolution, naming rules.
- **Hint:** Implement one directory level before nesting.
- **Depends on:** 5.2.

## Stage 6 — A kernel-like runtime

### 6.1 Program loading and process state

- **Objective:** Model a loaded program and its CPU state as a process.
- **Why:** The runtime needs a unit to run and stop.
- **Expected behavior:** Loading creates a runnable process; halt moves it to a finished state.
- **Acceptance:** Tests distinguish new, runnable, and finished states without sharing accidental CPU state.
- **Study:** Process control blocks, lifecycle, isolation.
- **Hint:** Record only state the scheduler will actually need.
- **Depends on:** 1.7 and a stable loader.

### 6.2 System calls and I/O

- **Objective:** Give programs a narrow request path for basic output and file access.
- **Why:** Applications should ask the runtime for services instead of calling host APIs directly.
- **Expected behavior:** Known requests work; unknown requests fail predictably; the runtime owns host-facing I/O.
- **Acceptance:** A program makes one output request; tests cover an invalid request.
- **Study:** Privilege boundaries as a model, APIs, device abstraction.
- **Hint:** Start with a single output service.
- **Depends on:** 6.1; file calls also need Stage 5.

### 6.3 Round-robin scheduling

- **Objective:** Share CPU steps across two or more processes using a fixed time slice.
- **Why:** Scheduling demonstrates how one CPU can make multiple programs progress.
- **Expected behavior:** Runnable processes take turns; halted ones leave the queue.
- **Acceptance:** Tests show fair progress and eventual completion of two short programs.
- **Study:** Queues, context switching, time slices.
- **Hint:** First make one process pause and resume correctly.
- **Depends on:** 6.1, 6.2.

### 6.4 Minimal memory isolation

- **Objective:** Prevent one process from reading or writing another process's memory region.
- **Why:** It clarifies what the runtime must protect as programs multiply.
- **Expected behavior:** Legal addresses translate correctly; cross-region access fails.
- **Acceptance:** Tests cover each process's legal range and a forbidden access.
- **Study:** Base/limit addressing, address translation, protection.
- **Hint:** Prefer one simple translation rule to a full paging model.
- **Depends on:** 6.3.

## Stage 7 — Shell and visual output

### 7.1 Basic shell

- **Objective:** Accept commands to list files, change directory, read a file, and launch a program.
- **Why:** It gives the system a usable text interface.
- **Expected behavior:** Commands report results or clear errors without crashing the shell.
- **Acceptance:** Manual walkthrough and focused tests cover `ls`, `cd`, `cat`, and one program launch.
- **Study:** Command loops, parsing, current working directory.
- **Hint:** Split command parsing from command execution.
- **Depends on:** Stages 5 and 6.

### 7.2 Framebuffer and pixels

- **Objective:** Model a small virtual display as addressable pixels.
- **Why:** A visible result makes later programs more tangible.
- **Expected behavior:** Set, clear, and inspect pixels; invalid coordinates fail clearly.
- **Acceptance:** Tests cover corners, an interior pixel, and invalid coordinates; a simple viewer renders the buffer.
- **Study:** 2D indexing, color representation, rendering boundaries.
- **Hint:** Keep the framebuffer independent of the window toolkit.
- **Depends on:** 6.2.

### 7.3 Text and input

- **Objective:** Render a small bitmap font and deliver keyboard input to a program through the runtime.
- **Why:** This connects display and interaction without requiring windows yet.
- **Expected behavior:** Text appears in the framebuffer; input events reach only the intended program.
- **Acceptance:** A demo prints text and responds to a key; tests cover glyph bounds and input delivery.
- **Study:** Glyph bitmaps, event queues, device interfaces.
- **Hint:** Begin with a tiny character set and one input event type.
- **Depends on:** 7.2, 6.2.

### 7.4 Optional UI, piping, and redirection

- **Objective:** Choose one motivating extension after the simpler system works.
- **Why:** Windows, richer graphics, pipes, and redirection each expose different systems ideas.
- **Expected behavior:** Specify the chosen feature's behavior before implementing it.
- **Acceptance:** Add a small demo and tests for the chosen feature; update this roadmap with smaller tasks first.
- **Study:** Depends on the chosen feature.
- **Hint:** Pick the extension that answers a question you now care about.
- **Depends on:** 7.1–7.3 as relevant.
