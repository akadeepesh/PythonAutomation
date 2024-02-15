import matplotlib.pyplot as plt

def reflect_y_axis(x1, y1, x2, y2):
    x1_ref = -x1
    x2_ref = -x2

    print("Coordinates after reflection about the y-axis:")
    print(f"Point 1: ({x1_ref}, {y1})")
    print(f"Point 2: ({x2_ref}, {y2})")

    plt.plot([x1, x2], [y1, y2], label='Original line')
    plt.plot([x1_ref, x2_ref], [y1, y2], label='Line after reflection')

    plt.legend()
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Reflection of a Line about the Y-axis')
    plt.grid(True)
    plt.show()


def main():
    x1, y1 = map(int, input("Enter the starting point of line segment (x1 y1): ").split())
    x2, y2 = map(int, input("Enter the ending point of line segment (x2 y2): ").split())
    reflect_y_axis(x1, y1, x2, y2)

if __name__ == "__main__":
    main()