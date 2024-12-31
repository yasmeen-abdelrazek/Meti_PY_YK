import os

def input_and_store_grades(filename):
    grades = []
    
    while True:
        subject = input("Enter the subject name (or type 'done' to finish): ")
        if subject.lower() == 'done':
            break
        try:
            grade = float(input(f"Enter the grade for {subject}: "))
            if grade < 0 or grade > 100:
                print("Please enter a grade between 0 and 100.")
                continue
            grades.append((subject, grade))
        except ValueError:
            print("Invalid input. Please enter a numeric grade.")
    
    try:
        with open(filename, 'a') as file:
            for subject, grade in grades:
                file.write(f"{subject},{grade}\n")
        print("Grades successfully stored!")
    except IOError as e:
        print(f"Error while storing grades: {e}")

def calculate_average(filename):
    if not os.path.exists(filename):
        print("No grade data found.")
        return
    
    try:
        with open(filename, 'r') as file:
            grades = []
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 2:
                    try:
                        grade = float(parts[1])
                        grades.append(grade)
                    except ValueError:
                        print(f"Skipping invalid grade entry: {line.strip()}")
            
            if grades:
                average = sum(grades) / len(grades)
                print(f"Average grade: {average:.2f}")
            else:
                print("No valid grades available.")
    except IOError as e:
        print(f"Error while reading grades: {e}")

def main():
    filename = "grades.txt"

    while True:
        print("\nGrade Tracker")
        print("1. Input and Store Grades")
        print("2. Calculate Average Grade")
        print("3. Exit")
        
        try:
            choice = int(input("Choose an option: "))
            if choice == 1:
                input_and_store_grades(filename)
            elif choice == 2:
                calculate_average(filename)
            elif choice == 3:
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number corresponding to the menu option.")

if __name__ == "__main__":
    main()
