import tkinter as tk

def draw_stick_figure(canvas):
    # 頭
    canvas.create_oval(50, 50, 100, 100, outline="black", width=2)

    # 体
    canvas.create_line(75, 100, 75, 200, fill="black", width=2)

    # 左腕
    canvas.create_line(75, 130, 30, 90, fill="black", width=2)

    # 右腕
    canvas.create_line(75, 130, 120, 90, fill="black", width=2)

    # 左脚
    canvas.create_line(75, 200, 50, 250, fill="black", width=2)

    # 右脚
    canvas.create_line(75, 200, 100, 250, fill="black", width=2)

def main():
    root = tk.Tk()
    root.title("Stick Figure")

    canvas = tk.Canvas(root, width=150, height=300)
    canvas.pack()

    draw_stick_figure(canvas)

    root.mainloop()

if __name__ == "__main__":
    main()