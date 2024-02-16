# 2021UME4099 - Deepesh Kumar

import matplotlib.pyplot as plt

def translate_line(x1, y1, x2, y2, tx, ty):
    print("Coordinates after Translation:")
    print(f"A: ({x1+tx}, {y1+ty})")
    print(f"B: ({x2+tx}, {y2+ty})")
    plt.plot([x1, x2], [y1, y2], label='Original line')
    plt.plot([x1+tx, x2+tx], [y1+ty, y2+ty], label='Line after translation')
    plt.legend()
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Translation of a Line')
    plt.grid(True)
    plt.show()

def main():
    x1, y1 = map(int, input("Enter the starting point of line segment (x1 y1): ").split())
    x2, y2 = map(int, input("Enter the ending point of line segment (x2 y2): ").split())
    tx, ty = map(int, input("Enter translation distances tx, ty: ").split())
    translate_line(x1, y1, x2, y2, tx, ty)

if __name__ == "__main__":
    main()
