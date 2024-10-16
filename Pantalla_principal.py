import tkinter as tk
import Calculadora_Mate as CM 
import pygame
import os
carpeta_recursos = os.path.join(os.path.dirname(__file__), 'audiovisual')

# Ventana principal
ventana = tk.Tk()
ventana.title("Proyecto Final")
ventana.geometry("600x500")
ventana.resizable(0, 0)
ventana.iconbitmap(os.path.join(carpeta_recursos, 'logo.ico'))

# Inicializa pygame la reproduccion de sonidos
pygame.mixer.init()

# Función para reproducir el sonido y cerrar la ventana
def reproducir_sonido_cerrar():
    pygame.mixer.music.load(os.path.join(carpeta_recursos, "persona.mp3"))
    pygame.mixer.music.play()
    ventana.after(2500, ventana.destroy)

# Funciones de navegación
def pantalla_inicio():
    home.grid()
    algebra_lineal.grid_forget()
    matematica_discreta.grid_forget()
    integrantes.grid_forget()
    
    boton1.place(x=250, y=60, width=120, height=25)
    boton2.place(x=250, y=90, width=120, height=25)
    boton_integrantes.place(x=250, y=120, width=120, height=25)
    kill.place(x=500, y=400, width=50, height=40)

def pantalla_algebra():
    algebra_lineal.grid()
    home.grid_forget()
    matematica_discreta.grid_forget()
    integrantes.grid_forget()

    boton1.place_forget()
    boton2.place_forget()
    boton_integrantes.place_forget()
    kill.place_forget()

    boton_volver_algebra.grid(row=4, column=1, padx=10, pady=10)

def pantalla_matematica():
    matematica_discreta.grid()
    home.grid_forget()
    algebra_lineal.grid_forget()
    integrantes.grid_forget()

    boton1.place_forget()
    boton2.place_forget()
    boton_integrantes.place_forget()
    kill.place_forget()

    for widget in matematica_discreta.winfo_children():
        widget.destroy()  # Limpia el contenido del frame
    CM.operaciones_matematica_discreta(matematica_discreta, pantalla_inicio)  # Llamar la función del segundo script

    boton_volver_matematica.grid(row=4, column=1, padx=10, pady=10)

def pantalla_integrantes():
    integrantes.grid()
    home.grid_forget()
    algebra_lineal.grid_forget()
    matematica_discreta.grid_forget()

    boton1.place_forget()
    boton2.place_forget()
    boton_integrantes.place_forget()
    kill.place_forget()

    boton_volver_integrantes.grid(row=4, column=1, padx=10, pady=10)
    
# Definición de las pantallas
home = tk.Frame(ventana)
algebra_lineal = tk.Frame(ventana)
matematica_discreta = tk.Frame(ventana)
integrantes = tk.Frame(ventana)

# Botones de navegación entre calculadoras (Inicio eliminado)
boton1 = tk.Button(ventana, text="Álgebra lineal", command=pantalla_algebra)
boton1.place(x=250, y=60, width=120, height=25)

boton2 = tk.Button(ventana, text="Matemática discreta", command=pantalla_matematica)
boton2.place(x=250, y=90, width=120, height=25)

boton_integrantes = tk.Button(ventana, text="Integrantes", command=pantalla_integrantes)
boton_integrantes.place(x=250, y=120, width=120, height=25)

# Label de bienvenida
bienvenida = tk.Label(home, text="Bienvenido, selecciona tu calculadora", font=("Times New Roman", 12))
bienvenida.grid(row=0, column=2, padx=200, pady=20)

# Botones para regresar a la pantalla principal
boton_volver_algebra = tk.Button(algebra_lineal, text="Volver al Inicio", command=pantalla_inicio)
boton_volver_algebra.grid(row=4, column=1, padx=10, pady=10)

boton_volver_matematica = tk.Button(matematica_discreta, text="Volver al Inicio", command=pantalla_inicio)
boton_volver_matematica.grid(row=4, column=1, padx=10, pady=10)

boton_volver_integrantes = tk.Button(integrantes, text="Volver al Inicio", command=pantalla_inicio)
boton_volver_integrantes.grid(row=4, column=1, padx=10, pady=10)

# Botón de cierre con imagen
icono = tk.PhotoImage(file=os.path.join(carpeta_recursos, "pistola.png"))
kill = tk.Button(ventana, image=icono, command=reproducir_sonido_cerrar)
kill.place(x=500, y=400, width=50, height=40)

# Inicia la pantalla principal
pantalla_inicio()

# Ejecuta el bucle principal
ventana.mainloop()
