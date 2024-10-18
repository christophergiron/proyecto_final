# **Diccionario de Datos**
Variables
camb

Tipo: tk.StringVar
Descripción: Variable que controla si se está trabajando con Permutaciones o Combinaciones.
Valores posibles: "Permutacion", "Combinacion"
camb_rep

Tipo: tk.StringVar
Descripción: Variable que define si la operación se hace con o sin repetición.
Valores posibles: "Sin Repeticion", "Con Repeticion"
pri

Tipo: int
Descripción: Primer valor introducido por el usuario para realizar los cálculos (n).
seg

Tipo: int
Descripción: Segundo valor introducido por el usuario para realizar los cálculos (m).
resulta

Tipo: int
Descripción: Resultado de la operación (permutación o combinación).
tiprep

Tipo: str
Descripción: Cadena que indica si la operación es con o sin repetición.
pqpermu

Tipo: str
Descripción: Explicación de la fórmula utilizada para permutaciones.
pqcomb

Tipo: str
Descripción: Explicación de la fórmula utilizada para combinaciones.
Widgets
panta_princi

Tipo: tk.Frame
Descripción: Frame principal que contiene el menú inicial.
panta_permu

Tipo: tk.Frame
Descripción: Frame que muestra la interfaz de permutaciones.
panta_comb

Tipo: tk.Frame
Descripción: Frame que muestra la interfaz de combinaciones.
entra_pri

Tipo: tk.Entry
Descripción: Campo de entrada donde el usuario introduce el primer número (n) para permutaciones.
entra_seg

Tipo: tk.Entry
Descripción: Campo de entrada donde el usuario introduce el segundo número (m) para permutaciones.
entra_pric

Tipo: tk.Entry
Descripción: Campo de entrada donde el usuario introduce el primer número (n) para combinaciones.
entra_segc

Tipo: tk.Entry
Descripción: Campo de entrada donde el usuario introduce el segundo número (m) para combinaciones.
result

Tipo: tk.Label
Descripción: Etiqueta donde se muestra el resultado de la operación de permutaciones.
resultc

Tipo: tk.Label
Descripción: Etiqueta donde se muestra el resultado de la operación de combinaciones.
Funciones
permu

Tipo: Función
Descripción: Calcula las permutaciones.
Parámetros:
pri (int): número total de elementos (n).
seg (int): número de elementos a elegir (m).
rep (str): indica si la operación es con o sin repetición.
Retorno: int - resultado de la permutación.
comb

Tipo: Función
Descripción: Calcula las combinaciones.
Parámetros:
pri (int): número total de elementos (n).
seg (int): número de elementos a elegir (m).
rep (str): indica si la operación es con o sin repetición.
Retorno: int - resultado de la combinación.
calc

Tipo: Función
Descripción: Procesa los valores introducidos por el usuario y muestra el resultado en pantalla.
Parámetros: Ninguno
Retorno: Ninguno - actualiza los widgets result y resultc con el resultado correspondiente.
mostrar

Tipo: Función
Descripción: Cambia entre las diferentes pantallas (Permutación, Combinación, Principal).
Parámetros:
panta (tk.Frame): Frame que se va a mostrar.
Retorno: Ninguno - solo actualiza la interfaz gráfica.