# Feature: Create Project

## Purpose
Allow the user to establish and initialize a new Manga Bible project on disk.

## Inputs
* **Project Name:** String identifier for the project.
* **Project Location:** Target directory path on the local filesystem.

## Outputs
* Root project directory matching the project name.
* A core `.mbproj` manifest file containing JSON metadata.
* Standard internal directory scaffolding (`assets/`, `scenes/`, `build/`).

## Error Handling
* Empty or invalid name strings (e.g., restricted OS characters).
* Non-existent or read-only parent location paths.
* Directory collision if a project folder with the same name already exists.

## Future Extensions
* Template-based project initialization.
* Automatic local Git repository initialization.