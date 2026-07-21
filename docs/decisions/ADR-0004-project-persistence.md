# ADR 0004: Separation of Project Domain Logic and Persistence Repository

## Status
Accepted

## Context
As project storage requirements evolve, mixing file IO operations (JSON/SQLite disk access) with core domain logic creates rigid coupling and complicates unit testing.

## Decision
adopted the Repository Pattern by separating storage mechanics into a dedicated `ProjectRepository` layer, while business logic resides exclusively in `ProjectService`.

## Consequences
* Enables isolated unit testing of file IO routines independently from application workflow logic.
* Allows future persistence format migrations (e.g., from JSON to SQLite or binary `.mbproj` archives) without altering service layer contracts.