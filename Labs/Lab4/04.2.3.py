from cProfile import label
import math
import matplotlib.pyplot as plt

ball_y: float =  0
ball_starting_speed: float = 100 
ball_speed : float = ball_starting_speed
g: float = 9.8
delta_t: float = 0.1
exact_ball_y: float = 0
print_info: bool = False

time: list[float] = []
y_exact: list[float] = []   
y_simulated: list[float] = []
x: list[int] = []


def simulate_ball(ball_y: float, ball_speed: float, g: float, delta_t: float) -> tuple[float, float]:
    '''
    Given all nedeed parameters it returns the new y position after delta_t time has passed \n
    Simulated
    First value is y position second value is the new speed
    '''

    ball_speed = ball_speed - g * delta_t
    ball_y = ball_y + ball_speed * delta_t

    return ball_y, ball_speed

def exact_ball(ball__starting_speed: float, g: float, t: float) -> float:
    '''
    Given all nedeed parameters it returns the new y position after delta_t time has passed \n
    Exact formula
    '''
    return ball__starting_speed * t - (1/2 * g * math.pow(t, 2)) 

step: int = 1

while ball_y >= 0 or exact_ball_y >= 0: 

    

    ball_y , ball_speed = simulate_ball(ball_y, ball_speed, g, delta_t)
    exact_ball_y = exact_ball(ball_starting_speed, g, delta_t*step)

    time.append(step * delta_t)
    y_simulated.append(ball_y)
    y_exact.append(exact_ball_y)
    x.append(0)

    if(print_info):
        print(f"Simulation step {step} : ")
        print(f"Simulated y position : {ball_y}")
        print(f"Exact y position : {exact_ball_y}")

    step += 1

plt.plot(time, y_simulated, label = "Simulated")
plt.plot(time, y_exact, label = "Exact")
plt.plot(time, x)

plt.xlabel("Time")
plt.ylabel("Position")

plt.legend()
plt.show()
