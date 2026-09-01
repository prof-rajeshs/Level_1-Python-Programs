class Student:
    def __init__(self, student_id, maths, science):
        self.student_id = student_id
        self.maths = maths
        self.science = science
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_student(self, student_id, maths, science):
        new_student = Student(student_id, maths, science)

        if self.head is None:
            self.head = new_student
        else:
            current = self.head

            while current.next is not None:
                current = current.next

            current.next = new_student

    def display(self):
        current = self.head

        print("\nStudent Details")
        print("----------------------------")
        print("ID\tMaths\tScience")
        print("----------------------------")

        while current is not None:
            print(current.student_id, "\t", current.maths,
                  "\t", current.science)
            current = current.next


# Main program
students = LinkedList()

while True:
    student_id = int(input("Enter Student ID (-1 to exit): "))

    if student_id == -1:
        break

    maths = int(input("Enter Maths mark: "))
    science = int(input("Enter Science mark: "))

    students.add_student(student_id, maths, science)

students.display()