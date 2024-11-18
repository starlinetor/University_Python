from time import sleep

#starting conditions

k : float = 10          #N/m
x : float = 0.5         #m
v : float = 0           #m/s
m : float = 1           #kg
delta_t : float = 0.01  #s

while True: 
    f = -1 * k * x      #Hooke law
    a = f/m             #Newton law
    v += a * delta_t    #change in velocity is time times acceleration
    x += v * delta_t    #change in position is time times speed
    print(x)
    sleep(0.01)