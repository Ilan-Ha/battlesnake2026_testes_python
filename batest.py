# class FooWrapper(object):
#     def __init__(self, value):
#          self.value = value

# # save an object into a list
# l = []
# obj = FooWrapper(5)
# l.append(obj)
# print(l) 
# # add another object, so the initial object is shifted
# l.insert(0, FooWrapper(1))
# print(l) 
# # change the value of the initial object
# obj.value = 3
# print(l) 
# print(l[1].value) # prints 3 since it's still the same reference

# print('\x1b[6;30;42m' + 'Success!' + '\x1b[0m')
# for i in range(0,16):
#     aux = ''
#     for j in range(0,16):
#         code = str(i*16 + j)
#         aux += u"\u001b[38;5;"+code+'m '+ code.ljust(4)
#     print(aux+'\u001b[0m')
# print(u"\u001b[38;5;1m teste1 \u001b[0m")
# print(u"\u001b[38;5;9m teste2 \u001b[0m")

import tkinter as tk
from random import seed, choice
from string import ascii_letters

seed(42)

colors = ('red', 'yellow', 'green', 'cyan', 'blue', 'magenta')
def do_stuff():
    s = ''.join([choice(ascii_letters) for i in range(10)])
    color = choice(colors)
    l.config(text=s, fg=color)
    root.after(100, do_stuff)

root = tk.Tk()
root.wm_overrideredirect(True)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.bind("<Button-1>", lambda evt: root.destroy())

l = tk.Label(text='', font=("Helvetica", 60))
l.pack(expand=True)

do_stuff()
root.mainloop()