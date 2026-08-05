class Calcuator:
    def add(self, a, b=0):
        return a+b
c = Calcuator()
print(c.add(10))
print(c.add(10, 20))