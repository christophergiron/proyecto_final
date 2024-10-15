import tkinter as tk
from tkinter import messagebox
import math
# Función que coloca los widgets en el frame de matemática discreta
def operaciones_matematica_discreta(frame, volver_inicio):
    
    #Creacion de las pantallas
    panta_princi = tk.Frame(frame)
    panta_permu = tk.Frame(frame)
    panta_comb = tk.Frame(frame)

    def mostrar(panta):
        panta_princi.pack_forget()
        panta_permu.pack_forget()
        panta_comb.pack_forget()
        panta.pack()
        
        if panta == panta_princi:
            entra_pri.delete(0, tk.END)
            entra_seg.delete(0, tk.END)
            entra_pric.delete(0, tk.END)
            entra_segc.delete(0, tk.END)
            result.config(text="")
            resultc.config(text="")


    #cambia la pantalla
    camb = tk.StringVar(value="Permutacion")
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
            if camb.get() == "Permutacion":
                pri = int(entra_pri.get().strip())
                seg = int(entra_seg.get().strip())
            
            else: 
                pri = int(entra_pric.get().strip())
                seg = int(entra_segc.get().strip())
            
            
            if pri < 0 or seg < 0 :
                messagebox.showerror("","Ingrese un Valor entero valido que no sea negativo")
                return
            
            if seg > pri and camb_rep.get() == "Sin Repeticion":
                messagebox.showerror("", "El segundo Valor No puede Ser mayor al Primero Si se elige sin repeticion")
                return
            
            tiprep = "Con Repetición" if camb_rep.get() == "Con Repeticion" else "Sin Repetición"
            pqpermu = "porque n! / (n-m)!" if camb_rep.get() == "Sin Repeticion" else "porque n^m"
            pqcomb = "porque n! / [m!(n-m)!]" if camb_rep.get() == "Sin Repeticion" else "porque (n+m-1)! / [m!(n-1)!]"
            
            if camb.get() == "Permutacion":
                resulta = permu(pri, seg, camb_rep.get())
                result.config(text = f"Permutaciones {tiprep}: {pqpermu} es igual a: {resulta} " ) 
            
            elif camb.get() == "Combinacion":
                resulta = comb(pri, seg, camb_rep.get())
                resultc.config(text = f"Combinaciones {tiprep}: {pqcomb} es igual a: {resulta}" ) 
                
        except ValueError:
            messagebox.showerror("", "El valor introducido no es valido, Introduce Por favor un Numero")
            return
        
        
    btnpermu = tk.Button(panta_princi, text="Permutacion", command=lambda:[mostrar(panta_permu), camb.set("Permutacion")], font=("Times New Roman", 10), width=30, height=3)
    btnpermu.grid(row=1, column=2, padx=200, pady=10)


    btncomb = tk.Button(panta_princi, text="Combinacion", command=lambda: [mostrar(panta_comb), camb.set("Combinacion")], font=("Times New Roman", 10), width=30, height=3)
    btncomb.grid(row=2, column=2,padx=200, pady=15)
    
     # Botón para volver al menú principal del proyecto (regresar a la selección de calculadoras)
    btn_volver_menu = tk.Button(panta_princi, text="Volver al Inicio", command=volver_inicio, font=("Times New Roman", 10), width=30, height=3)
    btn_volver_menu.grid(row=3, column=2, padx=200, pady=20)

    #Pantalla permu
    camb = tk.StringVar(value="Permutacion")
    camb_rep = tk.StringVar(value="Sin Repeticion") 

    prilab = tk.Label(panta_permu, text="Ingrese El Primer Valor: ", font=("Times New Roman", 10))
    prilab.grid(row=2, column=0, padx=10, pady=10)

    seglab = tk.Label(panta_permu, text="Ingrese El segundo valor", font=("Times New Roman", 10))
    seglab.grid(row=3, column=0, padx=10, pady=10)

    entra_pri = tk.Entry(panta_permu, font=("Times New Roman", 10), width=30)
    entra_pri.grid(row=2, column=1, padx=10, pady=10)

    entra_seg = tk.Entry(panta_permu, font=("Times New Roman", 10), width=30)
    entra_seg.grid(row=3, column=1, padx=10, pady=10)

    rep = tk.Label(panta_permu, text="Tipo:", font=("Times New Roman", 10))
    rep.grid(row=4, column=0, padx=10, pady=10)

    norep = tk.Radiobutton(panta_permu, text="Sin Repeticion", variable=camb_rep, value="Sin Repeticion", font=("Times New Roman", 10))
    norep.grid(row=4, column=1, padx=10, pady=10)

    conrep = tk.Radiobutton(panta_permu, text="Con Repeticion", variable=camb_rep, value="Con Repeticion", font=("Times New Roman", 10))
    conrep.grid(row=4, column=2, padx=10, pady=10)

    btncalc = tk.Button(panta_permu, text="Calcular", command=calc, font=("Times New Roman", 10), width=50, height=2)
    btncalc.grid(row=6, column=0, columnspan=2, pady=10)

    result = tk.Label(panta_permu, text="", font=("Times New Roman", 10))
    result.grid(row=7, column=1, columnspan=2, pady=10)

    btnpatras_permu = tk.Button(panta_permu, text="Regresar", command=lambda: mostrar(panta_princi), font=("Times New Roman", 10), width=10, height=2)
    btnpatras_permu.grid(row=1, column=0, pady=10)

    #pantalla de combinaciones


    prilabc = tk.Label(panta_comb, text="Ingrese El Primer Valor: ", font=("Times New Roman", 10))
    prilabc.grid(row=2, column=0, padx=10, pady=10)

    seglabc = tk.Label(panta_comb, text="Ingrese El segundo valor", font=("Times New Roman", 10))
    seglabc.grid(row=3, column=0, padx=10, pady=10)

    entra_pric = tk.Entry(panta_comb, font=("Times New Roman", 10), width=30)
    entra_pric.grid(row=2, column=1, padx=10, pady=10)

    entra_segc = tk.Entry(panta_comb, font=("Times New Roman", 10), width=30)
    entra_segc.grid(row=3, column=1, padx=10, pady=10)

    repc = tk.Label(panta_comb, text="Tipo:", font=("Times New Roman", 10))
    repc.grid(row=4, column=0, padx=5, pady=10)

    norepc = tk.Radiobutton(panta_comb, text="Sin Repeticion", variable=camb_rep, value="Sin Repeticion", font=("Times New Roman", 10))
    norepc.grid(row=4, column=1, padx=10, pady=10)

    conrepc = tk.Radiobutton(panta_comb, text="Con Repeticion", variable=camb_rep, value="Con Repeticion", font=("Times New Roman", 10))
    conrepc.grid(row=4, column=2, padx=10, pady=10)

    btncalcc = tk.Button(panta_comb, text="Calcular", command=calc, font=("Times New Roman", 10), width=50, height=2)
    btncalcc.grid(row=6, column=0, columnspan=2, pady=10)

    resultc = tk.Label(panta_comb, text="", font=("Times New Roman", 10))
    resultc.grid(row=7, column=1, columnspan=2, pady=10)

    btnpatras_com = tk.Button(panta_comb, text="Regresar", command=lambda: mostrar(panta_princi), font=("Times New Roman", 10), width=10, height=2)
    btnpatras_com.grid(row=1, column=0, pady=10)
    
    mostrar(panta_princi)