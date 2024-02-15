import matplotlib.pyplot as plt
import math

def rotate_line(x1, y1, x2, y2, angle):
    # angle to radians
    angle_rad = math.radians(angle)

    # the midpoint of the original line
    xm = (x1 + x2) / 2
    ym = (y1 + y2) / 2

    # Translate the line to the origin
    x1 -= xm
    y1 -= ym
    x2 -= xm
    y2 -= ym

    # Coordinates after rotation on origin
    x1_rot = x1 * math.cos(angle_rad) - y1 * math.sin(angle_rad)
    y1_rot = x1 * math.sin(angle_rad) + y1 * math.cos(angle_rad)
    x2_rot = x2 * math.cos(angle_rad) - y2 * math.sin(angle_rad)
    y2_rot = x2 * math.sin(angle_rad) + y2 * math.cos(angle_rad)

    # Translate the line back to its original point
    x1_rot += xm
    y1_rot += ym
    x2_rot += xm
    y2_rot += ym

    # Plot original and rotated lines
    plt.plot([x1 + xm, x2 + xm], [y1 + ym, y2 + ym], label='Original line')
    plt.plot([x1_rot, x2_rot], [y1_rot, y2_rot], label='Line after rotation')

    print("Coordinates after rotation:")
    print(f"Point 1: ({x1_rot}, {y1_rot})")
    print(f"Point 2: ({x2_rot}, {y2_rot})")

    plt.legend()
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Rotation of a Line')
    plt.grid(True)
    plt.show()

def main():
    x1, y1 = map(int, input("Enter the starting point of line segment (x1 y1): ").split())
    x2, y2 = map(int, input("Enter the ending point of line segment (x2 y2): ").split())
    angle = float(input("Enter rotation angle in degrees: "))
    rotate_line(x1, y1, x2, y2, angle)

if __name__ == "__main__":
    main()
