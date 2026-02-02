---
name: commit
description: Commit and push a solved LeetCode problem
argument-hint: <number>
user-invocable: true
---

# Commit and push LeetCode problem $ARGUMENTS[0]

## Instructions

1. Run `ruff format .` to format all code.
2. Stage all changes with `git add -A`.
3. Commit with the message `Problem $ARGUMENTS[0]`.
4. Push with `git push`.
