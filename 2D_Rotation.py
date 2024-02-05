import math

def calculate_rotation_points(x, y, Q):
    cos_Q = math.cos(Q)
    sin_Q = math.sin(Q)
    
    new_x = x * cos_Q - y * sin_Q
    new_y = x * sin_Q + y * cos_Q
    
    return new_x, new_y

# Example usage
x = 2
y = 7
Q = 0.7

new_x, new_y = calculate_rotation_points(x, y, Q)
print(f"New x: {new_x}, New y: {new_y}")