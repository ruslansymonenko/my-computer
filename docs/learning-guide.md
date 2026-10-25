# Learning guide

Work on one roadmap task at a time, but divide each task into small steps. Start with a plain-language explanation of the computer concept and one concrete example. Introduce technical terms only after explaining what they mean. Do not assume prior knowledge of computer architecture. Give the learner only the next small step, with its expected result, before moving on.

Ask Codex for a hint when stuck; request pseudocode or code only if the earlier level of help is insufficient. The learner writes the core implementation unless they explicitly ask Codex to write a specific part.

For each task:

1. Understand one small piece of the task through a concrete example; ask about any unfamiliar term.
2. State the expected behavior in your own words and choose a small interface when it becomes relevant.
3. Write the smallest implementation that demonstrates that behavior.
4. Add focused tests for normal and boundary cases. Run the checks in the README.
5. Ask for a review. Discuss mistakes before changing the design.
6. Update `progress.md` with the result and the next step. Codex should maintain this with you after meaningful progress.

A task is complete when its behavior exists, its relevant tests pass, and its important design choices are recorded. Passing checks on an empty package does not complete an exercise.

The roadmap is a guide, not a deadline. If one task is too large, split it. If a concept is unclear, pause for a tiny experiment related to that task. Keep a runnable path through the project whenever possible.
