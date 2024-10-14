from decimal import Decimal
from math import sqrt

G: float = 6.67E-11
#mass
M: float = 2.2E14
#radius
R: float = 9.4


velocity:float = float(input("Jump velocity : "))


escape_velocity = sqrt((2*G*M)/R)

antiescape_mass = (velocity*velocity*R)/(2*G)

if(velocity <= escape_velocity):
    print  (f"Velocity too low to escape\n\
            Escape velocity : {escape_velocity} km/h")
else:
    print(f"Velocity is enough to escape, \n\
            Mass needed to escape : {antiescape_mass} kg")