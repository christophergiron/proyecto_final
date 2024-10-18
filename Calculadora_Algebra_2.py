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

boton_calcular = None
boton_graficar = None
resultado_label = None
entradas_matriz = []

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
    global boton_calcular, boton_graficar
    frame_calc_gauss.grid()
    frame_pantalla_sis_ecuaciones.grid_forget()
    frame_Pantalla_Minversa.grid_forget()
    frame_pantalla_Multiplicacion.grid_forget()
    Pan_principal.grid_forget()
    frame_calc_cramer.grid_forget()

    boton_inversa.grid_forget()
    boton_Multi.grid_forget() 
    boton_sis_ecuaciones.grid_forget()
    sis_ecu_Gaus()

def sis_ecu_Gaus():
    global boton_calcular, boton_graficar, entradas_matriz, resultado_label

    def limpiar_matriz():
        # Eliminar todas las entradas anteriores
        for fila in entradas_matriz:
            for entrada in fila:
                entrada.destroy()
        entradas_matriz.clear()

    def limpiar_resultado_y_boton():
        # Limpiar el resultado anterior
        resultado_label.config(text="")
        # Si hay un botón de graficar, lo eliminamos
        if boton_graficar is not None:
            boton_graficar.destroy()

    def generar_matriz(filas, columnas):
        global boton_calcular, boton_graficar, entradas_matriz
        limpiar_matriz()  # Limpiar cualquier matriz previa
        limpiar_resultado_y_boton()  # Limpiar el resultado y botón previo
        
        entradas_matriz = []
        for i in range(filas):
            fila = []
            for j in range(columnas):
                entrada = tk.Entry(frame_calc_gauss, width=5)
                entrada.grid(row=i + 2, column=j + 2, padx=5, pady=5)
                fila.append(entrada)
            entradas_matriz.append(fila)
        
        if boton_calcular is not None:
            boton_calcular.destroy()

        boton_calcular = tk.Button(frame_calc_gauss, text="Calcular", command=lambda: calcular_solucion(entradas_matriz))
        boton_calcular.grid(row=6 + filas, column=1, columnspan=2, padx=5, pady=5)

    def calcular_solucion(entradas):
        limpiar_resultado_y_boton()  # Limpiar cualquier resultado y botón anterior
        try:
            matriz = np.array([[float(entradas[i][j].get()) for j in range(len(entradas[0]))] for i in range(len(entradas))])
            filas, columnas = matriz.shape
            argumento = np.hstack((matriz[:, :-1], matriz[:, -1].reshape(-1, 1)))
            
            for i in range(filas):
                pivot = argumento[i, i]
                if pivot == 0:
                    messagebox.showerror("Error", "El sistema no tiene solución única.")
                    return
                argumento[i] = argumento[i] / pivot
                
                for j in range(filas):
                    if j != i:
                        argumento[j] -= argumento[j, i] * argumento[i]
                        
            resultado = argumento[:, -1]
            resultado_label.config(text=f"Solución:\n{resultado}")
            
            # Crear botón de graficar solo si el cálculo fue exitoso
            global boton_graficar
            boton_graficar = tk.Button(frame_calc_gauss, text="Mostrar Gráfica", command=lambda: mostrar_grafica(resultado))
            boton_graficar.grid(row=8, column=1, columnspan=2, padx=5, pady=5)
            
        except Exception as e:
            messagebox.showerror("Error", f"Error al calcular la solución: {str(e)}")
    
    def mostrar_grafica(resultado):
        plt.close('all')  # Cerrar cualquier gráfica previa
        if len(resultado) == 2:
            x_vals = np.linspace(-10, 10, 100)
            y_vals = resultado[0] * x_vals + resultado[1]
            
            plt.plot(x_vals, y_vals, label='Solución del sistema')
            plt.xlabel('X')
            plt.ylabel('Y')
            plt.title('Gráfica del sistema 2x2')
            plt.legend()
            plt.grid(True)
            plt.show()
        elif len(resultado) == 3:
            
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            
            x_vals = np.linspace(-10, 10, 100)
            y_vals = np.linspace(-10, 10, 100)
            X, Y = np.meshgrid(x_vals, y_vals)
            Z = resultado[0] * X + resultado[1] * Y + resultado[2]
            
            ax.plot_surface(X, Y, Z, cmap='viridis')
            ax.set_xlabel('X')
            ax.set_ylabel('Y')
            ax.set_zlabel('Z')
            plt.title('Gráfica del sistema 3x3')
            plt.show()

    # Botones para seleccionar el tamaño de la matriz
    instruccionSize = tk.Label(frame_calc_gauss, text="Seleccione el tamaño del sistema de ecuaciones")
    instruccionSize.grid(row=0, column=2, columnspan=4, padx=10, pady=10)
        
    boton_2x2 = tk.Button(frame_calc_gauss, text="2x2", command=lambda: generar_matriz(2, 3))
    boton_2x2.grid(row=1, column=2, padx=10, pady=10)
    boton_3x3 = tk.Button(frame_calc_gauss, text="3x3", command=lambda: generar_matriz(3, 4))
    boton_3x3.grid(row=1, column=3, padx=10, pady=10)
    boton_4x4 = tk.Button(frame_calc_gauss, text="4x4", command=lambda: generar_matriz(4, 5))
    boton_4x4.grid(row=1, column=4, padx=10, pady=10)
    
    boton_regresar_gaus = tk.Button(frame_calc_gauss, text=("regresar"), command=pantalla_Sis_ecuaciones)
    boton_regresar_gaus.grid(row=0, column=0, padx=5, pady=5)
    
    resultado_label = tk.Label(frame_calc_gauss, text="")
    resultado_label.grid(row=7, column=1, columnspan=3, padx=10, pady=10)
    
# Definición de botones en la pantalla principal
boton_inversa = tk.Button(Frame2, text="Matriz Inversa",font=("Times New Roman", 10),command=pantalla_Minversa, width=30, height=3)
boton_inversa.grid(row=2, column=1, padx=10, pady=10)
    
boton_Multi = tk.Button(Frame2, text="Multiplicacion de matrices",font=("Times New Roman", 10),command=pantalla_Multiplicacion, width=30, height=3)
boton_Multi.grid(row=3, column=1, padx=10, pady=10)

boton_sis_ecuaciones = tk.Button(Frame2, text="Sistema De Ecuaciones,",font=("Times New Roman", 10),command=pantalla_Sis_ecuaciones,width=30, height=3)
boton_sis_ecuaciones.grid(row=4, column=1, padx=10, pady=10)

boton_calc_gauss = tk.Button(frame_pantalla_sis_ecuaciones, text="Metodo de Gauss Jordan",font=("Times New Roman", 10), command=Calculadora_gauss,width=30, height=3)
boton_calc_gauss.grid(row=2, column=1, padx=10, pady=10)

boton_calc_cramer = tk.Button(frame_pantalla_sis_ecuaciones,text="Metodo de Cramer",font=("Times New Roman", 10),command=lambda: None,width=30, height=3)
boton_calc_cramer.grid(row=3, column=1, padx=10, pady=10)

pantalla_principal
Frame2.mainloop()
