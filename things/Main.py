from things.Dao import Dao
from models.Jugador import Jugador
#import tkinter as tk
from tkinter import *
import tkinter as tk

if __name__ == '__main__':

    myDao = Dao()
    pl = Jugador()


    def btnInsertClicked():
        pl.setId(e1.get())
        pl.setNombre(e2.get())
        pl.setApellido(e3.get())
        pl.setEdad(e4.get())
        pl.setSalario(e5.get())
        print(e1.get() + e2.get() + e3.get() + e4.get() + e5.get())
        myDao.insert(pl)
        cleanScreen()

    def btnUpdateClicked():
        pl.setId(e1.get())
        pl.setNombre(e2.get())
        pl.setApellido(e3.get())
        pl.setEdad(e4.get())
        pl.setSalario(e5.get())
        print(e1.get() + e2.get() + e3.get() + e4.get() + e5.get())
        myDao.update(pl)
        cleanScreen()

    def btnDeleteClicked():
        pl.setId(e1.get())
        myDao.delete(pl)
        cleanScreen()

    def btnReadOneClicked():
        pl.setId(e1.get())
        print(myDao.readOne(pl))
        cleanScreen()


    def btnReadAllClicked():
        myDao.readAll()
        cleanScreen()

    def cleanScreen():
        e1.configure(text=None)
        e2.configure(text=None)
        e3.configure(text=None)
        e4.configure(text=None)
        e5.configure(text=None)

    """GUI AQUÍ"""

    m = tk.Tk()
    m.geometry('350x300')
    m.title('CRUD SELECCIÓN')

    #btn  = tk.Button(m,text='stop', width=25, command=m.destroy)
    #btn.pack()
    Label(m,text='Id').grid(row=0)
    Label(m, text='Nombre').grid(row=1)
    Label(m, text='Apellido').grid(row=2)
    Label(m, text='Edad').grid(row=3)
    Label(m, text='Salario').grid(row=4)

    e1 = Entry(m)
    e2 = Entry(m)
    e3 = Entry(m)
    e4 = Entry(m)
    e5 = Entry(m)

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    e3.grid(row=2, column=1)
    e4.grid(row=3, column=1)
    e5.grid(row=4, column=1)





    btnInsert = tk.Button(m, text = 'Insert', width=20, command=btnInsertClicked,  bg='yellow').grid(row=5, column=1)
    btnUpdate = tk.Button(m, text='Update', width=20, command=btnUpdateClicked, bg='yellow').grid(row=6, column=1)
    btnDelete = tk.Button(m, text='Delete', width=20, command=btnDeleteClicked, bg='yellow').grid(row=7, column=1)
    btnReadOne = tk.Button(m, text='ReadOne', width=20, command=btnReadOneClicked, bg='yellow').grid(row=8, column=1)
    btnReadAll = tk.Button(m, text='ReadOne', width=20, command=btnReadAllClicked, bg='yellow').grid(row=9, column=1)





    m.mainloop()



