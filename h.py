def calculate_height(t, g):
    h = g * t**2 / 2
    return h

while True:
    # Get input from the user
    time = input("Enter the time it takes for the object to fall (in seconds): ")

    # Convert the user's input to a float
    time = float(time)

    # Calculate the height of the object
    height = calculate_height(time, 9.81)

    # Print the result
    print(f"The height of the object is {height} meters.")
