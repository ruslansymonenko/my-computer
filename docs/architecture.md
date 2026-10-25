# Architecture

The system is a Python application that *simulates* a computer. It does not boot on hardware. Each layer is introduced only when earlier layers make it useful.

```text
Later: shell / display / user programs
             | commands and input/output
Later: kernel-like runtime (loader, processes, syscalls)
             | runs programs and manages devices
Later: virtual disk and filesystem
             | persists bytes and paths
Language compiler -> assembler -> machine-code bytes
                                  |
Now:                        virtual CPU <-> RAM
```

The arrows describe eventual interactions, not modules that already exist. The first milestone uses handwritten bytecode, RAM, and a CPU. A tiny program will load into memory and run one instruction at a time until it halts. This gives a working base before source languages or operating-system features are added.

## First milestone boundaries

- **Memory** owns a fixed set of addressable bytes. Reading and writing an invalid address must fail clearly.
- **Initial memory contents:** Every cell starts at 0. A cell stores one integer from 0 to 255; writing a value outside that range must fail clearly.
- **CPU** owns execution state such as a program counter, accumulator/registers, and a halted flag. It reads instruction bytes from memory, decodes them, changes state, and advances or changes the program counter.
- **Program loader** copies bytecode into a chosen memory range and initializes the starting program counter. It does not assemble source text.
- **Instruction set** is a small, documented contract between programs and the CPU: opcode values, operand lengths, effects, and invalid-opcode behavior. Define it as the related exercises arrive.

A small 8-bit machine is a useful starting direction: byte values are 0–255, with a small fixed RAM and a few instructions. The exact memory size, register set, and instruction encoding are decisions for the learner during Stage 1. Once chosen, document them before writing programs or tests that depend on them.

## Later layers and boundaries

- **Assembler:** transforms text instructions and labels into the CPU's bytecode. It does not execute instructions.
- **Language compiler:** turns a small source language into assembly or bytecode. Its lexer, parser, and code generation are handwritten learning exercises.
- **Virtual disk/filesystem:** stores bytes in a host file and gives them virtual file and directory names. A file's bytes are distinct from host filesystem paths.
- **Kernel-like runtime:** loads programs, tracks process state, schedules execution, and handles system calls. Programs request services through a defined interface.
- **Shell:** accepts user commands and asks the runtime or filesystem to perform them.
- **Display/input:** present a framebuffer and input events through runtime-managed devices after text-based execution works.

These boundaries can change when implementation reveals a better design. Avoid building abstractions solely for a future layer. Keep ordinary Python objects for the simulator; Python itself supplies the real process, memory safety, and host I/O.
