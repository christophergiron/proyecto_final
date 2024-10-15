import tkinter as tk
import Calculadora_Mate as CM  # Asegúrate de que este sea el nombre correcto del archivo donde tienes las operaciones
import pygame
ventana = tk.Tk()
ventana.title("Proyecto Final")
ventana.geometry("600x500")
ventana.resizable(0,0)

pygame.mixer.init()

def reproducir_sonido_cerrar():
    pygame.mixer.music.load("persona.mp3")
    pygame.mixer.music.play()
    ventana.after(2500, ventana.destroy)

def pantalla_inicio():
    home.grid()
    algebra_lineal.grid_forget()
    matematica_discreta.grid_forget()

    boton1.place(x=250, y=70, width=120, height=25)
    boton2.place(x=250, y=100, width=120, height=25)
    boton3.place(x=250, y=130, width=120, height=25)
    
def pantalla_algebra():
    algebra_lineal.grid()
    home.grid_forget()
    matematica_discreta.grid_forget()
    boton1.place_forget()
    boton2.place_forget()
    boton3.place_forget()
    boton_volver_algebra.grid(row=4, column=1, padx=10, pady=10)
    
def pantalla_matematica():
    matematica_discreta.grid()
    home.grid_forget()
    algebra_lineal.grid_forget()
    boton1.place_forget()
    boton2.place_forget()
    boton3.place_forget()
    for widget in matematica_discreta.winfo_children():
        widget.destroy()  # Limpia el contenido del frame
    CM.operaciones_matematica_discreta(matematica_discreta, pantalla_inicio)   # Llamar la función del segundo script
    boton_volver_matematica.grid(row=4, column=1, padx=10, pady=10)
        
home = tk.Frame(ventana)
algebra_lineal = tk.Frame(ventana)
matematica_discreta = tk.Frame(ventana)

boton1 = tk.Button(ventana, text="Inicio", command=pantalla_inicio)
boton1.place(x=250, y=70, width=120, height=25)

boton2 = tk.Button(ventana, text="Álgebra lineal", command=pantalla_algebra)
boton2.place(x=250, y=100, width=120, height=25)

boton3 = tk.Button(ventana, text="Matemática discreta", command=pantalla_matematica)
boton3.place(x=250, y=130, width=120, height=25)

bienvenida = tk.Label(home, text="Bienvenido, selecciona tu calculadora", font=("Times New Roman", 12))
bienvenida.grid(row=0, column=2, padx=200, pady=20)

boton_volver_algebra = tk.Button(algebra_lineal, text="Volver al Inicio", command=pantalla_inicio)
boton_volver_algebra.grid(row=4, column=1, padx=10, pady=10)

boton_volver_matematica = tk.Button(matematica_discreta, text="Volver al Inicio", command=pantalla_inicio)
boton_volver_matematica.grid(row=4, column=1, padx=10, pady=10)

icono = tk.PhotoImage(file="pistola.png")
kill = tk.Button(ventana, image=icono, command=reproducir_sonido_cerrar)
kill.place(x=500, y=400, width=50, height=40)

pantalla_inicio()

ventana.mainloop()
