import tkinter as tk
from tkinter import messagebox
import math
# Función que coloca los widgets en el frame de matemática discreta
def operaciones_matematica_discreta(frame):
    camb = tk.StringVar(value="")
    camb_rep = tk.StringVar(value="Sin Repeticion")

    def permu(pri, seg, rep):
        if rep == "Con Repeticion":
            return pri ** seg
        return math.factorial(pri) // math.factorial(pri - seg)

    def comb(pri, seg, rep):
        if rep == "Con Repeticion":
            return math.factorial(pri + seg - 1) // (math.factorial(seg) * math.factorial(pri - 1))
        return math.factorial(pri) // (math.factorial(seg) * math.factorial(pri - seg))

    def calc():
        try:
            pri = int(entra_pri.get())
            seg = int(entra_seg.get())

            if pri < 0 or seg < 0:
                messagebox.showerror("", "Ingrese un Valor entero válido que no sea negativo")
                return

            if seg > pri and camb_rep.get() == "Sin Repeticion":
                messagebox.showerror("", "El segundo Valor no puede ser mayor al primero si se elige sin repetición")
                return

            if camb.get() == "Permutacion":
                resulta = permu(pri, seg, camb_rep.get())
                result.config(text=f"Permutaciones: {resulta}")
            elif camb.get() == "Combinacion":
                resulta = comb(pri, seg, camb_rep.get())
                result.config(text=f"Combinaciones: {resulta}")

        except ValueError:
            messagebox.showerror("", "El valor introducido no es válido. Introduce por favor un número.")
            return

    def mostrar_panta(camb2):
        camb.set(camb2)
        result.config(text="")

        prilab.grid(row=1, column=0, padx=10, pady=10)
        entra_pri.grid(row=1, column=1, padx=10, pady=10)
        seglab.grid(row=2, column=0, padx=10, pady=10)
        entra_seg.grid(row=2, column=1, padx=10, pady=10)
        rep.grid(row=3, column=0, padx=10, pady=10)
        norep.grid(row=3, column=1, padx=10, pady=10)
        conrep.grid(row=4, column=1, padx=10, pady=10)
        btncalc.grid(row=5, column=0, columnspan=2, pady=10)
        result.grid(row=6, column=0, columnspan=2, pady=10)

    prilab = tk.Label(frame, text="Ingrese El Primer Valor:", font=("Times New Roman", 10))
    seglab = tk.Label(frame, text="Ingrese El Segundo Valor:", font=("Times New Roman", 10))
    entra_pri = tk.Entry(frame, font=("Times New Roman", 10), width=20)
    entra_seg = tk.Entry(frame, font=("Times New Roman", 10), width=20)

    rep = tk.Label(frame, text="Tipo:", font=("Times New Roman", 10))
    norep = tk.Radiobutton(frame, text="Sin Repeticion", variable=camb_rep, value="Sin Repeticion", font=("Times New Roman", 10))
    conrep = tk.Radiobutton(frame, text="Con Repeticion", variable=camb_rep, value="Con Repeticion", font=("Times New Roman", 10))

    btncalc = tk.Button(frame, text="Calcular", command=calc, font=("Times New Roman", 10), width=12, height=3)
    result = tk.Label(frame, text="", font=("Times New Roman", 10))

    btnpermu = tk.Button(frame, text="Permutaciones", command=lambda: mostrar_panta("Permutacion"), font=("Times New Roman", 10), width=20, height=2)
    btncomb = tk.Button(frame, text="Combinaciones", command=lambda: mostrar_panta("Combinacion"), font=("Times New Roman", 10), width=20, height=2)

    btnpermu.grid(row=0, column=0, padx=10, pady=10)
    btncomb.grid(row=0, column=1, padx=10, pady=10)