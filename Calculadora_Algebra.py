#import Pantalla_principal as PP
import tkinter as tk
from tkinter import messagebox 
import numpy as np

CA_Win = tk.Tk()
CA_Win.title("Calculadora de matrices")
CA_Win.geometry("625x300")

def menu_principal():
    for menu1 in CA_Win.winfo_children():
        menu1.destroy()
        
    def backButton():
        boton_return = tk.Button(CA_Win, text="Regresar", command=menu_principal)
        boton_return.grid(row=1, column=8, padx=10, pady=10)
        
    def clean_buttons():
        instruccion.grid_forget()
        boton.grid_forget()
        botonS.grid_forget()
        botonM.grid_forget()
        
    def inversa():
        clean_buttons()
        instruccionInv = tk.Label(CA_Win, text="Ingrese su matriz: ")
        instruccionInv.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        backButton()
        
    def multi():
        clean_buttons()
        instruccionInv = tk.Label(CA_Win, text="Ingrese su matriz: ")
        instruccionInv.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        backButton()
        
    def sis_ecu_sub():
        def clean_buttons_sub1():
            boton_cramer.grid_forget()
            boton_Gaus.grid_forget()
            boton_return_main.grid_forget()
            
        def sis_ecu_Gaus():
            clean_buttons_sub1()
            boton_return = tk.Button(CA_Win, text="Regresar", command=sis_ecu_sub)
            boton_return.grid(row=1, column=8, padx=10, pady=10)
            
        def sis_ecu_cramer():
            clean_buttons_sub1()
            boton_return = tk.Button(CA_Win, text="Regresar", command=sis_ecu_sub)
            boton_return.grid(row=1, column=8, padx=10, pady=10)

        boton_Gaus = tk.Button(CA_Win, text="Metodo de Gauss-Jordan", command=sis_ecu_Gaus)
        boton_Gaus.grid(row=1, column=8, padx=10, pady=10)

        boton_cramer = tk.Button(CA_Win, text="Metodo de cramer", command=sis_ecu_cramer)
        boton_cramer.grid(row=11, column=8, padx=10, pady=10)
        
        boton_return_main = tk.Button(CA_Win, text="Regresar", command=menu_principal)
        boton_return_main.grid(row=21, column=8, padx=10, pady=10)
        
    def sis_ecu():
        clean_buttons()
        backButton()
        for menu2 in CA_Win.winfo_children():
            menu2.destroy()
        sis_ecu_sub()
        
    instruccion = tk.Label(CA_Win, text="Seleccione la operacion a realizar: ")
    instruccion.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    boton = tk.Button(CA_Win, text="Matriz inversa", command=inversa)
    boton.grid(row=1, column=8, padx=10, pady=10)

    botonM = tk.Button(CA_Win, text="Multiplicacion", command=multi)
    botonM.grid(row=11, column=8, padx=10, pady=10)

    botonS = tk.Button(CA_Win, text="Sistemas de ecuaciones lineales", command=sis_ecu)
    botonS.grid(row=21, column=8, padx=10, pady=10)

menu_principal()
CA_Win.mainloop()