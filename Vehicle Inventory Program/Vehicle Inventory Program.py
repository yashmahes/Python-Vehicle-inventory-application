#Vehicle Inventory Program

from dealership import dealership

print("*************************Vehicle Inventory Program******************************")
    
dealer = dealership()

    
while True:
    print("Menu")
    print("1. To add vehicle")
    print("2. To remove vehicle")
    print("3. To update vehicle attributes")
    print("4. To display all vehicles")
    print("0. to quit")
    
    choice = input("Enter choice : ")
    
    if choice == "0":
        break
    
    elif choice == "1":
        dealer.add_vehicle()
        
    elif choice == "2":
        dealer.remove_vehicle()
        
        
    elif choice == "3":
        dealer.update_vehicle_attributes()
        
    elif choice == "4":
        dealer.display_vehicles()
        
    
    else:
        print("Invalid choice! Try again.")
    
    
    
choic = input("Do you want to output all vehicle inventory to a text file. y/n : ")

choic = choic.lower()
if choic == "y":
    
    filename = input("Enter the name of the file : ")
    
    fh = open(filename, "w")
    
    for v in dealer.vehicles:
            fh.write("\n")
            fh.write("Vehicle is")
            fh.write("\n")
            fh.write("Model - " + v.model)
            fh.write("\n")
        
            fh.write("Make - " + v.make)
            fh.write("\n")
            fh.write("Color - " + v.color)
            fh.write("\n")
            fh.write("Year - " + v.year)
            fh.write("\n")
            fh.write("Mileage - " + v.mileage)
            fh.write("\n")
        
    fh.write("end")
    
    fh.close()
    
    
    
    
    
    
    
    

