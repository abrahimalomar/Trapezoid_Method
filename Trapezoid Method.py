
import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt

class MainApp:
    def __init__(self, root):
        self.root = root
        root.title("Trapezoid Method")

        self.root.geometry("1000x800")  # Adjusted window size

        self.root.configure(bg="#87CEEB")  # Background color for the entire window

        self.central_frame = tk.Frame(root, bg="#E0FFFF")
        self.central_frame.pack(padx=50, pady=50)

        self.title_label = tk.Label(self.central_frame, text="Trapezoid Method", font=("Helvetica", 24, "bold"), bg="#E0FFFF")
        self.title_label.pack(pady=20)

        field_bg_color = "#E0FFFF"  # Color for field backgrounds

        self.nn_label, self.nn = self.create_input_field(self.central_frame, "Enter n:", font=("Helvetica", 18), bg=field_bg_color)
        self.dd_label, self.dd = self.create_input_field(self.central_frame, "Enter d:", font=("Helvetica", 18), bg=field_bg_color)
        self.yy_label, self.yy = self.create_input_field(self.central_frame, "Enter y:", font=("Helvetica", 18), bg=field_bg_color)
        self.aa_label, self.aa = self.create_input_field(self.central_frame, "Enter a:", font=("Helvetica", 18), bg=field_bg_color)
        self.bb_label, self.bb = self.create_input_field(self.central_frame, "Enter b:", font=("Helvetica", 18), bg=field_bg_color)

        self.result_label = tk.Label(self.central_frame, text="Result:", font=("Helvetica", 18), bg="#E0FFFF")
        self.result_label.pack()
        self.resulltt = tk.Entry(self.central_frame, font=("Helvetica", 18))
        self.resulltt.pack()

        self.calculate_button = tk.Button(self.central_frame, text="Calculate", font=("Helvetica", 18), command=self.calculate)
        self.calculate_button.pack(pady=20)

        self.reset_button = tk.Button(self.central_frame, text="Reset", font=("Helvetica", 18), command=self.reset)
        self.reset_button.pack(pady=20)

        self.calculate_button.configure(bg="#FFA500", fg="white")  # Button color
        self.reset_button.configure(bg="#FFA500", fg="white")  # Button color

    def create_input_field(self, parent, label_text, font, bg):
        label = tk.Label(parent, text=label_text, font=font, bg=bg)
        label.pack()
        entry = tk.Entry(parent, font=font, bg=bg)
        entry.pack()
        return label, entry

    def TrapezoidMethod(self, n, d, y, a, b):
        h = (b - a) / n
        ly = []
        lx = []

        def f(d, y, x):
            integration = d / (y + x * x)
            return integration

        z = a
        for j in range(n + 1):
            lx.append(z)
            z = z + h

        for i in lx:
            p = f(d, y, i)
            ly.append(p)

        s = 0
        for i in range(1, len(ly) - 1):
            s += ly[i]
            result = h / 2 * (ly[0] + 2 * (s) + ly[len(ly) - 1])

        return result

    def calculate(self):
        try:
            n1 = int(self.nn.get())
            d2 = float(self.dd.get())
            y3 = float(self.yy.get())
            a4 = float(self.aa.get())
            b5 = float(self.bb.get())
            x = self.TrapezoidMethod(n1, d2, y3, a4, b5)
            self.resulltt.delete(0, tk.END)
            self.resulltt.insert(0, str(x))
            self.plot_graph(n1, d2, y3, a4, b5)
        except Exception as e:
            self.show_errors_empty()

    def plot_graph(self, n, d, y, a, b):
        x_vals = np.linspace(a, b, n + 1)
        y_vals = [self.TrapezoidMethod(n, d, y, a, xi) for xi in x_vals]
        plt.plot(x_vals, y_vals, '-o')
        plt.xlabel('x')
        plt.ylabel('Integration Result')
        plt.title('Trapezoid Method')
        plt.grid()
        plt.show()

    def reset(self):
        self.nn.delete(0, tk.END)
        self.dd.delete(0, tk.END)
        self.yy.delete(0, tk.END)
        self.aa.delete(0, tk.END)
        self.bb.delete(0, tk.END)
        self.resulltt.delete(0, tk.END)

    def show_errors_empty(self):
        messagebox.showerror("Errors", "Error fields are empty")

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()

