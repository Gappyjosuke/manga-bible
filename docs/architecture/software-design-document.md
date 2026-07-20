# Software Design Document (SDD) - Manga Bible

## 1. System Overview
Manga Bible is an Integrated Development Environment (IDE) for manga production. It provides a structured, multi-panel desktop interface to manage scripts, asset bibles, node setups, and production layouts.

## 2. Interface Dock Layout Philosophy
The workspace uses a full drag-and-drop dock configuration:
* **Left Docks:** Node Palette, Story Editor, Bible Explorer, Prompt Encyclopedia.
* **Center Area:** Node Graph / Active Editor Canvas.
* **Right Docks:** Reference Manager, Asset Library, Camera Library.
* **Bottom Docks:** Output Log, Status Bar.

## 3. Data Pipeline & File Format
* **Project File:** Stored as a structural directory or JSON/SQLite binary using the `.mbproj` file extension.
* **Data Flow:** Story Context -> Scene Configuration -> Page Layout -> Panel Nodes -> Prompt Compiler -> Output Generation -> Project Asset DB.

## 4. UI Standards & Naming Conventions
* **Classes:** UpperCamelCase (e.g., `ProjectManager`, `StoryEditor`).
* **Signals:** lowerCamelCase (e.g., `projectOpened`, `pageGenerated`).
* **Files:** snake_case (e.g., `project_manager.py`, `story_editor.py`). No abbreviations allowed.