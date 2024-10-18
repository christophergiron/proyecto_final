import tkinter as tk
from tkinter import messagebox
import numpy as np
from fractions import Fraction
import matplotlib.pyplot as plt

Frame2 = tk.Tk()
Frame2.title("Calculadora de matrices")
Frame2.geometry("800x500")

Pan_principal = tk.Frame(Frame2)
frame_Pantalla_Minversa = tk.Frame(Frame2)
frame_pantalla_Multiplicacion = tk.Frame(Frame2)
frame_pantalla_sis_ecuaciones = tk.Frame(Frame2)
frame_calc_gauss = tk.Frame(Frame2)
frame_calc_cramer = tk.Frame(Frame2)
    
def pantalla_principal():
    Pan_principal.grid()
    frame_Pantalla_Minversa.grid_forget()
    frame_pantalla_Multiplicacion.grid_forget()
    frame_pantalla_sis_ecuaciones.grid_forget()
    frame_calc_gauss.grid_forget()
    frame_calc_cramer.grid_forget()
    
    boton_inversa.grid(row=2, column=1, padx=10, pady=10)
    boton_Multi.grid(row=3, column=1, padx=10, pady=10)
    boton_sis_ecuaciones.grid(row=4, column=1, padx=10, pady=10)
    
def pantalla_Minversa():
    frame_Pantalla_Minversa.grid()
    Pan_principal.grid_forget()
    frame_pantalla_Multiplicacion.grid_forget()
    frame_pantalla_sis_ecuaciones.grid_forget()
    frame_calc_gauss.grid_forget()
    frame_calc_cramer.grid_forget()
    
    boton_inversa.grid_forget()
    boton_Multi.grid_forget()
    boton_sis_ecuaciones.grid_forget()
    
def pantalla_Multiplicacion():
    frame_pantalla_Multiplicacion.grid()
    frame_Pantalla_Minversa.grid_forget()
    Pan_principal.grid_forget()
    frame_pantalla_sis_ecuaciones.grid_forget()
    frame_calc_gauss.grid_forget()
    frame_calc_cramer.grid_forget()

    boton_inversa.grid_forget()
    boton_Multi.grid_forget()
    boton_sis_ecuaciones.grid_forget()
    
def pantalla_Sis_ecuaciones():
    frame_pantalla_sis_ecuaciones.grid()
    frame_Pantalla_Minversa.grid_forget()
    frame_pantalla_Multiplicacion.grid_forget()
    Pan_principal.grid_forget()
    frame_calc_gauss.grid_forget()
    frame_calc_cramer.grid_forget()
    
    boton_inversa.grid_forget()
    boton_Multi.grid_forget()
    boton_sis_ecuaciones.grid_forget()
    boton_calc_gauss.grid(row=2, column=1, padx=10, pady=10)
    boton_calc_cramer.grid(row=3, column=1, padx=10, pady=10)
    
def Calculadora_gauss():
    frame_calc_gauss.grid()
    frame_pantalla_sis_ecuaciones.grid_forget()
    frame_Pantalla_Minversa.grid_forget()
    frame_pantalla_Multiplicacion.grid_forget()
    Pan_principal.grid_forget()
    frame_calc_cramer.grid_forget()
    
    boton_inversa.grid_forget()
    boton_Multi.grid_forget() 
    boton_sis_ecuaciones.grid_forget()
    
def Calculadora_cramer():
    frame_calc_cramer.grid()
    frame_pantalla_sis_ecuaciones.grid_forget()
    frame_Pantalla_Minversa.grid_forget()
    frame_pantalla_Multiplicacion.grid_forget()
    Pan_principal.grid_forget()
    frame_calc_gauss.grid_forget()

    boton_inversa.grid_forget()
    boton_Multi.grid_forget()
    boton_sis_ecuaciones.grid_forget()
    
boton_inversa = tk.Button(Frame2, text="Matriz Inversa",font=("Times New Roman", 10),command=pantalla_Minversa, width=30, height=3)
boton_inversa.grid(row=2, column=1, padx=10, pady=10)
    
boton_Multi = tk.Button(Frame2, text="Multiplicacion de matrices",font=("Times New Roman", 10),command=pantalla_Multiplicacion, width=30, height=3)
boton_Multi.grid(row=3, column=1, padx=10, pady=10)

boton_sis_ecuaciones = tk.Button(Frame2, text="Sistema De Ecuaciones,",font=("Times New Roman", 10),command=pantalla_Sis_ecuaciones,width=30, height=3)
boton_sis_ecuaciones.grid(row=4, column=1, padx=10, pady=10)

boton_calc_gauss = tk.Button(frame_pantalla_sis_ecuaciones, text="Metodo de Gauss Jordan",font=("Times New Roman", 10), command=Calculadora_gauss,width=30, height=3)
boton_calc_gauss.grid(row=2, column=1, padx=10, pady=10)

boton_calc_cramer = tk.Button(frame_pantalla_sis_ecuaciones,text="Metodo de Cramer",font=("Times New Roman", 10),command=Calculadora_cramer,width=30, height=3)
boton_calc_cramer.grid(row=3, column=1, padx=10, pady=10)
#RELLENEN EL MALDITO ESQUELETO SI NO ENTIENDEN ALGO AVISENME PORFAVOR TANTO A MI COMO A MIGUEL 
#ASEGURENSE DE LLAMAR SIEMPRE A LAS VENTANAS (FRAMES) CORRESPONDIENTES A CADA LUGAR NO ALTEREN EL ESQUELETO ESTA SOLO PARA RELLENAR 
#MIREN BIEN LAS VARIABLES QUE VAN A DEFINIR NO DUPLIQUEN FUNCIONES SI HAY ALGUNA FUNCION QUE NECESITA SER LLAMADA
#ES NECESARIO CREAR LA MISMA FUNCION ENCIMA BAJO EL MISMO NOMBRE SIMPLEMENTE LLAMEN A LA FUNCION ORIGINAL QUE CREARON
#EJEMPLO para llamar a un boton yo creo una funcion llamada def boton_poyo(): dentro de esto meto lo que deberia hacer el boton 
#si mas tarde creo otro boton y quiero que haga lo mismo simplemente le agrego al boton que llame a boton_poyo para que replique su funcionamiento
#es mas organizado y se evitan romper la cabeza 
#TAMPOCO METAN FUNCIONES DENTRO DE FUNCIONES SIEMPRE TRATEN DE QUE TODAS LAS FUNCIONES NUEVAS ESTEN BAJO LA MISMA JERARQUIA 
#A QUE ME REFIERO A QUE LAS DEFINICIONES ESTEN EN UNA MISMA SANGRIA YA LO QUE ESTE DENTRO DE LA FUNCION NO IMPORTA LA SANGRIA QUE PUEDA LLEGAR A TENER
#nuevamente se evitan romper los codigos y romper sus cabezas 
#buenas noches bueno buenos dias mejor dicho

pantalla_principal

Frame2.mainloop()
