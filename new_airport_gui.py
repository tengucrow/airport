import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
from tkinter import messagebox
import data_handling

air_list = data_handling.read_all_ports()
ports = []
for port in air_list:
    ports.append(port[0])


def open_port():
    f = filedialog.askopenfilename(initialdir = "./ports/",title = "Select file",filetypes = (("airport files","*.txt"),("all files","*.*")))
    fields = data_handling.read_port(f)
    name.set(fields[0])
    code.set(fields[1])
    polosa.set(fields[2])
    capacity.set(fields[3])
    coordinates.set(fields[4])

def del_airport():
    ports[lst.curselection()[0]]
    
    

def save_to_file():
    #f = filedialog.asksaveasfilename(initialdir = "./ports/",title = "Select file",filetypes = (("airport files","*.txt"),("all files","*.*")))
    if len(name.get()) > 0:
        data_handling.add_port(name.get(), code.get(), polosa.get(), capacity.get(), coordinates.get())
        messagebox.showinfo(title=None, message="Изменения добавлены")
    else:
        messagebox.showerror(title=None, message="Название аэропорта не может быть пустым")


root = tk.Tk()

name = tk.StringVar()
code = tk.StringVar()
polosa = tk.StringVar()
capacity = tk.StringVar()
coordinates = tk.StringVar()

root.title('Создать аэропорт')
root.geometry('400x500+100+100')


frame_add = ttk.Frame(root, padding = 3, borderwidth = 2, relief = 'sunken')
frame_add.grid(row = 1 , column = 1, padx = 5, pady = 5, sticky = 'we')
frame_del = ttk.Frame(root, padding = 3, borderwidth = 2, relief = 'sunken')
#frame_del.grid(row = 2 , column = 1, padx = 5, pady = 5, sticky = 'we')


lb1 = ttk.Label(frame_add, text = 'name:')
lb2 = ttk.Label(frame_add, text = 'code:')
lb3 = ttk.Label(frame_add, text = 'polosa:')
lb4 = ttk.Label(frame_add, text = 'capacity:')
lb5 = ttk.Label(frame_add, text = 'coordinates:')

ent1 = ttk.Entry(frame_add, textvariable = name)
ent2 = ttk.Entry(frame_add, textvariable = code)
ent3 = ttk.Entry(frame_add, textvariable = polosa)
ent4 = ttk.Entry(frame_add, textvariable = capacity)
ent5 = ttk.Entry(frame_add, textvariable = coordinates)

btn0 = ttk.Button(frame_add, text = "Открыть файл", command = open_port)


btn1 = ttk.Button(frame_add, text = "Сохранить в файл", command = save_to_file)



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

btn0.grid(row = 0, column = 2, sticky = 'we')
btn1.grid(row = 6, column = 2, sticky = 'we' )

ports_var = tk.StringVar(value=ports)
lst = tk.Listbox(frame_del, listvariable=ports_var)
lst.grid(row = 7, column = 1)

btn2 = ttk.Button(frame_del, text = "Удалить аэропорт", command = del_airport)
btn2.grid(row = 8, column = 2, sticky = 'we' )


root.mainloop()
