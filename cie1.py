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
print("car number:",sys.argv[1])
print("owner name:",sys.argv[2)
print("vehicle type:",sys.argv[3])
print("RC expiry year:",sys.argv[4])
