#dealership

from automobile import automobile

class dealership:
    def __init__(self):
        self.vehicles = []
        
    def add_vehicle(self):
        mileage = input("Please enter the mileage : ")
        make =  input("Please enter the make : ")
        model =  input("Please enter the model : ")
        color =  input("Please enter the color : ")
        year =  input("Please enter the year : ")
        
        v = automobile(make, model, color, year, mileage)
        
        self.vehicles.append(v)
        
        print("vehicle successfully added. \n")
        
    def remove_vehicle(self):
        print("Available vehicles")
        for v in self.vehicles:
            print(v.model)
        
        
        name = input("Please enter the vehicle model you want to remove : ")
        
        i = 0
        while i < len(self.vehicles):
            if (name == self.vehicles[i].model):
                self.vehicles.remove(self.vehicles[i])
                
            i += 1
                
        if i == len(self.vehicles):
            print("No such vehicle found")
            
            
        else:
            print("Vehicle successfully removed")
            
            
        
            
        
    def update_vehicle_attributes(self):
        print("Available vehicles")
        for v in self.vehicles:
            print(v.model)
        
        
        name = input("Please enter the vehicle model you want to update : ")
        
        i = 0
        while i < len(self.vehicles):
            if (name == self.vehicles[i].model):
                
                print(self.vehicles[i].tostring())
                
                mileage = input("Please enter the mileage : ")
                self.vehicles[i].mileage = mileage
                
                make =  input("Please enter the make : ")
                self.vehicles[i].make = make
                
                model =  input("Please enter the model : ")
                self.vehicles[i].model = model
                
                color =  input("Please enter the color : ")
                self.vehicles[i].color = color
                
                year =  input("Please enter the year : ")
                self.vehicles[i].year = year
                
                break
        
        
            i += 1
        
        
        if i == len(self.vehicles):
            print("No such vehicle found")
            
            
        else:
            print("Vehicle attributes successfully updated")
            
            
            
    def display_vehicles(self):
        print("Available vehicles")
        for v in self.vehicles:
            print(v.tostring())
            print("\n")
            
            
            