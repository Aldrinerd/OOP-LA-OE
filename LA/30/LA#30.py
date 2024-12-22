import tkinter as tk
windows_ko = tk.Tk()
name = "ALDRIN_PEÑA"
section = "BSIT-2B"
windows_ko.title(f"OOP")
windows_ko.geometry("300x200")
windows_ko.configure(bg = "white")
def on_press():
    anime = "Naruto"
    print(f"My favorite anime is {anime}")
button = tk.Button(windows_ko, text="Run", command=on_press)
button.pack(pady = 10)
windows_ko.mainloop()
