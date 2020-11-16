import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
import data_handling

def save_to_file():
    #f = filedialog.asksaveasfilename(initialdir = "./ports/",title = "Select file",filetypes = (("airport files","*.txt"),("all files","*.*")))
    data_handling.add_port(name.get(), code.get(), polosa.get(), capacity.get(), coordinates.get())


root = tk.Tk()

name = tk.StringVar()
code = tk.StringVar()
polosa = tk.StringVar()
capacity = tk.StringVar()
coordinates = tk.StringVar()

root.title('Создать аэропорт')
root.geometry('300x200+100+100')

lb1 = ttk.Label(root, text = 'name:')
lb2 = ttk.Label(root, text = 'code:')
lb3 = ttk.Label(root, text = 'polosa:')
lb4 = ttk.Label(root, text = 'capacity:')
lb5 = ttk.Label(root, text = 'coordinates:')

ent1 = ttk.Entry(root, textvariable = name)
ent2 = ttk.Entry(root, textvariable = code)
ent3 = ttk.Entry(root, textvariable = polosa)
ent4 = ttk.Entry(root, textvariable = capacity)
ent5 = ttk.Entry(root, textvariable = coordinates)

btn1 = ttk.Button(root, text = "Сохранить в файл", command = save_to_file)

lb1.grid(padx = 5, pady = 2, row = 1, column = 1, sticky = tk.E )
lb2.grid(padx = 5, pady = 2, row = 2, column = 1, sticky = tk.E )
lb3.grid(padx = 5, pady = 2, row = 3, column = 1, sticky = tk.E )
lb4.grid(padx = 5, pady = 2, row = 4, column = 1, sticky = tk.E )
lb5.grid(padx = 5, pady = 2, row = 5, column = 1, sticky = tk.E )


ent1.grid(padx = 5, pady = 2, row = 1, column = 2, sticky = tk.E )
ent2.grid(padx = 5, pady = 2, row = 2, column = 2, sticky = tk.E )
ent3.grid(padx = 5, pady = 2, row = 3, column = 2, sticky = tk.E )
ent4.grid(padx = 5, pady = 2, row = 4, column = 2, sticky = tk.E )
ent5.grid(padx = 5, pady = 2, row = 5, column = 2, sticky = tk.E )

btn1.grid(row = 6, column = 2, sticky = 'we' )


root.mainloop()
