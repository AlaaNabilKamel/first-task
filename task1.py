students = {}

while True:
    name = input("Enter student name (or 'done' to finish): ")
    if name.lower() == 'done':
        break
    grade = input(f"Enter {name}'s grade: ")
    students[name] = int(grade) if grade.isdigit() else 0

if students:
    print("\nClass Performance Report")
    print(f"Total Students: {len(students)}")
    print(f"Average Grade: {sum(students.values()) / len(students):.2f}")
    print(f"Highest: {max(students, key=students.get)} ({max(students.values())})")
    print(f"Lowest: {min(students, key=students.get)} ({min(students.values())})")
    print("\nPerformance:")
    for s, g in students.items():
        print(f"{s}: {g} ({'Excellent' if g >= 90 else 'Good' if g >= 75 else 'Needs Improvement'})")
