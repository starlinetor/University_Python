from ast import Raise


grade: float = float(input("Grade : "))

grades: dict[float : str] = {
    4.0 : "A" ,
    3.7 : "A-",
    3.3 : "B+",
    3.0 : "B" ,
    2.7 : "B-", 
    2.3 : "C+",
    2.0 : "C" ,
    1.7 : "C-",
    1.3 : "D+",
    1.0 : "D" ,
    0.7 : "D-",
    0.4 : "F" ,
}

if(not (0.0<=grade<=4.0)):
    raise ValueError(f"Grade : {grade} needs to be between 0 and 4")

closest_grade: float
smallest_distance: float = 10

for value in grades.keys():
    distance = abs(value - grade)
    if(distance < smallest_distance):
        smallest_distance = distance
        closest_grade = value

print(grades[closest_grade])




