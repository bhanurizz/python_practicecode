class Employee:
    def __init__(self, empid, salary):
        self.empid = empid
        self.salary = salary
    def __eq__(self, other):
        return self.empid == other.empid

s1 = Employee ("rahul", 10000)
s2 = Employee ("rahul", 10000)
s3 = Employee ("riya", 15000)

print (s1 == s2)
print (s1 == s3)