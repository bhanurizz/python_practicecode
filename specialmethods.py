class student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks
    def __str__(self):
        return f"name: {self.name}, roll: {self.roll}, marks: {self.marks}"
    def __eq__(self, other):
        if isinstance (other, student):
            return self.roll == other.roll
            return False

S1 = student ("rahul", 101, 90)
S2 = student ("rahul", 101, 90)
S3 = student ("riya", 102, 90)

print (S1)
print (repr(S1))
print (S1 == S2)
print (S1 == S3)