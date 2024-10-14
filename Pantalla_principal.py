import tkinter as tk

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
    
ventana = tk.Tk()
ventana.title("proyecto final")
ventana.geometry("400x300")

home = tk.Frame(ventana)
algebra_lineal = tk.Frame(ventana)
matematica_discreta= tk.Frame(ventana)

boton1 = tk.Button(ventana,text=" Inicio",command=pantalla_inicio)
boton1.place(x=145,y=40, width=130, height=30)

boton2 = tk.Button(ventana, text=" Alebra lineal ", command=pantalla_algebra)
boton2.place(x=145, y=70, width=130, height=30)

boton3 =tk.Button(ventana,text="Matematica discreta", command=pantalla_matematica)
boton3.place(x=145, y=100, width=130, height=30)
#opciones de menus 
#opciones de la pagina 1
poyo= tk.Label(home, text="Bienvenido selecciona tu calculadora",font=("Times New Roman", 12))
poyo.grid(row=0,column=0,padx=108, pady=10)

titulo1=tk.Label(matematica_discreta, text="poyo")
titulo1.grid(row=2,column=1)

entrada1=tk.Entry(matematica_discreta)
entrada1.grid(row=3, column=1)

titulo2 =tk.Label(algebra_lineal, text="poy")
titulo2.grid(row=2,column=1)

entrada2=tk.Entry(algebra_lineal)
entrada2.grid(row=3, column=1)

pantalla_inicio()

ventana.mainloop()