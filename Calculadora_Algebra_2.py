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
boton_calcular_cramer = None
boton_graficar_cramer = None
resultado_label = None
entradas_matriz = []

def limpiar_frame(frame, except_widgets=[]):
    """Eliminar todos los widgets de un frame, excepto los que se especifiquen."""
    for widget in frame.winfo_children():
        if widget not in except_widgets:
            widget.destroy()
        
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
    Calculadora_inversa()
    
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
    sis_ecu_cramer()
def Calculadora_inversa():
    # Etiqueta de instrucciones
    instruccion_inversa = tk.Label(frame_Pantalla_Minversa, text="Ingrese las dimensiones de su matriz")
    instruccion_inversa.grid(row=0, column=1, columnspan=2, padx=10, pady=10)

    # Etiquetas y entradas para filas
    filas_label = tk.Label(frame_Pantalla_Minversa, text="Filas:")
    filas_label.grid(row=1, column=0, padx=10, pady=5)
    filas_entry = tk.Entry(frame_Pantalla_Minversa, width=3)  # Ajustar tamaño
    filas_entry.grid(row=1, column=1, padx=10, pady=5)

    # Etiquetas y entradas para columnas
    columnas_label = tk.Label(frame_Pantalla_Minversa, text="Columnas:")
    columnas_label.grid(row=2, column=0, padx=10, pady=5)
    columnas_entry = tk.Entry(frame_Pantalla_Minversa, width=3)  # Ajustar tamaño
    columnas_entry.grid(row=2, column=1, padx=10, pady=5)

    # Botón para generar la matriz
    boton_generar_matriz = tk.Button(frame_Pantalla_Minversa, text="Generar Matriz",
                                      command=lambda: generar_matriz(filas_entry.get(), columnas_entry.get(), boton_regresar, boton_generar_matriz, instruccion_inversa, filas_label, filas_entry, columnas_label, columnas_entry))
    boton_generar_matriz.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    # Botón de regresar a la pantalla principal
    boton_regresar = tk.Button(frame_Pantalla_Minversa, text="Regresar", command=pantalla_principal)
    boton_regresar.grid(row=0, column=0, padx=10, pady=10)

def generar_matriz(filas, columnas, boton_regresar, boton_generar_matriz, instruccion_inversa, filas_label, filas_entry, columnas_label, columnas_entry):
    # Validación para que las entradas sean numéricas
    try:
        filas = int(filas)
        columnas = int(columnas)
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese valores numéricos.")
        return

    # Limpiar el frame, excepto los controles de entrada, las etiquetas y los botones
    limpiar_frame(frame_Pantalla_Minversa, excepciones=[boton_regresar, boton_generar_matriz, instruccion_inversa, filas_label, filas_entry, columnas_label, columnas_entry])

    matriz_entries = []

    # Generación de entradas para cada celda de la matriz
    for i in range(filas):
        row_entries = []
        for j in range(columnas):
            entry = tk.Entry(frame_Pantalla_Minversa, width=5)
            entry.grid(row=i + 3, column=j + 3, padx=5, pady=5)
            row_entries.append(entry)
        matriz_entries.append(row_entries)

    # Comprobar si la matriz es cuadrada para habilitar el cálculo de la inversa
    if filas == columnas:
        boton_calcular_inversa = tk.Button(frame_Pantalla_Minversa, text="Calcular Matriz Inversa",
                                           command=lambda: calcular_inversa(filas, matriz_entries))
        boton_calcular_inversa.grid(row=filas + 4, column=0, columnspan=columnas, padx=10, pady=10)
    else:
        messagebox.showwarning("Advertencia", "La matriz debe ser cuadrada para calcular la inversa.")

def limpiar_frame(frame, excepciones=[]):
    # Eliminar todos los widgets en el frame excepto aquellos en la lista de excepciones
    for widget in frame.winfo_children():
        if widget not in excepciones:
            widget.grid_forget()

def calcular_inversa(tamano, matriz_entries):
    try:
        matriz = np.zeros((tamano, tamano))
        for i in range(tamano):
            for j in range(tamano):
                matriz[i, j] = float(matriz_entries[i][j].get())

        matriz_inversa = np.linalg.inv(matriz)
        mostrar_resultado(matriz_inversa, tamano)
    except np.linalg.LinAlgError:
        messagebox.showerror("Error", "La matriz no es invertible.")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")

def mostrar_resultado(matriz_inversa, tamano):
    # Mostramos los resultados justo debajo de la matriz ingresada
    tk.Label(frame_Pantalla_Minversa, text="Matriz Inversa:").grid(row=tamano + 5, column=0, columnspan=tamano, padx=10, pady=10)

    # Mostramos los valores de la matriz inversa debajo de la matriz original
    for i in range(matriz_inversa.shape[0]):
        for j in range(matriz_inversa.shape[1]):
            tk.Label(frame_Pantalla_Minversa, text=f"{matriz_inversa[i, j]:.2f}").grid(row=i + tamano + 6, column=j, padx=5, pady=5)


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
        plt.close('all')

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
    
def sis_ecu_cramer():
    global boton_calcular_cramer, boton_graficar, entradas_matriz, resultado_label
    
    def limpiar_matriz_cra():
        # Eliminar todas las entradas anteriores
        for fila in entradas_matriz:
            for entrada in fila:
                entrada.destroy()
        entradas_matriz.clear()

    def limpiar_resultado_y_boton_cra():
        # Limpiar el resultado anterior
        resultado_label.config(text="")
        # Si hay un botón de graficar, lo eliminamos
        if boton_graficar is not None:
            boton_graficar.destroy()
        plt.close('all')
        
    def generar_matriz_cra(filas, columnas):
        global boton_calcular_cramer, boton_graficar, entradas_matriz
        limpiar_matriz_cra()  # Limpiar cualquier matriz previa
        limpiar_resultado_y_boton_cra()  # Limpiar el resultado y botón previo

        entradas_matriz = []
        for i in range(filas):
            fila = []
            for j in range(columnas):
                entrada = tk.Entry(frame_calc_cramer, width=5)
                entrada.grid(row=i +2, column=j + 2, padx=5, pady=5)
                fila.append(entrada)
            entradas_matriz.append(fila)
            
        if boton_calcular_cramer is not None:
            boton_calcular_cramer.destroy()
            
        boton_calcular_cramer = tk.Button(frame_calc_cramer, text="Calcular", command=lambda: calcular_solucion(entradas_matriz))
        boton_calcular_cramer.grid(row=6 + filas, column=1, columnspan=2, padx=5, pady=5)
           
    def calcular_solucion(entradas):
        limpiar_resultado_y_boton_cra()
        try:
            matriz = np.array([[float(entradas[i][j].get()) for j in range(len(entradas[0]))] for i in range(len(entradas))])
            filas, columnas = matriz.shape
            
            if filas != columnas - 1:
                messagebox.showerror("Error", "La matriz no tiene un formato válido.")
                return
            
            A = matriz[:, :-1]
            b = matriz[:, -1]
            
            det_A = np.linalg.det(A)
            if det_A == 0:
                messagebox.showerror("Error", "El sistema no tiene solución única.")
                return
            
            soluciones = []
            for i in range(len(b)):
                Ai = np.copy(A)
                Ai[:, i] = b
                det_Ai = np.linalg.det(Ai)
                solucion = det_Ai / det_A
                soluciones.append(Fraction(solucion).limit_denominator())
                
            soluciones_str = ', '.join([str(sol) for sol in soluciones])
            resultado_label.config(text=f"Solución:\n{soluciones_str}")
            
            global boton_graficar_cramer
            boton_graficar_cramer = tk.Button(frame_calc_gauss, text="Mostrar Gráfica", command=lambda: mostrar_grafica(soluciones_str))
            boton_graficar_cramer.grid(row=8, column=1, columnspan=2, padx=5, pady=5)
            
        except Exception as e:
            messagebox.showerror("Error", f"Error al calcular la solución: {str(e)}")
            
    def mostrar_grafica(soluciones_str):
        if len(soluciones_str) == 2:
            x_vals = np.linspace(-10, 10, 100)
            y_vals = soluciones_str[0] * x_vals + soluciones_str[1]
            
            plt.plot(x_vals, y_vals, label='Solución del sistema')
            plt.xlabel('X')
            plt.ylabel('Y')
            plt.title('Gráfica del sistema 2x2')
            plt.legend()
            plt.grid(True)
            plt.show()
        elif len(soluciones_str) == 3:
            
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            
            x_vals = np.linspace(-10, 10, 100)
            y_vals = np.linspace(-10, 10, 100)
            X, Y = np.meshgrid(x_vals, y_vals)
            Z = soluciones_str[0] * X + soluciones_str[1] * Y + soluciones_str[2]
            
            ax.plot_surface(X, Y, Z, cmap='viridis')
            ax.set_xlabel('X')
            ax.set_ylabel('Y')
            ax.set_zlabel('Z')
            plt.title('Gráfica del sistema 3x3')
            plt.show()

    instruccionSize = tk.Label(frame_calc_cramer, text="Seleccione el tamaño del sistema de ecuaciones")
    instruccionSize.grid(row=0, column=2, columnspan=4, padx=10, pady=10)
        
    boton_2x2 = tk.Button(frame_calc_cramer, text="2x2", command=lambda: generar_matriz_cra(2, 3))
    boton_2x2.grid(row=1, column=2, padx=10, pady=10)
    boton_3x3 = tk.Button(frame_calc_cramer, text="3x3", command=lambda: generar_matriz_cra(3, 4))
    boton_3x3.grid(row=1, column=3, padx=10, pady=10)
    boton_4x4 = tk.Button(frame_calc_cramer, text="4x4", command=lambda: generar_matriz_cra(4, 5))
    boton_4x4.grid(row=1, column=4, padx=10, pady=10)
    
    boton_regresar_cramer = tk.Button(frame_calc_cramer, text=("regresar"), command=pantalla_Sis_ecuaciones)
    boton_regresar_cramer.grid(row=0, column=0, padx=5, pady=5)
    
    resultado_label = tk.Label(frame_calc_cramer, text="")
    resultado_label.grid(row=7, column=1, columnspan=3, padx=10, pady=10)
    
# Definición de botones en la pantalla principal
boton_inversa = tk.Button(Frame2, text="Matriz Inversa",font=("Times New Roman", 10),command=pantalla_Minversa, width=30, height=3)
boton_inversa.grid(row=2, column=1, padx=10, pady=10)
    
boton_Multi = tk.Button(Frame2, text="Multiplicacion de matrices",font=("Times New Roman", 10),command=pantalla_Multiplicacion, width=30, height=3)
boton_Multi.grid(row=3, column=1, padx=10, pady=10)

boton_sis_ecuaciones = tk.Button(Frame2, text="Sistema De Ecuaciones",font=("Times New Roman", 10),command=pantalla_Sis_ecuaciones,width=30, height=3)
boton_sis_ecuaciones.grid(row=4, column=1, padx=10, pady=10)

boton_calc_gauss = tk.Button(frame_pantalla_sis_ecuaciones, text="Metodo de Gauss Jordan",font=("Times New Roman", 10), command=Calculadora_gauss,width=30, height=3)
boton_calc_gauss.grid(row=2, column=1, padx=10, pady=10)

boton_calc_cramer = tk.Button(frame_pantalla_sis_ecuaciones,text="Metodo de Cramer",font=("Times New Roman", 10),command=Calculadora_cramer,width=30, height=3)
boton_calc_cramer.grid(row=3, column=1, padx=10, pady=10)

#👍︎♒︎❒︎♓︎⬧︎ ●︎□︎ ♋︎♍︎♏︎◻︎⧫︎□︎ ⬧︎□︎⍓︎ ◆︎■︎ ⧫︎❒︎♏︎❍︎♏︎■︎♎︎□︎ ♓︎♎︎♓︎□︎⧫︎♋︎ ◻︎□︎❒︎ ■︎□︎ ♒︎♋︎♌︎♏︎❒︎ ◆︎⬧︎♋︎♎︎□︎ ☝︎🏱︎❄︎ ♍︎□︎❍︎□︎ ❒︎♏︎⬧︎◻︎♋︎●︎♎︎□︎ ◻︎♋︎❒︎♋︎ ❍︎♓︎ ❍︎♋︎♐︎◆︎♐︎♋︎♎︎♋︎ ⍓︎ ■︎□︎ ◻︎□︎■︎♏︎❒︎❍︎♏︎ ♋︎ ❖︎♏︎❒︎ ♏︎🙰♏︎❍︎◻︎●︎□︎⬧︎ ◻︎♋︎❒︎♋︎ ♒︎♋︎♍︎♏︎❒︎●︎□︎ ♎︎♏︎ ♐︎□︎❒︎❍︎♋︎ ❍︎♋︎⬧︎ ♏︎♐︎♓︎♍︎♓︎♏︎■︎⧫︎♏︎ ◻︎♏︎❒︎□︎ ■︎□︎ ⬧︎♏︎ ◻︎◆︎♏︎♎︎♏︎ ♎︎♏︎♍︎♓︎❒︎ ❑︎◆︎♏︎ ■︎□︎ ⧫︎❒︎♋︎♌︎♋︎🙰♏︎ ⧫︎♋︎❍︎◻︎□︎♍︎□︎ ◻︎□︎❒︎❑︎◆︎♏︎ ♋︎ ◻︎♏︎⬧︎♋︎❒︎ ♎︎♏︎ ⧫︎□︎♎︎□︎ ⬧︎♋︎❑︎◆︎♏︎ ♋︎♎︎♏︎●︎♋︎■︎⧫︎♏︎ ●︎♋︎⬧︎ ♍︎□︎⬧︎♋︎⬧︎ ♋︎ ♍︎□︎❍︎□︎ ◻︎□︎♎︎í♋︎📪︎ ♑︎❒︎♋︎♍︎♓︎♋︎⬧︎ ◻︎□︎❒︎ ⧫︎□︎♎︎♋︎ ●︎♋︎ ♋︎⍓︎◆︎♎︎♋︎ ♏︎■︎⬧︎♏︎❒︎♓︎□︎ ◻︎♋︎❒︎♋︎ ♋︎❒︎❒︎♏︎♑︎●︎♋︎❒︎ ♏︎⬧︎⧫︎♋︎ ♍︎□︎⬧︎♋︎ ⍓︎ ❖︎♏︎⌘︎ ♍︎□︎❍︎□︎ ♒︎♋︎♍︎♏︎❒︎ ❍︎□︎♎︎⬧︎ ⍓︎ ♏︎⬧︎♍︎❒︎♓︎♌︎♓︎❒︎ ♍︎ó♎︎♓︎♑︎□︎ ♎︎♏︎⬧︎♎︎♏︎ 📁︎ ■︎□︎ ♏︎⬧︎ ♓︎♑︎◆︎♋︎●︎ 🙰♋︎🙰♋︎🙰♋︎ ♎︎♏︎ ❖︎♏︎❒︎♎︎♋︎♎︎ ❍︎◆︎♍︎♒︎♋︎⬧︎ ♑︎❒︎♋︎♍︎♓︎♋︎⬧︎ ♋︎◆︎■︎❑︎◆︎♏︎ ❍︎♏︎ ❑︎◆︎♏︎🙰♏︎ ❍︎◆︎♍︎♒︎□︎ ♋︎♍︎♏︎◻︎⧫︎□︎ ❑︎◆︎♏︎ ⬧︎□︎⬧︎ ◆︎■︎ ♌︎◆︎♏︎■︎ ●︎í♎︎♏︎❒︎ ⍓︎ ♎︎♏︎ ❖︎♏︎❒︎♎︎♋︎♎︎ ⧫︎♏︎ ♋︎◻︎❒︎♏︎♍︎♓︎□︎ ◆︎■︎ ♍︎♒︎♓︎■︎♑︎□︎ ♍︎□︎❍︎□︎ ♋︎❍︎♓︎♑︎□︎ ♎︎♏︎ ■︎◆︎♏︎❖︎□︎ ♑︎❒︎♋︎♍︎♓︎♋︎⬧︎📬︎
#Cangrejo en el codigo? Donde esta pipipi
pantalla_principal
Frame2.mainloop()