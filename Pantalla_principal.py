import tkinter as tk
import Calculadora_Mate as CM

ventana = tk.Tk()
ventana.title("proyecto final")
ventana.geometry("600x500")
ventana.config()

def pantalla_inicio():
    home.grid()
    algebra_lineal.grid_forget()
    matematica_discreta.grid_forget()

def pantalla_algebra():
    algebra_lineal.grid()
    home.grid_forget()
    matematica_discreta.grid_forget()
    boton1.place_forget()
    boton2.place_forget()
    boton3.place_forget()

def pantalla_matematica():
    matematica_discreta.grid()
    home.grid_forget()
    algebra_lineal.grid_forget()
    boton1.place_forget()
    boton2.place_forget()
    boton3.place_forget()

    # limpia cualquier cosa en el frame para agregar correctamente los del script de matematica
    for widget in matematica_discreta.winfo_children():
        widget.destroy() #limpia el contenido del frame
    CM.operaciones_matematica_discreta(matematica_discreta) #se carga la funcion del script de matematica

home = tk.Frame(ventana)
algebra_lineal = tk.Frame(ventana)
matematica_discreta = tk.Frame(ventana)

boton1 = tk.Button(ventana, text="Inicio", command=pantalla_inicio)
boton1.place(x=250, y=70, width=120, height=25)

boton2 = tk.Button(ventana, text="Agebra lineal", command=pantalla_algebra)
boton2.place(x=250, y=100, width=120, height=25)

boton3 = tk.Button(ventana, text="Matematica discreta", command=pantalla_matematica)
boton3.place(x=250, y=130, width=120, height=25)

bienvenida = tk.Label(home, text="Bienvenido, selecciona tu calculadora", font=("Times New Roman", 12),)
bienvenida.grid(row=0, column=2, padx=200, pady=20)

pantalla_inicio()

ventana.mainloop()