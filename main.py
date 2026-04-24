def input_non_empty(prompt, default=None):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        if default is not None:
            return default
        print("Value cannot be empty.")


def input_positive_int(prompt, default=None):
    while True:
        value = input(prompt).strip()
        if value == "" and default is not None:
            return default
        if value.isdigit() and int(value) > 0:
            return int(value)
        print("Please enter a valid positive number.")


def get_next_student_id(students):
    return max((student["id"] for student in students), default=0) + 1


def find_student_by_id(students, student_id):
    for student in students:
        if student["id"] == student_id:
            return student
    return None


def print_student(student):
    print("-" * 36)
    print(f'ID    : {student["id"]}')
    print(f'Name  : {student["name"]}')
    print(f'Age   : {student["age"]}')
    print(f'Grade : {student["grade"]}')
    print(f'Email : {student["email"]}')
    print(f'Phone : {student["phone"]}')
    print("-" * 36)


def add_student(students):
    student = {
        "id": get_next_student_id(students),
        "name": input_non_empty("Name: "),
        "age": input_positive_int("Age: "),
        "grade": input_non_empty("Grade/Class: "),
        "email": input_non_empty("Email: "),
        "phone": input_non_empty("Phone: "),
    }
    students.append(student)
    print("Student added successfully.")


def view_all_students(students):
    if not students:
        print("No student records found.")
        return

    for student in sorted(students, key=lambda item: item["id"]):
        print_student(student)


def search_student(students):
    if not students:
        print("No student records found.")
        return

    query = input("Enter student ID or name: ").strip()
    if not query:
        print("Search value cannot be empty.")
        return

    if query.isdigit():
        matches = [student for student in students if student["id"] == int(query)]
    else:
        query_lower = query.lower()
        matches = [
            student
            for student in students
            if query_lower in student["name"].lower()
        ]

    if not matches:
        print("No matching student found.")
        return

    for student in matches:
        print_student(student)


def update_student(students):
    if not students:
        print("No student records found.")
        return

    student_id = input_positive_int("Enter student ID to update: ")
    student = find_student_by_id(students, student_id)
    if student is None:
        print("Student not found.")
        return

    print("Press Enter to keep current values.")
    student["name"] = input_non_empty(f'Name [{student["name"]}]: ', student["name"])
    student["age"] = input_positive_int(f'Age [{student["age"]}]: ', student["age"])
    student["grade"] = input_non_empty(f'Grade/Class [{student["grade"]}]: ', student["grade"])
    student["email"] = input_non_empty(f'Email [{student["email"]}]: ', student["email"])
    student["phone"] = input_non_empty(f'Phone [{student["phone"]}]: ', student["phone"])

    print("Student updated successfully.")


def delete_student(students):
    if not students:
        print("No student records found.")
        return

    student_id = input_positive_int("Enter student ID to delete: ")
    student = find_student_by_id(students, student_id)
    if student is None:
        print("Student not found.")
        return

    confirm = input(f'Delete {student["name"]}? (y/n): ').strip().lower()
    if confirm != "y":
        print("Delete cancelled.")
        return

    students.remove(student)
    print("Student deleted successfully.")


def show_menu():
    print("\nStudent Record Management System")
    print("1. Add student")
    print("2. View all students")
    print("3. Search for a student")
    print("4. Update student details")
    print("5. Delete a student")
    print("6. Save records to file")
    print("7. Exit")


def main():
    students = []

    while True:
        show_menu()
        choice = input("Choose an option (1-7): ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_all_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            print("In-memory version. File save will be added in next commit.")
        elif choice == "7":
            print("Goodbye.")
            break
        else:
            print("Invalid option. Please choose from 1 to 7.")


if __name__ == "__main__":
    main()