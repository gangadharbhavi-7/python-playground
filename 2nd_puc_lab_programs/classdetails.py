class Student:
    def __init__(self, name, usn):
        # Initialize student details
        self.name = name
        self.usn = usn
        self.marks = []      # list to store marks in 3 subjects
        self.total = 0       # total marks
        self.percentage = 0  # percentage

    def getMarks(self):
        # Read marks for 3 subjects
        for i in range(3):
            mark = int(input(f"Enter marks for subject {i+1}: "))
            self.marks.append(mark)
        # Calculate total and percentage
        self.total = sum(self.marks)
        self.percentage = self.total / len(self.marks)

    def display(self):
        # Display score card details
        print("\n--- Student Score Card ---")
        print("Name       :", self.name)
        print("USN        :", self.usn)
        print("Marks      :", self.marks)
        print("Total      :", self.total)
        print("Percentage :", round(self.percentage, 2), "%")


def main():
    # Read student details
    name = input("Enter student name: ")
    usn = input("Enter student USN: ")

    # Create Student object
    s = Student(name, usn)

    # Get marks and display score card
    s.getMarks()
    s.display()


# Run program
main()