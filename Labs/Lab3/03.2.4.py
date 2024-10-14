year: int = int(input("Enter a year above 1582 : "))

if(year <= 1582):
    raise ValueError(f"{year} must be higher than 1582")

if(year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)):
    print(f"{year} è bisestile")
else:
    print(f"{year} non è bisestile")    