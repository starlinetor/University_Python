R1: float  = float(input("R1 : "))
R2: float  = float(input("R2 : "))
R3: float  = float(input("R3 : "))

#    * * * * R 1 * * * * *
#   +++            *     *
#    *            R 2    R 3  
#   ---            *     * 
#    * * * * * * * * * * * 

R2 = 1/((1/R2) + (1/R2))

#    * * * * R 1 * *
#   +++            *
#    *            R 2  
#   ---            *
#    * * * * * * * *

R1 = R1 + R2

#    * * * * * * * *
#   +++            *
#    *            R 1  
#   ---            *
#    * * * * * * * *

print(R1)