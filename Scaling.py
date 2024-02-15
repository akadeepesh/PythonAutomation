import matplotlib.pyplot as plt

def scale_line(x1, y1, x2, y2, sx, sy):
    plt.plot([x1, x2], [y1, y2], label='Original line')
    plt.plot([x1*sx, x2*sx], [y1*sy, y2*sy], label='Line after scaling')
    plt.legend()
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Scaling of a Line')
    plt.grid(True)
    plt.show()

def main():
    x1, y1 = map(int, input("Enter the starting point of line segment (x1 y1): ").split())
    x2, y2 = map(int, input("Enter the ending point of line segment (x2 y2): ").split())
    sx, sy = map(float, input("Enter scaling factors sx, sy: ").split())
    scale_line(x1, y1, x2, y2, sx, sy)
    print("Coordinates after scaling:")
    print(f"A: ({x1*sx}, {y1*sy})")
    print(f"B: ({x2*sx}, {y2*sy})")

if __name__ == "__main__":
    main()
