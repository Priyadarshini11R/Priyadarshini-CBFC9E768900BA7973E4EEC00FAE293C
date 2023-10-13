class Student:
  def __init__(self, name, roll_number, cgpa):
      self.name = name
      self.roll_number = roll_number
      self.cgpa = cgpa

def sort_students(student_list):
  # Sort the student list based on CGPA in descending order
  sorted_students = sorted(student_list, key=lambda x: x.cgpa, reverse=True)
  return sorted_students

# Example usage:
if __name__ == "__main__":
  # Create a list of student objects
  students = [
      Student("Alice", "A001", 3.9),
      Student("Bob", "A002", 3.7),
      Student("Charlie", "A003", 3.5),
      # Add more students as needed
  ]

  # Display the original list of students
  print("Original List of Students:")
  for student in students:
      print(f"{student.name} ({student.roll_number}): CGPA - {student.cgpa}")

  # Sort the list of students based on CGPA
  sorted_students = sort_students(students)

  # Display the sorted list of students
  print("\nSorted List of Students (based on CGPA in descending order):")
  for student in sorted_students:
      print(f"{student.name} ({student.roll_number}): CGPA - {student.cgpa}")
