import tkinter as tk
from tkinter import messagebox
import math
# Función que coloca los widgets en el frame de matemática discreta
def operaciones_matematica_discreta(frame, volver_inicio,):
    
    #Creacion de las pantallas
    panta_princi = tk.Frame(frame, bg="#00183e")
    panta_permu = tk.Frame(frame,bg="#00183e")
    panta_comb = tk.Frame(frame,bg="#00183e")

    def mostrar(panta): # definicion de que hace cada pantalla y empaquetamiento de cada una
        panta_princi.pack_forget()
        panta_permu.pack_forget()
        panta_comb.pack_forget()
        panta.pack()
        
        if panta == panta_princi:
            entra_pri.delete(0, tk.END) #Hace que la pantalla borre los datos introducidos anteriormente, osea los numeros
            entra_seg.delete(0, tk.END)
            entra_pric.delete(0, tk.END)
            entra_segc.delete(0, tk.END)
            result.config(text="")
            resultc.config(text="")


    #cambia la pantalla
    camb = tk.StringVar(value="Permutacion")
    camb_rep = tk.StringVar(value="Sin Repeticion") # cambia para cambiar las repeticiones 

    def permu(pri, seg, rep): #define la formula de la permutacion y si es con repeticion o no
        if rep == "Con Repeticion": #aqui se muestra como si esta seleccionado el con repeticion, se realiza la formula
            return  (pri ** seg)
        return math.factorial(pri) // math.factorial(pri - seg)

    def comb(pri, seg, rep): # lo mismo que lo anterior, pero con la combinacion
        if rep == "Con Repeticion":
            return math.factorial(pri + seg - 1) // (math.factorial(seg) * math.factorial(pri - 1))
        return math.factorial(pri) // (math.factorial(seg)* math.factorial(pri - seg)) #Define las ecuaciones

    def calc(): #Define la funcion de calcular
        try:
            if camb.get() == "Permutacion":
                pri = int(entra_pri.get().strip()) #revisa que los valores introducidos y en que pantalla se encuentran escritos y que se muestren y lean
                seg = int(entra_seg.get().strip())
            
            else: 
                pri = int(entra_pric.get().strip())
                seg = int(entra_segc.get().strip())
            
            
            if pri < 0 or seg < 0 : #muestra un mensaje de error si el numero es negativo                                                                                                                                                                                    🐟 Pez en el codigo 
                messagebox.showerror("","Ingrese un Valor entero valido que no sea negativo")
                return
            
            if seg > pri and camb_rep.get() == "Sin Repeticion": #si es una permutacion o combinacion con repeticion, funciona
                messagebox.showerror("", "El segundo Valor No puede Ser mayor al Primero Si se elige sin repeticion")
                return
            
            tiprep = "Con Repetición" if camb_rep.get() == "Con Repeticion" else "Sin Repetición" #define el tipo de repeticion seleccionado y que texto muestra al colocarse
            pqpermu = "porque n! / (n-m)!" if camb_rep.get() == "Sin Repeticion" else "porque n^m" #verifica la formula de la permutacion que se quiera mostrar
            pqcomb = "porque n! / [m!(n-m)!]" if camb_rep.get() == "Sin Repeticion" else "porque (n+m-1)! / [m!(n-1)!]" #verifica la formula de la combinacion que se quiera mostrar
            
            if camb.get() == "Permutacion": #muestra los resultados del tipo de operacion que se pedia, al igual que lee todos los datos introducidos y realiza la operacion pedida y escribe el resultado en la pantalla
                resulta = permu(pri, seg, camb_rep.get())
                result.config(text = f"Permutaciones {tiprep}: {pqpermu} es igual a: {resulta} " ) 
            
            elif camb.get() == "Combinacion":
                resulta = comb(pri, seg, camb_rep.get()) #Lo mismo que lo de arriba pero con combinacion
                resultc.config(text = f"Combinaciones {tiprep}: {pqcomb} es igual a: {resulta}" ) 
                
        except ValueError: #muestra error si no se introduce un numero y se introduce una letra o si no se introduce nada
            messagebox.showerror("", "El valor introducido no es valido, Introduce Por favor un Numero")
            return
    operacionselec = tk.Label(panta_princi, font=("Times New Roman", 10), text="Seleccione su Operación" ,fg="#ffc54a", bg="#00183e") #solo funciona para bajar un poco los botones
    operacionselec.grid(row=0, column=3, padx=302, pady=30)   
    
    #Botones para enselar las pantallas de permutacion y de combinacion, haciendo que se intercambien entre las 3, que son la principal y las otras 2
    btnpermu = tk.Button(panta_princi, activebackground="#0085fa",bg="#00bbfa", text="Permutacion", command=lambda:[mostrar(panta_permu), camb.set("Permutacion")], font=("Times New Roman", 10), width=30, height=3)
    btnpermu.grid(row=1, column=3, padx=302, pady=10)


    btncomb = tk.Button(panta_princi, activebackground="#0085fa",bg="#00bbfa", text="Combinacion", command=lambda: [mostrar(panta_comb), camb.set("Combinacion")], font=("Times New Roman", 10), width=30, height=3)
    btncomb.grid(row=2, column=3,padx=302, pady=10)
    
     # Botón para volver al menú principal del proyecto (regresar a la selección de calculadoras)
    btn_volver_menu = tk.Button(panta_princi, activebackground="#a93a48", bg="#c93a48",text="Volver al Inicio", command=volver_inicio, font=("Times New Roman", 10), width=30, height=3)
    btn_volver_menu.grid(row=3, column=3, padx=302, pady=15)
    
    btnnada = tk.Button(panta_princi, text="", bg="#00bbfa", command=volver_inicio)
    btnnada.grid(row=9, column=3, padx=310, pady=3000) #sirve para poder rellenar el color, este y sus variantes posteriores en el codigo hacen lo mismo

    #Pantalla de la permutacion, muestra y lee todos los valores 
    
    btnnaada = tk.Button(panta_permu, text="", bg="#00bbfa", command=volver_inicio)
    btnnaada.grid(row=9, column=3, padx=310, pady=3000)
    
    camb = tk.StringVar(value="Permutacion") #define el cambio de repeticion
    camb_rep = tk.StringVar(value="Sin Repeticion") 

    prilab = tk.Label(panta_permu, bg="#ffc54a", text="Ingrese El Primer Valor: ", font=("Times New Roman", 10)) #coloca el texto que pide introducir los numeros
    prilab.grid(row=2, column=1, padx=10, pady=10)

    seglab = tk.Label(panta_permu, bg="#ffc54a", text="Ingrese El segundo valor", font=("Times New Roman", 10))
    seglab.grid(row=3, column=1, padx=10, pady=10)

    entra_pri = tk.Entry(panta_permu, bg="#79d7fd", font=("Times New Roman", 10), width=30) #deja introducir el valor del primer valor
    entra_pri.grid(row=2, column=2, padx=10, pady=10)

    entra_seg = tk.Entry(panta_permu, bg="#79d7fd", font=("Times New Roman", 10), width=30) # lo mismo que arriba pero con el segundo valor
    entra_seg.grid(row=3, column=2, padx=10, pady=10)

    rep = tk.Label(panta_permu, bg="#ffc54a",text="Tipo:", font=("Times New Roman", 10)) #coloca un texto que dice tipo para saber que repeticion se esta usando
    rep.grid(row=4, column=1, padx=2, pady=10)

    norep = tk.Radiobutton(panta_permu, activebackground="#0085fa", bg="#00bbfa",text="Sin Repeticion", variable=camb_rep, value="Sin Repeticion", font=("Times New Roman", 10)) #es el boton que se muestra, solo que este al ser un radiobutton, es un boton de bolita
    norep.grid(row=4, column=2,  padx=0, pady=10)

    conrep = tk.Radiobutton(panta_permu, activebackground="#0085fa",bg="#00bbfa", text="Con Repeticion", variable=camb_rep, value="Con Repeticion", font=("Times New Roman", 10))  # lo mismo que arriba, pero muestra con repeticion en lugar de sin repeticion
    conrep.grid(row=4, column=2, columnspan=20, padx=0, pady=10)

    btncalc = tk.Button(panta_permu, activebackground="#0085fa",bg="#00bbfa", text="Calcular", command=calc, font=("Times New Roman", 10), width=50, height=2) # es el boton que llama a la funcion de calcular 
    btncalc.grid(row=6, column=1, columnspan=2, pady=10)

    result = tk.Label(panta_permu, bg="#ffc54a", text="", font=("Times New Roman", 10,)) #muestra los resultados de las operaciones
    result.grid(row=7, column=1, columnspan=2, pady=10)

    btnpatras_permu = tk.Button(panta_permu, activebackground="#a93a48",bg="#c93a48", text="Regresar", command=lambda: mostrar(panta_princi), font=("Times New Roman", 10), width=10, height=2) #es el boton que regresa a la pantalla de inicio de la calculadora, el nombre de la extension lo deja muy claro
    btnpatras_permu.grid(row=1, column=0, pady=10)

    #pantalla combinaciones
    #tiene todo lo de arriba, solo cambia el nombre de la etiqueta agregando una c al final, y ya

    btnnaada = tk.Button(panta_comb, text="", bg="#00bbfa", command=volver_inicio)
    btnnaada.grid(row=9, column=3, padx=310, pady=3000)
    
    prilabc = tk.Label(panta_comb, bg="#ffc54a", text="Ingrese El Primer Valor: ", font=("Times New Roman", 10))
    prilabc.grid(row=2, column=1, padx=10, pady=10)

    seglabc = tk.Label(panta_comb, bg="#ffc54a", text="Ingrese El segundo valor", font=("Times New Roman", 10))
    seglabc.grid(row=3, column=1, padx=10, pady=10)

    entra_pric = tk.Entry(panta_comb, bg="#79d7fd", font=("Times New Roman", 10), width=30)
    entra_pric.grid(row=2, column=2, padx=10, pady=10)

    entra_segc = tk.Entry(panta_comb, bg="#79d7fd", font=("Times New Roman", 10), width=30)
    entra_segc.grid(row=3, column=2, padx=10, pady=10)

    repc = tk.Label(panta_comb, bg="#ffc54a", text="Tipo:", font=("Times New Roman", 10))
    repc.grid(row=4, column=1, padx=10, pady=10)

    norepc = tk.Radiobutton(panta_comb, activebackground="#0085fa",bg="#00bbfa", text="Sin Repeticion", variable=camb_rep, value="Sin Repeticion", font=("Times New Roman", 10))
    norepc.grid(row=4, column=2, padx=0, pady=10)

    conrepc = tk.Radiobutton(panta_comb, activebackground="#0085fa", bg="#00bbfa", text="Con Repeticion", variable=camb_rep, value="Con Repeticion", font=("Times New Roman", 10))
    conrepc.grid(row=4, column=2, columnspan=20,padx=10, pady=10)

    btncalcc = tk.Button(panta_comb, activebackground="#0085fa",bg="#00bbfa", text="Calcular", command=calc, font=("Times New Roman", 10), width=50, height=2)
    btncalcc.grid(row=6, column=1, columnspan=2, pady=10)

    resultc = tk.Label(panta_comb, bg="#ffc54a", text="", font=("Times New Roman", 10))
    resultc.grid(row=7, column=1, columnspan=2, pady=10)

    btnpatras_com = tk.Button(panta_comb, activebackground="#a93a48", bg="#c93a48", text="Regresar", command=lambda: mostrar(panta_princi), font=("Times New Roman", 10), width=10, height=2)
    btnpatras_com.grid(row=1, column=0, pady=10)
    #pe🐟
    mostrar(panta_princi) #llama a la pantalla principal para seleccionar la operacion 