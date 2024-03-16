class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class CustomCar(Vehicle):
    def __init__(self, make, model, year,number_of_tires):
        super().__init__(make, model, year)
        self.number_of_tires = number_of_tires


toyota = Vehicle('Toyota', 'Corolla', 2019)
rukururana = CustomCar({'Toyota', 'Mercedes'},{ 'Carina', 'Benz'}, {2019, 2021}, {4, 8})
print(rukururana.make, rukururana.model) 


