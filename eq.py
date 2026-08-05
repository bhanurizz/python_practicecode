class Student:
    def __init__(self, name):
        self.name = name
    def __eq__(self, other):
        return self.name == other.name

s1 = Student ("rahul")
s2 = Student ("rahul")
s3 = Student ("riya")

print (s1 == s2)
print (s1 == s3)