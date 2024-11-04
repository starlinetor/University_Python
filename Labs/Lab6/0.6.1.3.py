import math

def sphere_volume(r: float) -> float: 
    return 4/3 * math.pi * math.pow(r, 3)

def sphere_surface(r: float) -> float:
    return 4 * math.pi * math.pow(r, 2)
    
def cylinder_volume(r: float, h: float) -> float:
    return math.pi * math.pow(r, 2) * h
    
def cylinder_surface(r: float, h: float) -> float:
    return 2 * math.pi * r * h + 2 * math.pi * math.pow(r,2) 
    
def cone_volume(r: float, h: float) -> float: 
    return math.pi * math.pow(r, 2) * h / 3

def cone_surface(r: float, h: float) -> float:
    return math.pi * r * (r + math.sqrt(math.pow(h,2) + math.pow(r,2)))