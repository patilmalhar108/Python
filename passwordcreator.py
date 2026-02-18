import tkinter as tk
from tkinter import messagebox
import string
import secrets

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("CYBER_KEY_GEN")
        self.root.geometry("400x550")
        self.root.configure(bg="#0a0a0c")

        # Design Constants
        self.neon_green = "#22c55e"
        self.dark_bg = "#0a0a0c"
        self.card_bg = "#121214"

        # Variables
        self.length_var = tk.IntVar(value=16)
        self.upper_var = tk.BooleanVar(value=True)
        self.lower_var = tk.BooleanVar(value=True)
        self.nums_var = tk.BooleanVar(value=True)
        self.syms_var = tk.BooleanVar(value=True)
        self.password_var = tk.StringVar(value="")

        self.setup_ui()
        self.generate_password()

    def setup_ui(self):
        # Header
        tk.Label(self.root, text="CYBER_KEY_GEN", font=("Courier", 20, "bold"), 
                 bg=self.dark_bg, fg=self.neon_green).pack(pady=20)

        # Display Box
        display_frame = tk.Frame(self.root, bg="#000000", highlightthickness=1, 
                                 highlightbackground=self.neon_green)
        display_frame.pack(padx=30, fill="x")
        
        self.display_label = tk.Label(display_frame, textvariable=self.password_var, 
                                      font=("Courier", 14), bg="#000000", 
                                      fg=self.neon_green, wraplength=300)
        self.display_label.pack(pady=20)

        # Controls Frame
        ctrl_frame = tk.Frame(self.root, bg=self.dark_bg)
        ctrl_frame.pack(pady=20, padx=30, fill="x")

        # Length Slider
        tk.Label(ctrl_frame, text="KEY_LENGTH", bg=self.dark_bg, 
                 fg=self.neon_green, font=("Courier", 10)).pack(anchor="w")
        tk.Scale(ctrl_frame, from_=8, to=64, variable=self.length_var, 
                 orient="horizontal", bg=self.dark_bg, fg=self.neon_green, 
                 highlightthickness=0, troughcolor="#1e1e20").pack(fill="x", pady=5)

        # Checkbuttons
        opts = [("UPPERCASE", self.upper_var), ("LOWERCASE", self.lower_var), 
                ("NUMBERS", self.nums_var), ("SYMBOLS", self.syms_var)]
        
        for text, var in opts:
            tk.Checkbutton(ctrl_frame, text=text, variable=var, bg=self.dark_bg, 
                           fg=self.neon_green, selectcolor="#000000", 
                           activebackground=self.dark_bg, activeforeground=self.neon_green,
                           font=("Courier", 10)).pack(anchor="w")

        # Action Buttons
        tk.Button(self.root, text="GENERATE_SEQUENCE", command=self.generate_password,
                  bg=self.neon_green, fg="#000000", font=("Courier", 12, "bold"),
                  relief="flat", pady=10).pack(pady=10, padx=30, fill="x")

        tk.Button(self.root, text="COPY_TO_CLIPBOARD", command=self.copy_password,
                  bg="#1e1e20", fg=self.neon_green, font=("Courier", 10),
                  relief="flat", pady=5).pack(pady=5, padx=30, fill="x")

    def generate_password(self):
        chars = ""
        if self.upper_var.get(): chars += string.ascii_uppercase
        if self.lower_var.get(): chars += string.ascii_lowercase
        if self.nums_var.get(): chars += string.digits
        if self.syms_var.get(): chars += string.punctuation

        if not chars:
            self.password_var.set("SELECT_OPTIONS")
            return

        password = ''.join(secrets.choice(chars) for _ in range(self.length_var.get()))
        self.password_var.set(password)

    def copy_password(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.password_var.get())
        messagebox.showinfo("SUCCESS", "Access Granted: Password copied to clipboard.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()