#!/usr/bin/env python3

from anotador import Anotador
import tkinter
from tkinter import ttk
from tkinter import messagebox

class Gui():
    '''Provee una interfaz gráfica de usuario al anotador'''

    def __init__(self):
        '''Crea la pantalla inicial, mostrando botones y notas'''
        self.ventana_principal = tkinter.Tk()
        self.anotador = Anotador()
        self.ventana_principal.title("Anotador")

        botonAgregar=tkinter.Button(self.ventana_principal,text="Agregar nota",
                command = self.agregar_nota).grid(row=0, column=0)
        botonModificar=tkinter.Button(self.ventana_principal,text="Modificar",
                command = self.modificar_nota).grid(row=0, column=1)
        botonEliminar=tkinter.Button(self.ventana_principal,text="Eliminar",
                command = self.eliminar_nota).grid(row=0, column=2)
        tkinter.Label(self.ventana_principal,text="Buscar").grid(row=1,column=0)
        self.cajaBuscar = tkinter.Entry(self.ventana_principal)
        self.cajaBuscar.grid(row=1, column=1)
        botonBuscar = tkinter.Button(self.ventana_principal, text="Buscar",
                command = self.buscar_notas).grid(row=1, column=2)

        self.treeview = ttk.Treeview(self.ventana_principal, 
                columns=("texto","etiquetas"))
        self.treeview.heading("#0",text="id")
        self.treeview.column("#0",minwidth=0, width=40)
        self.treeview.heading("texto",text="Texto")
        self.treeview.heading("etiquetas",text="Etiquetas")
        self.treeview.grid(row=2, columnspan=3)
        botonSalir = tkinter.Button(self.ventana_principal, text = "Salir",
                command = self.ventana_principal.destroy)
        botonSalir.grid(row=3, column=1)

    def agregar_nota(self):
        
        '''Agrega una nueva nota a la lista de notas'''
        ''' Construye una ventana de diálogo '''
        
        self.dialogonota = tkinter.Toplevel()
        self.dialogonota.title("Agregar nota")
        boton_cerrar = tkinter.Button(self.dialogonota, text='Cerrar', 
                           command=self.dialogonota.destroy)   
        boton_cerrar.grid(row=3, column=3)
        boton_agregar = tkinter.Button(self.dialogonota, text='Agregar', 
                        command=self.guardar)
        boton_agregar.grid(row=3, column=2)
        self.cajanota = tkinter.Entry(self.dialogonota)
        self.cajanota.grid(row=0, column=1)
        tkinter.Label(self.dialogonota,text="Nota").grid(row=0,column=0)

        self.cajaetiqueta = tkinter.Entry(self.dialogonota)
        self.cajaetiqueta.grid(row=1, column=1)
        tkinter.Label(self.dialogonota,text="etiqueta").grid(row=1,column=0)


        self.dialogonota.grab_set()
        self.ventana_principal.wait_window(self.dialogonota)

    def guardar(self):
        
        nota=self.anotador.nueva_nota(self.cajanota.get(),self.cajaetiqueta.get())
        self.dialogonota.destroy()
        self.treeview.insert("",tkinter.END,text=nota.id,
                                     values=(nota.texto,nota.etiquetas),iid=nota.id)

        
        

    def modificar_nota(self):
        '''Modifica la nota seleccionada (texto o etiquetas)'''
        pass

    def eliminar_nota(self):
        '''Elimina la nota seleccionada'''
    
        pass

    def buscar_notas(self):
        '''Busca y muestra las notas que coincidan con un filtro de búsqueda 
        dado'''
        filtro = self.cajaBuscar.get()
        notas = self.anotador.buscar(filtro)
        if notas:
            self.poblar_tabla(notas)
        else:
            messagebox.showwarning("sin resultados","la busqueda no arrojo resultados")


    def poblar_tabla(self,notas=None):
        '''limpia el treeview y desoues agrega las notas que recibe en "notas"
        ,sino recibe nada trabaja con todas las notas'''

#limpiar treeview        
        for i in self.treeview.get_children():
            self.treeview.delete(i)

#insertar datos de notas
        if not notas:
            notas=self.anotador.notas
        else:
            for nota in notas:
                self.treeview.insert("",tkinter.END,text=nota.id,
                                     values=(nota.texto,nota.etiquetas),iid=nota.id)




if __name__ == "__main__":
    g = Gui()
    g.ventana_principal.mainloop()
