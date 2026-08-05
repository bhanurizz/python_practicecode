class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def __str__(self):
        return f"student(Name = {self.name}, marks = {self.marks})"
    def __repr__(self):
        return f"student ('{self.name}', {self.marks})"

s = student ("Rahul", 90)
print (s)
print (repr(s))