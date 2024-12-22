import tkinter as tk
windows_ko = tk.Tk()
name = "ALDRIN_PEÑA"
section = "BSIT-2B"
windows_ko.title(f"OOP")
windows_ko.geometry("300x200")
windows_ko.configure(bg = "white")

label = tk.Label(windows_ko, text=f"OOP LA28 {name} {section}")
label.grid(row=0, column=0, padx=50, pady=40)
label.configure(bg = "white")
windows_ko.mainloop()
