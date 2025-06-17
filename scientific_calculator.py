import tkinter as tk
import math

def calculate_expression(expr):
    try:
        expr = expr.replace("^", "**")  # Handle power
        expr = expr.replace("√", "math.sqrt")
        expr = expr.replace("log", "math.log10")
        expr = expr.replace("sin", "math.sin(math.radians")
        expr = expr.replace("cos", "math.cos(math.radians")
        expr = expr.replace("tan", "math.tan(math.radians")

        # Add closing parenthesis for trig functions
        open_count = expr.count("math.sin(math.radians") + expr.count("math.cos(math.radians") + expr.count("math.tan(math.radians")
        expr += ")" * open_count

        result = eval(expr)
        return result
    except:
        return "Error"

def click(event):
    button_text = event.widget["text"]
    current = entry.get()

    if button_text == "=":
        result = calculate_expression(current)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

# GUI setup
root = tk.Tk()
root.title("Scientific Calculator")

entry = tk.Entry(root, font=("Arial", 20), borderwidth=5, relief=tk.RIDGE, justify="right")
entry.grid(row=0, column=0, columnspan=6, pady=10)

buttons = [
    ["7", "8", "9", "/", "C", "√("],
    ["4", "5", "6", "*", "(", ")"],
    ["1", "2", "3", "-", "^", "log("],
    ["0", ".", "=", "+", "sin(", "cos("],["tan("]
]

for i in range(len(buttons)):
    for j in range(len(buttons[i])):
        b = tk.Button(root, text=buttons[i][j], font=("Arial", 18), width=5, height=2)
        b.grid(row=i+1, column=j)
        b.bind("<Button-1>", click)

root.mainloop()