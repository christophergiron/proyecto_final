#import Pantalla_principal as PP
import tkinter as tk
from tkinter import messagebox
import numpy as np
import sys
from fractions import Fraction
import matplotlib.pyplot as plt

CA_Win = tk.Tk()
CA_Win.title("Calculadora de matrices")
CA_Win.geometry("625x400")
frame_matriz = None
frame_matriz_M2 = None
boton_calcular = None
boton_calcular_cramer = None

#Menu principal
def menu_principal():
    for menu1 in CA_Win.winfo_children():
        menu1.destroy()
        
    #Funcion encargada del boton de regresar
    def backButton():
        boton_return = tk.Button(CA_Win, text="Regresar", command=menu_principal)
        boton_return.grid(row=0, column=0, padx=10, pady=10)

    #Funcion encargada de limpiar los botones tras cambiar de pestaña
    def clean_buttons():
        instruccion.grid_forget()
        boton.grid_forget()
        botonS.grid_forget()
        botonM.grid_forget()
        
    #Comienzo del codigo para obtener la matriz inversa
    def inversa():
        clean_buttons()
        instruccionInv = tk.Label(CA_Win, text="Ingrese el tamaño de la matriz: ")
        instruccionInv.grid(row=0, column=5, columnspan=2, padx=10, pady=10)

        # Entrada para el tamaño de la matriz
        fila_la1 = tk.Label(CA_Win, text="Filas: ")
        fila_la1.grid(row=1, column=0)
        fila_e1 = tk.Entry(CA_Win, width=5)
        fila_e1.grid(row=1, column=1)

        columna_la1 = tk.Label(CA_Win, text="Columnas: ")
        columna_la1.grid(row=2, column=0)
        columna_e2 = tk.Entry(CA_Win, width=5)
        columna_e2.grid(row=2, column=1)

        # Función para generar la matriz con los tamaños dados por el usuario
        def generar_matriz():
            global frame_matriz, boton_calcular

            # Si existe un frame de matriz previo, eliminarlo
            if frame_matriz is not None:
                frame_matriz.destroy()
                
                if boton_calcular is not None:
                    boton_calcular.destroy()
            try:
                # Captura las dimensiones de la matriz
                filas = int(fila_e1.get())
                columnas = int(columna_e2.get())

                # Verifica si el tamaño es válido (mayor que 1)
                if filas <= 1 | columnas <= 1:
                    messagebox.showerror("Error", "El tamaño debe ser mayor a 1.")
                else:
                    # Crear un nuevo frame para la matriz
                    frame_matriz = tk.Frame(CA_Win)
                    frame_matriz.grid(row=4, column=0, columnspan=columnas)

                    entradas_matriz = [] # Lista para almacenar las entradas de la matriz
                    # Genera las entradas para la matriz
                    for i in range(filas):
                        fila = []
                        for j in range(columnas):
                            entrada = tk.Entry(frame_matriz, width=5)
                            entrada.grid(row=i, column=j, padx=5, pady=5)
                            fila.append(entrada)
                        entradas_matriz.append(fila)

                    # Función para calcular la inversa de la matriz ingresada
                    def calcular_inversa():
                        try:
                            # Convierte los datos en una matriz
                            matriz = np.array([[float(entradas_matriz[i][j].get()) for j in range(columnas)] for i in range(filas)])
                            if filas != columnas:
                                resultado_inversa.config(text="La matriz no es cuadrada, no tiene inversa.")
                            else:
                                # Calcula la inversa de la matriz
                                matriz_inversa = np.linalg.inv(matriz)
                                resultado_inversa.config(text=f"Inversa de la matriz:\n{matriz_inversa}")
                            
                        except np.linalg.LinAlgError:
                            messagebox.showerror("Error","La matriz no es invertible.")
                        except Exception as e:
                            messagebox.showerror("Error", f"Error: {str(e)}")

                    # Botón para calcular la inversa
                    boton_calcular = tk.Button(CA_Win, text="Calcular Inversa", command=calcular_inversa)
                    boton_calcular.grid(row=4 + filas, column=0, columnspan=2, padx=10, pady=10)

            except ValueError as e:
                messagebox.showerror("Error", f"Error: {str(e)}")

        # Botón para generar la matriz
        boton_generar = tk.Button(CA_Win, text="Generar Matriz", command=generar_matriz)
        boton_generar.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        # Etiqueta para mostrar el resultado de la inversa
        resultado_inversa = tk.Label(CA_Win, text="")
        resultado_inversa.grid(row=4 + 10, column=0, columnspan=4, padx=10, pady=10)

        backButton() # Invoca la funcion del boton atras

    #Comienzo del codigo de la multiplicacion
    def multi():
        clean_buttons()
        instruccionMulti = tk.Label(CA_Win, text="Ingrese el tamaño de sus matrices: ")
        instruccionMulti.grid(row=0, column=1, columnspan=2, padx=10, pady=10)
        
        instruccionMulti_M1 = tk.Label(CA_Win, text="Primera Matriz")
        instruccionMulti_M1.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        
        instruccionMulti_M2 = tk.Label(CA_Win, text="Segunda Matriz")
        instruccionMulti_M2.grid(row=1, column=2, columnspan=2, padx=10, pady=10)
        
        fila_la1 = tk.Label(CA_Win, text="Filas: ")
        fila_la1.grid(row=2, column=0)
        fila_e1 = tk.Entry(CA_Win, width=5)
        fila_e1.grid(row=2, column=1)

        columna_la1 = tk.Label(CA_Win, text="Columnas: ")
        columna_la1.grid(row=3, column=0)
        columna_e1 = tk.Entry(CA_Win, width=5)
        columna_e1.grid(row=3, column=1)
        
        fila_la2 = tk.Label(CA_Win, text="Filas: ")
        fila_la2.grid(row=2, column=2)
        fila_e2 = tk.Entry(CA_Win, width=5)
        fila_e2.grid(row=2, column=3)

        columna_la2 = tk.Label(CA_Win, text="Columnas: ")
        columna_la2.grid(row=3, column=2)
        columna_e2 = tk.Entry(CA_Win, width=5)
        columna_e2.grid(row=3, column=3)
        
        #Genera la cuadricula de la matriz
        def generar_matriz():
            global frame_matriz, frame_matriz_M2, boton_calcular
            # Si existe un frame de matriz previo, eliminarlo
            if frame_matriz is not None:
                frame_matriz.destroy()
                
                if boton_calcular is not None:
                    boton_calcular.destroy()
                    
            if frame_matriz_M2 is not None:
                frame_matriz_M2.destroy()
                if boton_calcular is not None:
                    boton_calcular.destroy()
            try:
                # Captura los tamaños de ambas matrices
                filas = int(fila_e1.get())
                columnas = int(columna_e1.get())
                
                filas_M2 = int(fila_e2.get())
                columnas_M2 = int(columna_e2.get())

                # Verifica si los tamaños son válidos
                if filas <= 1 or columnas <= 1 or filas_M2 <= 1 or columnas_M2 <= 1:
                    messagebox.showerror("Error", "El tamaño debe ser mayor a 1.")
                else:
                    if filas != columnas_M2:
                        messagebox.showerror("Error", "Estas matrices no se pueden multiplicar!!!")
                    else:
                        # Crear un nuevo frame para la matriz
                        frame_matriz = tk.Frame(CA_Win)
                        frame_matriz.grid(row=4, column=0, columnspan=columnas)
                        
                        # Crear un nuevo frame para la segunda matriz
                        frame_matriz_M2 = tk.Frame(CA_Win)
                        frame_matriz_M2.grid(row=4, column=columnas+1, columnspan=columnas_M2)

                        entradas_matriz = []
                        for i in range(filas):
                            fila = []
                            for j in range(columnas):
                                entrada = tk.Entry(frame_matriz, width=5)
                                entrada.grid(row=i, column=j, padx=5, pady=5)
                                fila.append(entrada)
                            entradas_matriz.append(fila)
                            
                        entradas_matriz_2 = []
                        for i in range(filas_M2):
                            fila_2 = []
                            for j in range(columnas_M2):
                                entrada_2 = tk.Entry(frame_matriz_M2, width=5)
                                entrada_2.grid(row=i, column=j, padx=5, pady=5)
                                fila_2.append(entrada_2)
                            entradas_matriz_2.append(fila_2)
                            
                        # Función para calcular la multiplicación de matrices
                        def calculoEnSi():
                            try:
                                # Obtener los valores de las matrices ingresadas
                                matriz = np.array([[float(entradas_matriz[i][j].get()) for j in range(columnas)] for i in range(filas)])
                                matriz_M2 = np.array([[float(entradas_matriz_2[i][j].get()) for j in range(columnas_M2)] for i in range(filas_M2)])
                                
                                # Realizar la multiplicación de matrices (producto matricial)
                                resultado = np.dot(matriz, matriz_M2)
                                
                                # Mostrar el resultado en una nueva ventana o actualizar algún widget para mostrarlo
                                resultado_multi.config(text=f"Resultado:\n{resultado}")
                            except ValueError as e:
                                messagebox.showerror("Error", f"Error: {str(e)}")
                            except Exception as e:
                                messagebox.showerror("Error", f"Error inesperado: {str(e)}")

                    # Crear botón para calcular el producto de matrices
                    boton_calcular = tk.Button(CA_Win, text="Multiplicar", command=calculoEnSi)
                    boton_calcular.grid(row=6 + filas, column=1, columnspan=2, padx=10, pady=10)
                
            except ValueError as e:
                messagebox.showerror("Error", f"Error: {str(e)}")
                
        boton_generar = tk.Button(CA_Win, text="Generar Matriz", command=generar_matriz)
        boton_generar.grid(row=6, column=1, columnspan=2, padx=10, pady=10)

        resultado_multi = tk.Label(CA_Win, text="")
        resultado_multi.grid(row=4 + 10, column=0, columnspan=4, padx=10, pady=10)
                
        backButton()
        
    #Inicio del codigo del sistema de ecuaciones
    def sis_ecu_sub():
        metodo_frame = tk.Frame(CA_Win)
        
        def clean_buttons_sub1():
            instruccionMetodo.grid_forget()
            boton_cramer.grid_forget()
            boton_Gaus.grid_forget()
            boton_return_main.grid_forget()
        
        #Comienzo del metodo de gauss jordan
        def sis_ecu_Gaus():
            #limpia los botones dentro del submenu al cambiar de submenu
            clean_buttons_sub1()
            boton_return = tk.Button(CA_Win, text="Regresar", command=lambda: regresar())
            boton_return.grid(row=0, column=0, padx=10, pady=10)
            
            # Boton encargado de regresar al submenu anterior
            def regresar():
                clean_buttons_sub2_ga()
                resultado_label.config(text="")
                sis_ecu_sub()    
            
            #limpia los botones dentro del submenu al regresar al menu anterior
            def clean_buttons_sub2_ga():
                instruccionSize.grid_forget()
                boton_2x2.grid_forget()
                boton_3x3.grid_forget()
                boton_4x4.grid_forget()
                
                if frame_matriz is not None:
                    frame_matriz.destroy()
                    
                if boton_calcular is not None:
                    boton_calcular.destroy()
            
            def generar_matriz(filas, columnas):
                global frame_matriz, boton_calcular
                frame_matriz = tk.Frame(CA_Win)
                frame_matriz.grid(row=4, column=1, columnspan=columnas)
                
                entradas_matriz = []
                for i in range(filas):
                    fila = []
                    for j in range(columnas):
                        entrada = tk.Entry(frame_matriz, width=5)
                        entrada.grid(row=i, column=j, padx=5, pady=5)
                        fila.append(entrada)
                    entradas_matriz.append(fila)
                    
                boton_calcular = tk.Button(CA_Win, text="Calcular", command=lambda: calcular_solucion(entradas_matriz))
                boton_calcular.grid(row=6 + filas, column=1, columnspan=2, padx=5, pady=5)
            
            def calcular_solucion(entradas):
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
                    
                    boton_graficar = tk.Button(CA_Win, text="Mostrar Gráfica", command=lambda: mostrar_grafica(resultado))
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
            
            def doble():
                clean_buttons_sub2_ga()
                generar_matriz(2, 3)
                
            def triple():
                clean_buttons_sub2_ga()
                generar_matriz(3, 4)
                
            def cuadruple():
                clean_buttons_sub2_ga()
                generar_matriz(4, 5)
                
            
            instruccionSize = tk.Label(CA_Win, text="Seleccione el tamaño del sistema de ecuaciones")
            instruccionSize.grid(row=0, column=2, columnspan=4, padx=10, pady=10)
                
            boton_2x2 = tk.Button(CA_Win, text="2x2", command=doble)
            boton_2x2.grid(row=1, column=2, padx=10, pady=10)
            boton_3x3 = tk.Button(CA_Win, text="3x3", command=triple)
            boton_3x3.grid(row=1, column=3, padx=10, pady=10)
            boton_4x4 = tk.Button(CA_Win, text="4x4", command=cuadruple)
            boton_4x4.grid(row=1, column=4, padx=10, pady=10)
            
            resultado_label = tk.Label(CA_Win, text="")
            resultado_label.grid(row=7, column=1, columnspan=3, padx=10, pady=10)
            
        #Comienzo del metodo de cramer
        def sis_ecu_cramer():
            clean_buttons_sub1()
            
            def clean_buttons_sub2():
                instruccionSize.grid_forget()
                boton_2x2.grid_forget()
                boton_3x3.grid_forget()
                boton_4x4.grid_forget()
                
                if frame_matriz is not None:
                    frame_matriz.destroy()
                    
                if boton_calcular_cramer is not None:
                    boton_calcular_cramer.destroy()
                    
                resultado_label.config(text="")
                
            def generar_matriz(filas, columnas):
                global frame_matriz, boton_calcular_cramer
                clean_buttons_sub2()
                
                frame_matriz = tk.Frame(CA_Win)
                frame_matriz.grid(row=4, column=1, columnspan=columnas)

                entradas_matriz = []
                for i in range(filas):
                    fila = []
                    for j in range(columnas):
                        entrada = tk.Entry(frame_matriz, width=5)
                        entrada.grid(row=i, column=j, padx=5, pady=5)
                        fila.append(entrada)
                    entradas_matriz.append(fila)
                    
                boton_calcular_cramer = tk.Button(CA_Win, text="Calcular", command=lambda: calcular_solucion(entradas_matriz))
                boton_calcular_cramer.grid(row=6 + filas, column=1, columnspan=2, padx=5, pady=5)
                    
            def doble():
                generar_matriz(2, 3)
                
            def triple():
                generar_matriz(3, 4)
                
            def cuadruple():
                generar_matriz(4, 5)
                
            boton_return = tk.Button(CA_Win, text="Regresar", command=lambda: [clean_buttons_sub2(), sis_ecu_sub()])
            boton_return.grid(row=0, column=0, padx=10, pady=10)
            
            instruccionSize = tk.Label(CA_Win, text="Seleccione el tamaño del sistema de ecuaciones")
            instruccionSize.grid(row=0, column=2, columnspan=4, padx=10, pady=10)
                
            boton_2x2 = tk.Button(CA_Win, text="2x2", command=doble)
            boton_2x2.grid(row=1, column=2, padx=10, pady=10)
            boton_3x3 = tk.Button(CA_Win, text="3x3", command=triple)
            boton_3x3.grid(row=1, column=3, padx=10, pady=10)
            boton_4x4 = tk.Button(CA_Win, text="4x4", command=cuadruple)
            boton_4x4.grid(row=1, column=4, padx=10, pady=10)
            
            resultado_label = tk.Label(CA_Win, text="")
            resultado_label.grid(row=7, column=1, columnspan=3, padx=10, pady=10)
            
            def calcular_solucion(entradas):
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
                    
                except Exception as e:
                    messagebox.showerror("Error", f"Error al calcular la solución: {str(e)}")

        #Menu del sistema de ecuaciones
        instruccionMetodo = tk.Label(CA_Win, text="Seleccione el metodo a utilizar")
        instruccionMetodo.grid(row=0, column=5, columnspan=5, padx=10, pady=10)
        
        boton_Gaus = tk.Button(CA_Win, text="Metodo de Gauss-Jordan", command=sis_ecu_Gaus)
        boton_Gaus.grid(row=1, column=10, padx=10, pady=10)

        boton_cramer = tk.Button(CA_Win, text="Metodo de Cramer", command=sis_ecu_cramer)
        boton_cramer.grid(row=11, column=10, padx=10, pady=10)
        
        boton_return_main = tk.Button(CA_Win, text="Regresar", command=menu_principal)
        boton_return_main.grid(row=0, column=0, padx=10, pady=10)
        
        metodo_frame.grid(row=1, column=0)

    # Encargado de iniciar el submuenu para seleccionar metodos en el sistema de ecuaciones      
    def sis_ecu():
        clean_buttons()
        backButton()
        for menu2 in CA_Win.winfo_children():
            menu2.destroy()
        sis_ecu_sub()

    # Funciones para cada opción del menú principal
    instruccion = tk.Label(CA_Win, text="Seleccione la operacion a realizar: ")
    instruccion.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    boton = tk.Button(CA_Win, text="Matriz inversa", command=inversa)
    boton.grid(row=1, column=8, padx=10, pady=10)

    botonM = tk.Button(CA_Win, text="Multiplicacion", command=multi)
    botonM.grid(row=11, column=8, padx=10, pady=10)

    botonS = tk.Button(CA_Win, text="Sistemas de ecuaciones lineales", command=sis_ecu)
    botonS.grid(row=21, column=8, padx=10, pady=10)

#Cangrejo en el codigo 🦀
menu_principal()
CA_Win.mainloop()