# ADR 0002: Project-Centric Launch Architecture

## Status
Accepted

## Context
Professional desktop creative tools (like Unreal Engine or modern IDEs) require users to establish or load a specific project environment context before loading the primary production workspace. 

## Decision
We changed the initial application launch behavior to target a "Project Hub" configuration prompt first (New/Open/Recent Projects) rather than launching straight into a blank editor layout window.

## Consequences
* Ensures all asset directories, local paths, and database pipelines are validated before loading complex UI nodes.
* Decouples early development cycles from the heavy main window interface, speeding up fundamental testing modules.