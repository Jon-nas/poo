class student:
    school = "DIO"

    def __init__(self, name, enrollment):
        self.name = name
        self.enrollment = enrollment

    def __str__(self):
        return f"{self.name} - {self.enrollment} - {self.school}"
    
def show_values(*objects):
    for obj in objects:
        print(obj)
    
s1 = student("Sheldon", 1)
s2 = student("Amy", 2)
show_values(s1, s2)

student.school = "Call Tech"
s3 = student("Leonard", 3)
show_values(s1, s2, s3)