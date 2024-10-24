import tkinter as tk
import Calculadora_Mate as CM
import Calculadora_Algebra as CA
import pygame
import os
from tkinter import ttk
carpeta_recursos = os.path.join(os.path.dirname(__file__), 'audiovisual')

# Ventana principal
ventana = tk.Tk()
ventana.title("Proyecto Final")
ventana.geometry("800x500")
ventana.resizable(0, 1)
ventana.iconbitmap(os.path.join(carpeta_recursos, 'logo.ico'))
ventana.config(bg="#498af2")
# Inicializa pygame para la reproducción de sonidos
pygame.mixer.init()

# Función para reproducir el sonido y cerrar la ventana
def reproducir_sonido_cerrar():
    pygame.mixer.music.load(os.path.join(carpeta_recursos, "persona.mp3"))
    pygame.mixer.music.play()
    ventana.after(2000, ventana.destroy)

# Funciones de navegación para las pantallas
def pantalla_inicio():
    home.grid(row=0, column=0, sticky="nsew")
    algebra_lineal.grid_forget()
    matematica_discreta.grid_forget()
    integrantes.grid_forget()
    
    boton1.grid(row=1, column=0, pady=10) 
    boton2.grid(row=2, column=0, pady=10)  
    boton_integrantes.grid(row=3, column=0, pady=10)  
    kill.place(x=700, y=400, width=50, height=40)

def pantalla_algebra():
    algebra_lineal.grid(row=0, column=0, sticky="nsew")
    home.grid_forget()
    matematica_discreta.grid_forget()
    integrantes.grid_forget()

    boton1.grid_forget()
    boton2.grid_forget()
    boton_integrantes.grid_forget()
    kill.place_forget()
    
    for widget in algebra_lineal.winfo_children():
        widget.destroy()
    CA.operaciones_Algebra(algebra_lineal, pantalla_inicio)

    boton_volver_algebra.grid(row=4, column=1, padx=10, pady=10)

def pantalla_matematica():
    matematica_discreta.grid(row=0, column=0, sticky="nsew")
    home.grid_forget()
    algebra_lineal.grid_forget()
    integrantes.grid_forget()

    boton1.grid_forget()
    boton2.grid_forget()
    boton_integrantes.grid_forget()
    kill.place_forget()

    for widget in matematica_discreta.winfo_children():
        widget.destroy()  # Limpia el contenido del frame
    CM.operaciones_matematica_discreta(matematica_discreta, pantalla_inicio)  # Llamar la función del segundo script
    
    boton_volver_matematica.grid(row=4, column=1, padx=10, pady=10)

def pantalla_integrantes():
    integrantes.grid(row=0, column=0, sticky="nsew")
    home.grid_forget()
    algebra_lineal.grid_forget()
    matematica_discreta.grid_forget()

    boton1.grid_forget()
    boton2.grid_forget()
    boton_integrantes.grid_forget()
    kill.place_forget()

    boton_volver_integrantes.grid(row=4, column=1, padx=10, pady=10)

# Definición de las pantallas
home = tk.Frame(ventana, bg="#498af2")  # Asegúrate de aplicar el color a todos los Frames
algebra_lineal = tk.Frame(ventana, bg="#498af2")
matematica_discreta = tk.Frame(ventana, bg="#498af2")
integrantes = tk.Frame(ventana, bg="#498af2")
frame_integrantes = tk.Frame(integrantes, bg="#498af2")
frame_integrantes.grid(row=0, column=0, padx=50, pady=20)

# Botones de navegación entre calculadoras
boton1 = tk.Button(ventana, activebackground="#4c6c9e", bg="#92bcff", text="Álgebra lineal",  font=("Times New Roman", 10),command=pantalla_algebra, width=30, height=3)
boton1.grid(row=1, column=0, padx=10, pady=10)

boton2 = tk.Button(ventana, activebackground="#4c6c9e", bg="#92bcff", text="Matemática discreta",  font=("Times New Roman", 10),command=pantalla_matematica, width=30, height=3)
boton2.grid(row=2, column=0, padx=10, pady=10) 

boton_integrantes = tk.Button(ventana, activebackground="#4c6c9e", bg="#92bcff", text="Integrantes",  font=("Times New Roman", 10), command=pantalla_integrantes, width=30, height=3)
boton_integrantes.grid(row=3, column=0, padx=10, pady=10)

# Label de bienvenida (centrado y en la parte superior)
bienvenida = tk.Label(home, bg="#498af2", text="Bienvenido, selecciona tu calculadora", font=("Times New Roman", 10))
bienvenida.grid(row=0, column=2, padx=310, pady=(20, 10), sticky="n")

# Botones para regresar a la pantalla principal
boton_volver_algebra = tk.Button(algebra_lineal, activebackground="#001a43", bg="#4e2193", text="Volver al Inicio", command=pantalla_inicio, width=25, height=3)
boton_volver_algebra.grid(row=4, column=1, padx=10, pady=10)

boton_volver_matematica = tk.Button(matematica_discreta, text="Volver al Inicio", command=pantalla_inicio)
boton_volver_matematica.grid(row=4, column=1, padx=10, pady=10)

boton_volver_integrantes = tk.Button(integrantes, activebackground="#001a43", bg="#4e2193", text="Volver al Inicio", command=pantalla_inicio, width=25, height=3)
boton_volver_integrantes.grid(row=4, column=0, padx=10, pady=50)

# Botón de cierre con imagen
icono = tk.PhotoImage(file=os.path.join(carpeta_recursos, "pistola.png"))
kill = tk.Button(ventana, activebackground="#001a43", bg="#4e2193", image=icono, command=reproducir_sonido_cerrar)
kill.place(x=700, y=400, width=50, height=40)

# contenido de la pantalla integrantes 
tree = ttk.Treeview(frame_integrantes, columns=("Nombre", "Carnet", "Rol"), show="headings", height=5)
tree.heading("Nombre", text="Nombre")
tree.heading("Carnet", text="Carnet")
tree.heading("Rol", text="Rol")
tree.column("Nombre", width=250)
tree.column("Carnet", width=120)
tree.column("Rol", width=300)

# Insertar datos en el Treeview
tree.insert("", "end", values=("Christopher Ricardo Garcia Giron", "0907-24-10087", "Líder de proyecto, Encargado de la intefaz principal"))
tree.insert("", "end", values=("Miguel José Alfaro Vásquez","0907-24-12948", "Encargado calculadora Matematica discreta,Decorador"))
tree.insert("", "end", values=("José Miguel Castillo Pérez","0907-24-1862", "Encargado calculadora algebra lineal"))
tree.insert("", "end", values=("Diego Alejandro Fernández González","0907-24-25569", "Encargado calculadora algebra lineal"))
tree.pack(padx=10, pady=50)

# Botón para regresar a la pantalla principal
boton_volver_integrantes = tk.Button(frame_integrantes, text="Volver al Inicio", command=pantalla_inicio)
boton_volver_integrantes.pack(pady=5)  # Colocamos el botón debajo del Treeview usando pack
#poyo 🐥
pantalla_inicio()

ventana.mainloop()
