class car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def __str__(self):
        return f"car(brand = {self.brand}, model = {self.model})"

s = car ("brand = BMW", "model = M3")
print (s)
