import tkinter as tk

def click(event):
    global expression
    text = event.widget.cget("text")
    process_input(text)

def key_press(event):
    global expression
    key = event.char
    if key in "0123456789+-*/.":
        expression += key
        input_var.set(expression)
    elif key == "\r":  # Enter key
        try:
            result = eval(expression)
            input_var.set(result)
            expression = str(result)
        except Exception as e:
            input_var.set("Error")
            expression = ""
    elif key == "\x08":  # Backspace
        expression = expression[:-1]
        input_var.set(expression)

def process_input(text):
    global expression
    if text == "=":
        try:
            result = eval(expression)
            input_var.set(result)
            expression = str(result)
        except Exception as e:
            input_var.set("Error")
            expression = ""
    elif text == "C":
        expression = ""
        input_var.set("")
    else:
        expression += text
        input_var.set(expression)

# Main GUI window
root = tk.Tk()
root.geometry("350x500")
root.title("Python Calculator")

# Global expression string
expression = ""

# Input field
input_var = tk.StringVar()
entry = tk.Entry(root, textvar=input_var, font="Arial 20", bd=10, relief=tk.RIDGE, justify="right")
entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)
entry.focus()  # Focus input to receive keyboard events

# Bind keyboard keys
root.bind("<Key>", key_press)

# Button layout
btn_frame = tk.Frame(root)
btn_frame.pack()

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", "C", "=", "+"]
]

for row in buttons:
    row_frame = tk.Frame(btn_frame)
    row_frame.pack(expand=True, fill="both")
    for btn_text in row:
        btn = tk.Button(row_frame, text=btn_text, font="Arial 18", relief=tk.RAISED, bd=5, height=2, width=4)
        btn.pack(side="left", expand=True, fill="both", padx=5, pady=5)
        btn.bind("<Button-1>", click)

root.mainloop()
