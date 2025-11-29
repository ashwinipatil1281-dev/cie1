import sys
if len(sys.argv)<4:
   car_number=sys.argv[1]
   owner_name=sys.argv[2]
   vehicle_type=sys.argv[3]
   RC_expiry_year=sys.argv[4]
else:
   car_number=9876
   owner_name="abc"
   vehicle_type="BMW"
   RC_expiry_year=2030
   
print(f"car number: {car_number}")
print(f"owner name: {owner_name}")
print(f"vehicle type: {vehicle_type}")
print(f"RC expiry year: {RC_expiry_year}")
