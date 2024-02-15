import matplotlib.pyplot as plt

def reflect_x_axis(x1, y1, x2, y2):
    y1_ref = -y1
    y2_ref = -y2

    print("Coordinates after reflection about the x-axis:")
    print(f"Point 1: ({x1}, {y1_ref})")
    print(f"Point 2: ({x2}, {y2_ref})")

    plt.plot([x1, x2], [y1, y2], label='Original line')
    plt.plot([x1, x2], [y1_ref, y2_ref], label='Line after reflection')

    plt.legend()
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Reflection of a Line about the X-axis')
    plt.grid(True)
    plt.show()

def main():
    x1, y1 = map(int, input("Enter the starting point of line segment (x1 y1): ").split())
    x2, y2 = map(int, input("Enter the ending point of line segment (x2 y2): ").split())
    reflect_x_axis(x1, y1, x2, y2)

if __name__ == "__main__":
    main()