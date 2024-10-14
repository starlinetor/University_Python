month: int = int(input("Month : "))
day: int = int(input("Day : "))
season : str = ""

if(not ( 1 <= month <= 12 and 1 <= day <= 31 )): 
    raise ValueError (f"Month : {month} needs to be between 1 and 12\n\
                        Day : {day} needs to be between 1 and 31")

if(1 <= month <= 3):
    season = "Winter"
elif(4 <= month <= 6):
    season = "Spring"
elif(7 <= month <= 9):
    season = "Summer"
elif(10 <= month <= 12):
    season = "Fall"

if(month % 3 == 0 and day >= 21):
    if(season == "Winter"): 
        season = "Spring"
    elif(season == "Spring"):
        season = "Summer"
    elif(season == "Summer"):
        season = "Fall"
    else:
        season = "Winter" 

print(season)