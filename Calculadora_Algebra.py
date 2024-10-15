#import Pantalla_principal as PP
import tkinter as tk
from tkinter import messagebox
import numpy as np

CA_Win = tk.Tk()
CA_Win.title("Calculadora de matrices")
CA_Win.geometry("625x400")

def menu_principal():
    for menu1 in CA_Win.winfo_children():
        menu1.destroy()
        
    def backButton():
        boton_return = tk.Button(CA_Win, text="Regresar", command=menu_principal)
        boton_return.grid(row=0, column=0, padx=10, pady=10)

    def clean_buttons():
        instruccion.grid_forget()
        boton.grid_forget()
        botonS.grid_forget()
        botonM.grid_forget()

    def inversa():
        clean_buttons()
        instruccionInv = tk.Label(CA_Win, text="Ingrese el tamaño de la matriz: ")
        instruccionInv.grid(row=0, column=5, columnspan=2, padx=10, pady=10)

        fila_la1 = tk.Label(CA_Win, text="Filas: ")
        fila_la1.grid(row=1, column=0)
        fila_e1 = tk.Entry(CA_Win, width=5)
        fila_e1.grid(row=1, column=1)

        columna_la1 = tk.Label(CA_Win, text="Columnas: ")
        columna_la1.grid(row=2, column=0)
        columna_e2 = tk.Entry(CA_Win, width=5)
        columna_e2.grid(row=2, column=1)

        def generar_matriz():
            try:
                filas = int(fila_e1.get())
                columnas = int(columna_e2.get())

                if filas <= 0 or columnas <= 0:
                    raise ValueError("El tamaño debe ser mayor a 0.")
                
                entradas_matriz = []
                for i in range(filas):
                    fila = []
                    for j in range(columnas):
                        entrada = tk.Entry(CA_Win, width=5)
                        entrada.grid(row=4 + i, column=j, padx=5, pady=5)
                        fila.append(entrada)
                    entradas_matriz.append(fila)

                def calcular_inversa():
                    try:
                        matriz = np.array([[float(entradas_matriz[i][j].get()) for j in range(columnas)] for i in range(filas)])
                        if filas != columnas:
                            resultado_inversa.config(text="La matriz no es cuadrada, no tiene inversa.")
                        else:
                            matriz_inversa = np.linalg.inv(matriz)
                            resultado_inversa.config(text=f"Inversa de la matriz:\n{matriz_inversa}")
                        
                    except np.linalg.LinAlgError:
                        resultado_inversa.config(text="Error: La matriz no es invertible.")
                    except Exception as e:
                        resultado_inversa.config(text=f"Error: {str(e)}")

                boton_calcular = tk.Button(CA_Win, text="Calcular Inversa", command=calcular_inversa)
                boton_calcular.grid(row=4 + filas, column=0, columnspan=2, padx=10, pady=10)

            except ValueError as e:
                resultado_inversa.config(text=f"Error: {str(e)}")

        boton_generar = tk.Button(CA_Win, text="Generar Matriz", command=generar_matriz)
        boton_generar.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        resultado_inversa = tk.Label(CA_Win, text="")
        resultado_inversa.grid(row=4 + 10, column=0, columnspan=4, padx=10, pady=10)

        backButton()

    def multi():
        clean_buttons()
        instruccionMulti = tk.Label(CA_Win, text="Ingrese sus matrices: ")
        instruccionMulti.grid(row=0, column=5, columnspan=2, padx=10, pady=10)
        backButton()
        
    def sis_ecu_sub():
        def clean_buttons_sub1():
            instruccionMetodo.grid_forget()
            boton_cramer.grid_forget()
            boton_Gaus.grid_forget()
            boton_return_main.grid_forget()
            
        def sis_ecu_Gaus():
            clean_buttons_sub1()
            boton_return = tk.Button(CA_Win, text="Regresar", command=sis_ecu_sub)
            boton_return.grid(row=0, column=0, padx=10, pady=10)
            
        def sis_ecu_cramer():
            clean_buttons_sub1()
            boton_return = tk.Button(CA_Win, text="Regresar", command=sis_ecu_sub)
            boton_return.grid(row=0, column=0, padx=10, pady=10)

        instruccionMetodo = tk.Label(CA_Win, text="Seleccione el metodo a utilizar")
        instruccionMetodo.grid(row=0, column=5, columnspan=5, padx=10, pady=10)
        
        boton_Gaus = tk.Button(CA_Win, text="Metodo de Gauss-Jordan", command=sis_ecu_Gaus)
        boton_Gaus.grid(row=1, column=10, padx=10, pady=10)

        boton_cramer = tk.Button(CA_Win, text="Metodo de Cramer", command=sis_ecu_cramer)
        boton_cramer.grid(row=11, column=10, padx=10, pady=10)
        
        boton_return_main = tk.Button(CA_Win, text="Regresar", command=menu_principal)
        boton_return_main.grid(row=0, column=0, padx=10, pady=10)
        
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