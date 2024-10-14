import tkinter as tk
from tkinter import messagebox
import math
import Pantalla_principal as PP
rai = tk.Tk()
rai.title("Calculadora de Combinaciones y Repeticiones")
rai.geometry("500x500")

#cambia la pantalla
camb = tk.StringVar(value="")
camb_rep = tk.StringVar(value="Sin Repeticion") # cambia para cambiar las repeticiones 

def permu(pri, seg, rep):
    if rep == "Con Repeticion":
        return  (pri ** seg)
    return math.factorial(pri) // math.factorial(pri - seg)

def comb(pri, seg, rep):
    if rep == "Con Repeticion":
        return math.factorial(pri + seg - 1) // (math.factorial(seg) * math.factorial(pri - 1))
    return math.factorial(pri) // (math.factorial(seg)* math.factorial(pri - seg)) #Define las ecuaciones

def calc(): #Define la funcion de calcular
    try:
        pri = int(entra_pri.get())
        seg = int(entra_seg.get())
        
        if pri < 0 or seg < 0 :
            messagebox.showerror("","Ingrese un Valor entero valido que no sea negativo")
            return
        
        if seg > pri and camb_rep.get() == "Sin Repeticion":
            messagebox.showerror("", "El segundo Valor No puede Ser mayor al Primero Si se elige sin repeticion")
            return
        
        if camb.get() == "Permutacion":
            resulta = permu(pri, seg, camb_rep.get())
            result.config(text = f"Permutaciones: {resulta} " ) 
        
        elif camb.get() == "Combinacion":
            resulta = comb(pri, seg, camb_rep.get())
            result.config(text = f"Combinaciones: {resulta}" ) 
            
    except ValueError:
        messagebox.showerror("", "El valor introducido no es valido, Introduce Por favor un Numero")
        return

def mostrar_panta(camb2): # define el cambio de pantallas
    camb.set(camb2)
    result.config(text="")
    
    prilab.place(x=50, y=150)
    entra_pri.place(x=200, y=150, width=200)
    seglab.place(x=50, y=200)
    entra_seg.place(x=200, y=200, width=200)
    rep.place(x=50, y=250)
    conrep.place(x=275, y=250)
    norep.place(x=100, y=250)
    btncalc.place(x=50, y=350)
    result.place(x=50, y=400)
    
prilab = tk.Label(rai, text="Ingrese El Primer Valor: ", font=("Times New Roman", 10))
seglab = tk.Label(rai, text="Ingrese El segundo valor", font=("Times New Roman", 10))
entra_pri = tk.Entry(rai, font=("Times New Roman", 10), width=20)
entra_seg = tk.Entry(rai, font=("Times New Roman", 10), width=20)

rep = tk.Label(rai, text="Tipo:", font=("Times New Roman", 10))
norep = tk.Radiobutton(rai, text="Sin Repeticion", variable=camb_rep, value="Sin Repeticion", font=("Times New Roman", 10))
conrep = tk.Radiobutton(rai, text="Con Repeticion", variable=camb_rep, value="Con Repeticion", font=("Times New Roman", 10))

btncalc = tk.Button(rai, text="Calcular", command=calc, font=("Times New Roman", 10), width=12, height=3)

result = tk.Label(rai, text="", font=("Times New Roman", 10))

btnpermu = tk.Button(rai, text="Permutaciones", command=lambda: mostrar_panta ("Permutacion"), font=("Times New Roman", 10), width=20, height=2)
btncomb = tk.Button(rai, text="Combinaciones", command=lambda: mostrar_panta("Combinacion"), font=("Times New Roman", 10), width=20, height=2)

btnpermu.place(x=50, y=20)
btncomb.place (x=250, y=20)

PP.volver()

rai.mainloop()