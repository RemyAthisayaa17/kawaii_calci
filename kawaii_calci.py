import tkinter as tk
from math import sqrt

# 🌸 Create main window
root = tk.Tk()
root.title("Kawaii_Calci🎀💗")
root.geometry("380x550")
root.config(bg="#ffd6eb")# Baby pink background
root.iconbitmap('kawaii_calci.ico')
# 🌸 Entry box
entry = tk.Entry(
    root,
    width=20,
    font=("Comic Sans MS", 26, "bold"),
    border=0,
    bg="#fff0f8",
    justify="right"
)
entry.pack(pady=30, ipady=10)

# 🌸 Frame for buttons
frame = tk.Frame(root, bg="#ffd6eb")
frame.pack()

# 🌸 Button style
btn_style = {
    "font": ("Comic Sans MS", 18, "bold"),
    "bg": "#ffc8e1",  # soft pink
    "fg": "#5e366a",  # lilac text
    "activebackground": "#ffb6d9",
    "activeforeground": "#5e366a",
    "width": 5,
    "height": 2,
    "bd": 0,
    "relief": "ridge"
}

# 🌸 Functions
def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    elif text == "⌫":  # Backspace button
        current = entry.get()
        entry.delete(0, tk.END)
        entry.insert(tk.END, current[:-1])
    elif text == "√":
        try:
            value = float(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, sqrt(value))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    else:
        entry.insert(tk.END, text)

# 🌸 Title label
title = tk.Label(
    root,
    text="Kawaii_Calci 🎀",
    bg="#ffd6eb",
    fg="#b86bba",
    font=("Comic Sans MS", 20, "bold")
)
title.pack(pady=5)

# 🌸 Buttons layout
buttons = [
    ["C", "⌫", "√", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "%", "="]
]

for row in buttons:
    frame_row = tk.Frame(frame, bg="#ffd6eb")
    frame_row.pack()
    for b in row:
        btn = tk.Button(frame_row, text=b, **btn_style)
        btn.pack(side=tk.LEFT, padx=8, pady=8)
        btn.bind("<Button-1>", click)

root.mainloop()
