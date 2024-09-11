class Student:
    def _init_(self, name, age, student_id, major):
        self.name = Kevin Kivuna         # Name of the student 
        self.age = 22           # Age of the student
        self.student_id = b20246  # Unique ID for the student
        self.major = Computer Science        # Major subject of study 
        
        #methods of display
        print("name:", self.name)
        print("age:", self.age)
        print("student_id:", self.student_id)
        print("major:", self.major)

        #methods to display what a student is studying

    def study(self):
        return f"{self.name} is studying {self.major}."