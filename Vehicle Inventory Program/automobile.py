#automobile

class automobile:
    def __init__(self, make, model, color, year, mileage):
        self.mileage = mileage
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        
        
    def tostring(self):
        print("Vehicle is")
        print("Model : " + self.model)
        
        print("Make : " + self.make)
        print("Color : " + self.color)
        print("Year : " + self.year)
        print("Mileage : " + self.mileage)
        
        
        
        
        