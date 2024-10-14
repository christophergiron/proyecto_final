import tkinter as tk
from tkinter import messagebox
import math
import Pantalla_principal as PP
rai = tk.Tk()
rai.title("Calculadora de ")
rai.geometry("950x950")

#cambia la pantalla
camb = tk.StringVar(value="")
camb_rep = tk.StringVar(value="Sin Repeticion") # cambia para cambiar las repeticiones 

def permu(pri, seg, rep):
    if rep == "Con repeticion":
        return  math.pow(pri, seg)
    return math.factorial(pri) // math.factorial(pri - seg)

def comb(pri, seg, rep):
    if rep == "Con repeticion":
        return math.comb(pri - seg -1, seg)
    return math.factorial(pri) // (math.factorial(seg)* math.factorial(pri - seg))
def calc():
    try:
        pri = int(entra_pri.get())
        seg = int(entra_seg.get())
        
        if pri < 0 or seg < 0 :
            messagebox.showerror("Ingrese un Valor entero valido")
            return
        
        if seg > pri and camb_rep.get() == "sin repeticion":
            messagebox.showerror("El segundo Valor No puede Ser mayor al Primero Si se elige con repeticion")
            return
        
        if camb.get() == "Permutacion":
            result = permu(pri, seg, camb_rep.get())
            result.config(text = f"Permutaciones: {result} " ) 
        
        elif camb.get() == "Combinacion":
            result = comb(pri, seg, camb_rep.get())
            result.config(text = f"Combinaciones: {result}" ) 
    except ValueError:
        messagebox.showerror("El valor introducido no es valido, Introduce Por favor un Numero")
        return

def mostrar_panta(camb_repe):
    prilab.place(x=50, y=150)
    entra_pri.place(x=200, y=150, width=200)
    
prilab = tk.Label(rai, text="Ingrese El Primer Valor: ", font=("Times New Roman"))
seglab = tk.Label(rai, text="Ingrese El segundo valor", font=("Times New Roman", 10))
entra_pri = tk.Entry(rai, font=("Times New Roman", 10), width=20)
entra_seg = tk.Entry(rai, font=("Times New Roman", 10), width=20)

PP.volver()






rai.mainloop()