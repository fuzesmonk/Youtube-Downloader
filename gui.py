import tkinter as tk



main = tk.Tk()
main_window = tk.Label(
    bg = "black",
    fg = "white",
    width = 50,
    height = 25
)
video = tk.Entry()
prompt = tk.Label(text="Choose how you would like to download your file", fg="white")
main_window.pack()
main.mainloop()
