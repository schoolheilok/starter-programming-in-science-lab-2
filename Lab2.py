# Function 1: Calculate the height of the ball after time t
# This function should take the initial height h0 and time t as inputs, and return the height at time t.
# Round up to one decimal point
def calculate_height(h0, t):
    # TODO: Implement this function
    pass  # Replace with your code
    
h_0=float(input("Enter initial height of ball in meters: "))
t=float(input("Enter time in seconds: "))
g=9.8
def calculate_height(t):
    return h_0 - 0.5*g*t**2
print(f"Initial height entered: {h_0}")
print(f"Time entered: {t}")
print(f"Height of ball at time {t} seconds is {round(calculate_height(t),1)} meters.")


# Function 2: Calculate the distance traveled by the car
# This function should take the time t as input and return the distance traveled by the car.
def calculate_car_distance(t):
    # TODO: Implement this function
    pass  # Replace with your code

d=float(input("Enter distance in meters: "))
t=float(input("Enter time in seconds: "))
def calculate_car_distance(t):
    return d/t
print(f"Distance entered: {d}")
print(f"Time entered: {t}")
print(f"Car's speed is {round(calculate_car_distance(t),1)} meters per second.")
