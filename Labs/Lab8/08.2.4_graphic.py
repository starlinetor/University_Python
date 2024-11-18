from time import sleep
import tkinter as tk

#starting conditions

k : float = 10          #N/m
x : float = 0.5         #m
v : float = 0           #m/s
m : float = 1           #kg
delta_t : float = 0.01  #s

#tkinter
root = tk.Tk()
c = tk.Canvas(root, bg="white",height=400, width=1000)
c.pack()

pendulum = c.create_oval(0, 0, 50, 50,fill="Red")
#move pendulum to starting position
c.move(pendulum,int(500*(1-x)),200)

while True: 
    f = -1 * k * x      #Hooke law
    a = f/m             #Newton law
    v += a * delta_t    #change in velocity is time times acceleration
    x += v * delta_t    #change in position is time times speed
    print(x)
    
    c.move(pendulum, int(-1*v * delta_t * 500),0)
    
    root.update()
    
    sleep(0.01)