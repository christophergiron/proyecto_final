#import Pantalla_principal as PP
import tkinter as tk
from tkinter import messagebox
import math
import numpy


def inversa():
    print("Test")
    
def multi():
    print("Test")
    
def sis_ecu():
    print("Test")
    
CA_Win = tk.Tk()
CA_Win.title("Calculadora de matrices")
CA_Win.geometry("400x300")

instruccion = tk.Label(CA_Win, text="Seleccione la operacion a realizar: ")
instruccion.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

boton = tk.Button(CA_Win, text="Matriz inversa", command=inversa)
boton.grid(row=1, column=8, padx=10, pady=10)

boton = tk.Button(CA_Win, text="Multiplicacion", command=multi)
boton.grid(row=11, column=8, padx=10, pady=10)

boton = tk.Button(CA_Win, text="Sistemas de ecuaciones lineales", command=sis_ecu)
boton.grid(row=21, column=8, padx=10, pady=10)
#pp.volver()

CA_Win.mainloop()