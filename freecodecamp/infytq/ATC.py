#Calculate the number of flights remaining on the airport
initial_flights= 100
takeoff=int(input("Enter the no. of Flights that took off:"))
arrival=int(input("Enter the no. of Flights that arrived:"))
remaining_flight= ((initial_flights+arrival)-takeoff)
print("No. of Flights remaining on the airport",remaining_flight)
