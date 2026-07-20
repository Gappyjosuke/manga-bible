# ADR 0001: Use of src/ Directory Layout

## Status
Accepted

## Context
We need a project structure that scales cleanly, prevents accidental imports of local development modules from the root workspace directory, and ensures the code executes exactly how it would when packaged and distributed.

## Decision
We adopted a dedicated `src/` layout strategy, keeping all core package directories (`src/mangabible/`) isolated from configuration files and deployment scripts at the root level.

## Consequences
* Improves overall test reliability since testing frameworks must import from the built code rather than raw root scripts.
* Adds a small amount of navigation overhead in the file tree, which is easily managed by modern IDEs.