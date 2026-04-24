# Project Planner

Project Name:
Student Record Management System

Problem Statement:
Many schools, tutors, and small training centers need a simple way to store and manage student information. Manual record handling can be slow and confusing, especially when searching, updating, and deleting student details.

Objective:
Build a basic Python command-line application that allows users to manage student records in an organized way.

## Features
- Add a student
- View all students
- Search for a student
- Update student details
- Delete a student
- Save records to a file

## Functions
- `show_menu()`
- `load_students()`
- `save_students(students)`
- `add_student(students)`
- `view_all_students(students)`
- `search_student(students)`
- `update_student(students)`
- `delete_student(students)`

To-Do:
- [x] Plan project
- [x] Create menu
- [x] Build features
- [x] Test program
- [ ] Fix bugs
- [x] Final review

Progress Notes:
- Completed 3-step development flow:
  - Step 1: Project structure and menu skeleton
  - Step 2: Full CRUD logic (in-memory)
  - Step 3: JSON file persistence in `data/students.json`

Problems and Fixes:
- Problem: Data was lost after closing the program in Step 2.
- Fix: Added JSON storage with auto-create logic in Step 3.

Future Improvements:
- Add input validation for email and phone format
- Add sorting and filtering options
- Add export to CSV
- Add basic authentication for admin access
