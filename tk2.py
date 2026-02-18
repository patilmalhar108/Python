import tkinter as tk
window = tk.Tk()
for i in range(3):
    for j in range(5):
        frame = tk.Frame(master = window, relief = tk.RAISED, borderwidth = 1)
        frame.grid(row = i, column = j, padx = 25, pady = 25)
        label = tk.Label(master = frame, text = f"row{i}\n column{j}")
        label.pack()
window.mainloop()