import customtkinter as ctk

# Set appearance and theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class CalculatorApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Modern Python Calculator")
        self.geometry("360x520")
        self.resizable(False, False)

        self.expression = ""

        # Display
        self.entry_var = ctk.StringVar()
        self.display = ctk.CTkEntry(self, textvariable=self.entry_var, font=("Arial", 24), justify="right", height=60)
        self.display.pack(padx=20, pady=20, fill="x")

        # Keyboard bindings
        self.bind("<Key>", self.handle_key_press)
        self.bind("<Return>", lambda event: self.on_button_click("="))
        self.bind("<BackSpace>", lambda event: self.on_backspace())

        # Button layout using grid
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", "C", "=", "+"]
        ]

        button_frame = ctk.CTkFrame(self)
        button_frame.pack(expand=True, fill="both", padx=10, pady=10)

        for row_idx, row_values in enumerate(buttons):
            for col_idx, val in enumerate(row_values):
                btn = ctk.CTkButton(button_frame, text=val, font=("Arial", 18),
                                    command=lambda v=val: self.on_button_click(v))
                btn.grid(row=row_idx, column=col_idx, sticky="nsew", padx=5, pady=5)

        for i in range(4):
            button_frame.grid_columnconfigure(i, weight=1)
            button_frame.grid_rowconfigure(i, weight=1)

    def on_button_click(self, char):
        if char == "=":
            try:
                result = str(eval(self.expression))
                self.entry_var.set(result)
                self.expression = result
            except:
                self.entry_var.set("Error")
                self.expression = ""
        elif char == "C":
            self.expression = ""
            self.entry_var.set("")
        else:
            self.expression += char
            self.entry_var.set(self.expression)

    def on_backspace(self):
        self.expression = self.expression[:-1]
        self.entry_var.set(self.expression)

    def handle_key_press(self, event):
        key = event.char
        if key in "0123456789+-*/().":
            self.expression += key
            self.entry_var.set(self.expression)
        elif key.lower() == 'c':
            self.on_button_click("C")

if __name__ == "__main__":
    app = CalculatorApp()
    app.mainloop()
