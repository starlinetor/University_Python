newCarPrice: float = float(input ("New car price : "))
kmPerYear: float = float(input("Km per year existimate : "))
fuelPrice: float = float(input("Fuel price €/l : "))
efficency: float = float(input("Fuel efficency km/l : "))
usedCarValue: float = float(input("Car resell value after 5 years : "))

totalPrice: float = newCarPrice + (kmPerYear/efficency)*fuelPrice - usedCarValue
#km/(km/l) * €/l = l *  €/l = € 

print(totalPrice)