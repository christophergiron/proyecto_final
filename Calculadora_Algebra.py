#import Pantalla_principal as PP
import tkinter as tk
from tkinter import messagebox 
import numpy as np

def inversa():
    instruccion.grid_remove()
    boton.grid_remove()
    botonS.grid_remove()
    botonM.grid_remove()
    inversaExec()
    
def multi():
    instruccion.grid_remove()
    boton.grid_remove()
    botonS.grid_remove()
    botonM.grid_remove()
    multiExec()
    
def sis_ecu():
    instruccion.grid_remove()
    boton.grid_remove()
    botonS.grid_remove()
    botonM.grid_remove()
    sis_ecuExec()

def inversaExec():
    instruccionInv = tk.Label(CA_Win, text="Ingrese su matriz: ")
    instruccionInv.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
    
def multiExec():
    instruccionInv = tk.Label(CA_Win, text="Ingrese su matriz: ")
    instruccionInv.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
    
def sis_ecuExec():
    instruccionSis = tk.Label(CA_Win, text="Ingrese su matriz: ")
    instruccionSis.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        
CA_Win = tk.Tk()
CA_Win.title("Calculadora de matrices")
CA_Win.geometry("625x300")

instruccion = tk.Label(CA_Win, text="Seleccione la operacion a realizar: ")
instruccion.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

boton = tk.Button(CA_Win, text="Matriz inversa", command=inversa)
boton.grid(row=1, column=8, padx=10, pady=10)

botonM = tk.Button(CA_Win, text="Multiplicacion", command=multi)
botonM.grid(row=11, column=8, padx=10, pady=10)

botonS = tk.Button(CA_Win, text="Sistemas de ecuaciones lineales", command=sis_ecu)
botonS.grid(row=21, column=8, padx=10, pady=10)
#pp.volver()

CA_Win.mainloop()