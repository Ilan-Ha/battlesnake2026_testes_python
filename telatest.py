import tkinter as tk

root = tk.Tk()

# Setting some window properties
root.title("Tk Example")
root.configure(background="yellow")
root.minsize(200, 200)
root.maxsize(500, 500)
root.geometry("300x300+50+50")

# Create two labels
tk.Label(root, text="Nothing will work unless you do.").pack()
tk.Label(root, text="- Maya Angelou").pack()

root.mainloop()