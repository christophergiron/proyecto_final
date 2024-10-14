#import Pantalla_principal as PP
import tkinter as tk
from tkinter import messagebox
import math
import numpy

ventana = tk.Tk()
ventana.title("Calculadora de matrices")
ventana.geometry("400x300")

instruccion = tk.Label(ventana, text="Seleccione la operacion a realizar: ")
instruccion.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
#pp.volver()

ventana.mainloop()