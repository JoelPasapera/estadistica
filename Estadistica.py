import numpy as np
import statistics as stats
import tkinter as tk
import tkinter.messagebox as messagebox
from tkinter import ttk
import tkinter.simpledialog as simpledialog
from win10toast import ToastNotifier


# Diccionario de traducciones
t = {
    "Click me!": ("Click me!", "Haz clic aquí!"),
    "Enter text:": ("Enter text:", "Ingresa texto:"),
    "Submit": ("Submit", "Enviar"),
    "File": ("File", "Archivo"),
    "Open": ("Open", "Abrir"),
    "Save": ("Save", "Guardar"),
    "Exit": ("Exit", "Salir"),
    "Configuration": ("Configuration", "Configuración"),
    "Statistics": ("Statistics", "Estadísticas"),
    "Interpretation": ("Interpretation", "Interpretación"),
    "Language": ("Language", "Idioma"),
    "English": ("English", "Inglés"),
    "Spanish": ("Spanish", "Español"),
    "Spanish": ("Spanish", "Español"),
    "Measures or parameters of central tendency (MTC)": (
        "Measures or parameters of central tendency (MTC)",
        "Medidas o parámetros de tendencia central (MTC)",
    ),
    "mean": ("mean", "media"),
    "median": ("median", "mediana"),
    "mod": ("mod", "moda"),
    "others": ("others", "otros"),
    "elements": ("elements", "elementos"),
    "max": ("max", "máximo"),
    "min": ("min", "minimo"),
    "Measures or parameters of absolute dispersion": (
        "Measures or parameters of absolute dispersion",
        "Medidas o parámetros de dispersión absoluta",
    ),
    "standard deviation (std)": (
        "standard deviation (std)",
        "desviación estándar (desvt)",
    ),
    "variance (var)": ("variance (var)", "varianza (var)"),
    "range": ("range", "rango"),
    "Relative dispersion measures or parameters": (
        "Relative dispersion measures or parameters",
        "Medidas o parámetros de dispersión relativa",
    ),
    "Coefficient of variation (cv)": (
        "Coefficient of variation (cv)",
        "Coeficiente de variación (cv)",
    ),
    "Non-central tendency measures or parameters": (
        "Non-central tendency measures or parameters",
        "Medidas o parámetros de tendencia no central",
    ),
    "Quartils": ("Quartils", "cuartiles"),
    "Successful copy": ("Successful copy", "Copia exitosa"),
    "Results have been copied to the clipboard": (
        "Results have been copied to the clipboard",
        "Los resultados se han copiado en el portapapeles",
    ),
    "Enter data separated by commas": (
        "Enter data separated by commas",
        "Introduzca los datos separados por comas",
    ),
    "Enter the number of decimals in the results": (
        "Enter the number of decimals in the results",
        "Introduzca el número de decimales en los resultados",
    ),
    "Get results": ("Get results", "Obtener resultados"),
    "Enter the percentile number you wish to obtain": (
        "Enter the percentile number you wish to obtain",
        "Introduzca el número de percentil que desea obtener",
    ),
    "Enter data separated by commas": (
        "Enter data separated by commas",
        "Introduzca los datos separados por comas",
    ),
    "Copy results": ("Copy results", "Copiar resultados"),
    "Help": ("Help", "Ayuda"),
}

root1 = tk.Tk()
root1.geometry("200x50+600+300")
root1.title("Idioma")
label = tk.Label(root1, text="Selecciona el idioma")
label.pack()
combobox = ttk.Combobox(root1, values=["Español", "Inglés"])
combobox.pack()


def destroy():
    global seleccion
    seleccion = combobox.get()
    # Idioma seleccionado
    toaster = ToastNotifier()
    toaster.show_toast(
        "Idioma",
        f"Language: '{seleccion}'",
        duration=10,
        threaded=True,
        icon_path=None,
    )
    root1.destroy()


button = tk.Button(root1, text="ok", command=destroy, activebackground="#fdbce1")
button.place(x=175, y=18)

root1.mainloop()


if seleccion == "Español":
    o = 1
else:
    o = 0
print(o)
"=============================================================================================="


# los prints no son necesarios, solo imprime en terminal el nombre, pero deja las funciones porque al darle click al boton, esta funcion se activa y ejecuta algo
def abrir_archivo():
    print(t["Open"][o])


def guardar_archivo():
    print(t["Save"][o])


def opcion_1():
    print(t["Statistics"][o])


def opcion_2():
    print(t["Interpretation"][o])


def help():
    root1 = tk.Tk()
    root1.geometry("400x100+600+300")
    root1.title("Proceso")
    text = "Este es un texto de ejemplo que puede ser muy largo y necesitar ajustarse en la ventana."
    text_widget = tk.Text(root1, font=("Arial", 12))
    text_widget.pack(fill=tk.BOTH, expand=True)
    text_widget.insert(tk.END, text)

    # Ajustar el texto al tamaño de la ventana
    def ajustar_texto(event):
        text_widget.configure(width=event.width // 10, height=event.height // 20)

    text_widget.bind("<Configure>", ajustar_texto)


# Crear la ventana principal
root = tk.Tk()
root.geometry("800x600+250+50")
root.title(t["Statistics"][o])

# Crear la barra de menú
barra_menu = tk.Menu(root)

# Crear los menús y sus elementos
menu_archivo = tk.Menu(barra_menu, tearoff=0)
menu_archivo.add_command(label=t["Open"][o], command=abrir_archivo)
menu_archivo.add_command(label=t["Save"][o], command=guardar_archivo)
menu_archivo.add_separator()
menu_archivo.add_command(label=t["Exit"][o], command=root.quit)

menu_configuracion = tk.Menu(barra_menu, tearoff=0)
menu_configuracion.add_command(label=t["Statistics"][o], command=opcion_1)
menu_configuracion.add_command(label=t["Interpretation"][o], command=opcion_2)

menu_idioma = tk.Menu(barra_menu, tearoff=0)
menu_idioma.add_command(label=t["English"][o])
menu_idioma.add_command(label=t["Spanish"][o])

# Agregar los menús a la barra de menú
barra_menu.add_cascade(label=t["File"][o], menu=menu_archivo)
barra_menu.add_cascade(label=t["Configuration"][o], menu=menu_configuracion)
barra_menu.add_cascade(label=t["Language"][o], menu=menu_idioma)
barra_menu.add_cascade(label=t["Help"][o], command=help)
# Mostrar la barra de menú en la ventana principal
root.config(menu=barra_menu)

"""
#traduccion
a = label=t["Statistics"][o]
"""


def mct():
    global mean
    mean = np.round(np.mean(array), decimals)
    global median
    median = np.median(array)
    global mod
    mod = stats.mode(array)
    # traduccion
    a = label = t["Measures or parameters of central tendency (MTC)"][o]
    b = label = t["mean"][o]
    c = label = t["median"][o]
    d = label = t["mod"][o]
    mct_answer.config(text=f"{a}: \n {b} = {mean}, {c} = {median}, {d} = {mod}")


def other():
    elements = len(array)
    global max
    max = np.max(array)
    global min
    min = np.min(array)
    # traduccion
    a = label = t["others"][o]
    b = label = t["elements"][o]
    c = label = t["max"][o]
    d = label = t["min"][o]
    other_answer.config(text=f"{a}: \n {b} = {elements}, {c} = {max}, {d} = {min}")


def mad():
    global std
    std = np.round(np.std(array), decimals)
    global var
    var = np.round(np.var(array), decimals)
    # traduccion
    a = label = t["Measures or parameters of absolute dispersion"][o]
    b = label = t["standard deviation (std)"][o]
    c = label = t["variance (var)"][o]
    d = label = t["range"][o]
    mad_answer.config(text=f"{a}: \n {b} = {std}, {c} = {var} \n {d} = {max-min}")


def cv():
    global cv
    coefficient = np.round(std / median, decimals)
    percentage = f"{np.round(coefficient*100,decimals)} %"
    # traduccion
    a = label = t["Relative dispersion measures or parameters"][o]
    b = label = t["Coefficient of variation (cv)"][o]

    coefficient_answer.config(text=f"{a}: \n {b}: {coefficient} ({percentage})")
    # Pearson's coefficient of variation


def non_mtc():
    global non_mtc
    q1 = np.percentile(array, 25)
    q2 = np.percentile(array, 50)
    q3 = np.percentile(array, 75)


def percentile():
    # quartil is the same as certain kind of percentile, example quartil 1 is the same to percentil 25.
    q1 = np.percentile(array, 25)
    q2 = np.percentile(array, 50)
    q3 = np.percentile(array, 75)
    percentile_entry = int(get_percentile.get())
    pe = percentile_entry
    percentile_obtained = np.round(np.percentile(array, pe), decimals)
    # traduccion
    a = label = t["Non-central tendency measures or parameters"][o]
    b = label = t["Quartils"][o]
    percentile_answer.config(
        text=f"{a}: \n {b}: q1 = {q1}, q2 = {q2}, q3 = {q3} \n Percentil {percentile_entry}: ({percentile_obtained})"
    )


def copy_results():
    results = (
        mct_answer.cget("text")
        + "\n"
        + other_answer.cget("text")
        + "\n"
        + mad_answer.cget("text")
        + "\n"
        + coefficient_answer.cget("text")
        + "\n"
        + percentile_answer.cget("text")
    )
    root.clipboard_clear()
    root.clipboard_append(results)
    # traduccion
    a = label = t["Successful copy"][o]
    b = label = t["Results have been copied to the clipboard"][o]
    messagebox.showinfo(a, b)


# traduccion
axx = label = t["Enter data separated by commas"][o]
bxx = label = t["Enter the number of decimals in the results"][o]
cxx = label = t["Enter the percentile number you wish to obtain"][o]
dxx = label = t["Copy results"][o]
exx = label = t["Interpretation"][o]
fxx = label = t["Get results"][o]

lista = tk.Label(root, text=f"{axx}: ")
lista.pack()
entrada = tk.Text(root, height=4, width=50)
entrada.pack()
get_decimals = tk.Label(root, text=f"{bxx}: ")
get_decimals.pack()
get_decimal = tk.Spinbox(root, from_=0, to=100)
get_decimal.pack()

boton_obtener = tk.Button(
    root,
    text=f"{fxx}",
    command=lambda: [obtener_datos(), mct(), other(), mad(), cv(), percentile()],
    activebackground="#fdbce1",
)
boton_obtener.pack()

mct_answer = tk.Label(root, text="")
mct_answer.pack()
other_answer = tk.Label(root, text="")
other_answer.pack()
mad_answer = tk.Label(root, text="")
mad_answer.pack()
coefficient_answer = tk.Label(root, text="")
coefficient_answer.pack()
ask_percentile = tk.Label(root, text=f"{cxx}: ")
ask_percentile.pack()
get_percentile = ttk.Combobox(
    root,
    values=[
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
        16,
        17,
        18,
        19,
        20,
        21,
        22,
        23,
        24,
        25,
        26,
        27,
        28,
        29,
        30,
        31,
        32,
        33,
        34,
        35,
        36,
        37,
        38,
        39,
        40,
        41,
        42,
        43,
        44,
        45,
        46,
        47,
        48,
        49,
        50,
        51,
        52,
        53,
        54,
        55,
        56,
        57,
        58,
        59,
        60,
        61,
        62,
        63,
        64,
        65,
        66,
        67,
        68,
        69,
        70,
        71,
        72,
        73,
        74,
        75,
        76,
        77,
        78,
        79,
        80,
        81,
        82,
        83,
        84,
        85,
        86,
        87,
        88,
        89,
        90,
        91,
        92,
        93,
        94,
        95,
        96,
        97,
        98,
        99,
    ],
)
get_percentile.pack()
percentile_answer = tk.Label(root, text="")
percentile_answer.pack()
boton_copiar = tk.Button(
    root, text=f"{dxx}", command=copy_results, activebackground="#fdbce1"
)
boton_copiar.pack()


def obtener_datos():
    global decimals
    decimals = int(get_decimal.get())
    get = entrada.get("1.0", "end")
    separado = get.split(",")
    # acceder y modificar una variable global desde dentro de una función
    global array
    array = np.array(list(map(int, separado)))


interpretación = tk.Label(root, text=f"{exx}: ")
interpretación.pack()

# Iniciar el bucle principal de eventos
root.mainloop()
