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
    while True:
        show_menu()
        choice = input("Choose an option (1-7): ").strip()

        if choice == "7":
            print("Goodbye.")
            break
        elif choice in {"1", "2", "3", "4", "5", "6"}:
            print("This feature will be added in the next commit.")
        else:
            print("Invalid option. Please choose from 1 to 7.")


if __name__ == "__main__":
    main()