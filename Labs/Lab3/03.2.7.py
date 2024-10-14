#starting units
from pickletools import uint1


s_units: dict[str:float] = {
    "ml"   : 1E-3,
    "l"    : 1,
    "g"    : 1 ,
    "kg"   : 1E3,
    "mm"   : 1E-3,
    "cm"   : 1E-2,
    "m"    : 1,
    "km"   : 1E3
}

#ending units
e_units: dict[str:float] = {
    #volume
    "fl"   : 1E-15,
    "gal"  : 3.78541,
    "oz_v" : 0.0295735,
    #mass
    "oz_w" : 28.3495,
    "lb"   : 453.592, 
    #distances
    "in"   : 0.0254,
    "ft"   : 0.3048,
    "mi"   : 1609.34

}

convertions: dict[str:list[float]] = {
    "ml"   : ["fl", "gal", "oz_v"],
    "l"    : ["fl", "gal", "oz_v"],
    "g"    : ["oz_w", "lb"],
    "kg"   : ["oz_w", "lb"],
    "mm"   : ["in", "ft", "mi"],
    "cm"   : ["in", "ft", "mi"],
    "m"    : ["in", "ft", "mi"],
    "km"   : ["in", "ft", "mi"]
}

unit_1: str = input("unit 1 : ")
unit_1_value: float = float(input("unit 1 value : "))
unit_2: str = input("unit 2 : ")

if(unit_1 not in s_units.keys()):
    raise ValueError  (f"{unit_1} is not a valid key,\n\
                        valid keys : ml, l, g, kg, mm, cm, m, km ")
if(unit_2 not in e_units.keys()):
    raise ValueError  (f"{unit_2} is not a valid key,\n\
                        valid keys : fl, oz_v, gal, oz_w, lb, in, ft, mi ") 
if(unit_2 not in convertions[unit_1]):
    raise ValueError("Invalid convertion")

print(unit_1_value * s_units[unit_1] / e_units[unit_2])
