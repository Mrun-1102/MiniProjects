#Initiallising dictionary
stud_grades = {}

#Add new element
def add_student(name,grade):
    stud_grades[name]= grade
    #[sagar]=200
    print(f"Added {name} with a {grade}")

#update a student
def update_student(name, grade):
    if name in stud_grades:
        print(stud_grades(name))
        stud_grades[name]=grade
        print(f"{name}'s marks are updated to {grade}")
     
    else:
        print(f"{name} not found!")


#Delete a student
def delete_student(name):
    if name in stud_grades:
        del stud_grades[name]
        print(f"{name} has been successfully deleted")
    else:
        print(f"{name} is not found!")

#View all student data
def display_all():
    if stud_grades:
        for name, grade in stud_grades.items():
            print(f"{name} : {grade}")
    
    else:
        print("No student found/added.")

def main():
    while True:
        print("\n Student Grades Management System")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View Student")
        print("5. Exit")

        choice = int(input("Enter your choice = "))
        if choice ==1:
            name = input("Enter student name = ")
            grade = int(input("Enter student grade = "))
            add_student(name, grade)
        
        elif choice == 2:
            name = input("Enter student name = ")
            grade = int(input("Enter student grade = "))
            update_student(name, grade)

        elif choice == 3:
            name = input("Enter student name = ")
            delete_student(name)

        elif choice == 4:
            display_all()

        elif choice == 5:
            print("Closing the program.....")
            break

        else:
            print("Invalid Choice!!")

if __name__ == "__main__":
    main()

