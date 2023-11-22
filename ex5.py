import tkinter as tk

class AnimatedStickFigureApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Animated Stick Figure")

        self.canvas = tk.Canvas(self.master, width=300, height=300)
        self.canvas.pack()

        self.x_position = 50  # 初期位置

        self.draw_stick_figure()
        self.animate()

    def draw_stick_figure(self):
        self.canvas.delete("all")  # キャンバスをクリア

        # 頭
        self.canvas.create_oval(self.x_position - 25, 50, self.x_position + 25, 100, outline="black", width=2)

        # 体
        self.canvas.create_line(self.x_position, 100, self.x_position, 200, fill="black", width=2)

        # 左腕
        self.canvas.create_line(self.x_position, 140, self.x_position - 45, 90, fill="black", width=2)

        # 右腕
        self.canvas.create_line(self.x_position, 140, self.x_position + 45, 90, fill="black", width=2)

        # 左脚
        self.canvas.create_line(self.x_position, 200, self.x_position - 25, 250, fill="black", width=2)

        # 右脚
        self.canvas.create_line(self.x_position, 200, self.x_position + 25, 250, fill="black", width=2)

    def animate(self):
        # 10ミリ秒ごとにアニメーションを更新
        self.x_position += 1
        self.draw_stick_figure()
        self.master.after(10, self.animate)

def main():
    root = tk.Tk()
    app = AnimatedStickFigureApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()