print("--------- WELCOME TO AIRPORT STATION ----------")
#Name
first_name="Arul"
last_name="Balaji"
print(f"Welcome sir your Full name {first_name} {last_name}")
#Security_checking
print("Security verified / Not verified")
travelor=input("Enter you status:").lower().strip()
if travelor=='verified':
    print("you are allowed")
else:
    print("Sorry! you are not allowed ")
#covid_19_check
print("---------- COVID 19 CHECK ----------")
print("Type you covid result positive / negative")
covid_check=input("Enter you status:").strip()
if covid_check=='negative':
    print("You are allowed to Travel")
else:
    print("sorry sir!, You are not allowed to Travel") 
#Immegration_checking 
print("---------- IMMEGRATION CHECKING ----------")
immegration_checking=input("Enter the ID proof name:").strip()
if immegration_checking=='covid report' or immegration_checking=='lisence' or immegration_checking=='aadhar' or immegration_checking=='passport' or immegration_checking=='visa':
    if immegration_checking=='covid report':
        print("Verified")
    if immegration_checking=='lisence':
        print("Verified")
    if immegration_checking=='aadhar':
        print("Verified")
    if immegration_checking=='passport':
        print("Verified")
    if immegration_checking=='visa':
        print("Verified")
else:
    print("Sorry! you are Not allowed")
#Bag_checking
print("---------- CHECK YOUR BAG WEIGHT ----------")
Bag_weight_check=int(input("Enter your Bag weight:"))
if Bag_weight_check<=20:
    print("your allowed")
else:
    print("you have to pay extra money for extra kg")                
#Boarding pass
print("---------- BOARDING APPROVE ----------")
Boarding_approve=input("Enter your Boaring status:").strip()
if Boarding_approve=='yes':
    print("you are approved")
else:
    print("you are not allowed")        
print("---------- ENJOY YOUR TRAVEL SIR ----------")    