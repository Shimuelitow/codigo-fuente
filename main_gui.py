from tkinter import *
from tkinter import font
from tkinter import ttk

pantalla_principal = Tk()
pantalla_principal.title("Sistema institucional de votacion estudiantil")
pantalla_principal.geometry("1280x720")
pantalla_principal.resizable(False, False)
pantalla_principal.config(bg="#F4E9CD")

# Create a style object to configure ttk widgets
style = ttk.Style()
style.configure('TButton', font=("Cascadia Code SemiBold", 20), background="#726E75", foreground="black", width=20, height=2,)

# Text principal
title = Label(pantalla_principal, text="SIVES", font=("Cascadia Code SemiBold", 50), bg="#F4E9CD")
title.place(x=150, y=50)

global identificador

#funciones
def devolver_a_pantalla_principal():
    if identificador == 0:
        pantalla_datos_del_votante.withdraw()
        pantalla_principal.deiconify()
    elif identificador == 1:
        pantalla_creditos.withdraw()
        pantalla_principal.deiconify()
    elif identificador == 2:
        pantalla_candidatos.withdraw()
        pantalla_principal.deiconify()
    elif identificador == 3:
        pantalla_conteo_de_votos.withdraw()
        pantalla_principal.deiconify()

def datos_del_votante():
    global identificador
    identificador = 0
    pantalla_principal.withdraw()
    global pantalla_datos_del_votante
    pantalla_datos_del_votante = Toplevel()
    pantalla_datos_del_votante.title("Datos del votante")
    pantalla_datos_del_votante.geometry("500x720")
    pantalla_datos_del_votante.resizable(False, False)
    pantalla_datos_del_votante.config(bg="#F4E9CD")

    #labels
    label_datos_del_votante = Label(pantalla_datos_del_votante, text="Datos del votante", font=("Cascadia Code SemiBold", 25), bg="#F4E9CD")
    label_datos_del_votante.place(x=120, y=50)

    label_nombre = Label(pantalla_datos_del_votante, text="Nombre:", font=("Cascadia Code SemiBold", 20), bg="#F4E9CD")
    label_nombre.place(x=90, y=200)

    label_cedula = Label(pantalla_datos_del_votante, text="Cedula:", font=("Cascadia Code SemiBold", 20), bg="#F4E9CD")
    label_cedula.place(x=90, y=300)

    #entrys
    entry_nombre = ttk.Entry(pantalla_datos_del_votante, font=("Cascadia Code SemiBold", 20))
    entry_nombre.place(x=90, y=250)

    entry_cedula = ttk.Entry(pantalla_datos_del_votante, font=("Cascadia Code SemiBold", 20))
    entry_cedula.place(x=90, y=350)


    
    #buttons
    devolver = ttk.Button(pantalla_datos_del_votante, text="Devolver", command=devolver_a_pantalla_principal)
    devolver.place(x=90, y=600)
    enviar = ttk.Button(pantalla_datos_del_votante, text="Enviar")
    enviar.place(x=90, y=500)


def creditos():
    global identificador
    identificador = 1
    pantalla_principal.withdraw()
    global pantalla_creditos
    pantalla_creditos = Toplevel()
    pantalla_creditos.title("Creditos")
    pantalla_creditos.geometry("600x720")
    pantalla_creditos.resizable(False, False)
    pantalla_creditos.config(bg="#F4E9CD")

    #labels
    programadores = Label(pantalla_creditos, text="Programadores", font=("Cascadia Code SemiBold", 25), bg="#F4E9CD")
    programadores.place(x=90, y=50)
    nombre_del_programador_1 = Label(pantalla_creditos, text="Gabriel Dario Chacon Madrigal", font=("Cascadia Code SemiBold", 20), bg="#F4E9CD", fg="#726E75")
    nombre_del_programador_1.place(x=90, y=100)
    trabajo_escrito_por_1 = Label(pantalla_creditos, text="Trabajo escrito", font=("Cascadia Code SemiBold", 25), bg="#F4E9CD")
    trabajo_escrito_por_1.place(x=90, y=200)
    nombre_del_programador_2 = Label(pantalla_creditos, text="Sommer Chaves Ugalde", font=("Cascadia Code SemiBold", 20), bg="#F4E9CD", fg="#726E75")
    nombre_del_programador_2.place(x=90, y=250)

    #buttons
    devolver = ttk.Button(pantalla_creditos, text="Devolver", command=devolver_a_pantalla_principal)
    devolver.place(x=130, y=600)
    

def candidatos():
    global identificador
    identificador = 2
    pantalla_principal.withdraw()
    global pantalla_candidatos
    pantalla_candidatos = Toplevel()
    pantalla_candidatos.title("Candidatos")
    pantalla_candidatos.geometry("1280x720")
    pantalla_candidatos.resizable(False, False)
    pantalla_candidatos.config(bg="#F4E9CD")
    
    #buttons
    devolver = ttk.Button(pantalla_candidatos, text="Devolver", command=devolver_a_pantalla_principal)
    devolver.place(x=90, y=600)

def conteo_de_votos():
    global identificador
    identificador = 3
    pantalla_principal.withdraw()
    global pantalla_conteo_de_votos
    pantalla_conteo_de_votos = Toplevel()
    pantalla_conteo_de_votos.title("Conteo de votos")
    pantalla_conteo_de_votos.geometry("1280x720")
    pantalla_conteo_de_votos.resizable(False, False)
    pantalla_conteo_de_votos.config(bg="#F4E9CD")

    #buttons
    devolver = ttk.Button(pantalla_conteo_de_votos, text="Devolver", command=devolver_a_pantalla_principal)
    devolver.place(x=90, y=600)

# Buttons
Area_de_votacion = ttk.Button(pantalla_principal, text="Area de votacion", command=datos_del_votante)
Area_de_votacion.place(x=90, y=200)

Conteo_de_votos = ttk.Button(pantalla_principal, text="Conteo de votos", command=conteo_de_votos)
Conteo_de_votos.place(x=90, y=300)

Candidatos = ttk.Button(pantalla_principal, text="Candidatos", command=candidatos)
Candidatos.place(x=90, y=400)

Creditos = ttk.Button(pantalla_principal, text="Creditos", command=creditos)
Creditos.place(x=90, y=500)

Salir = ttk.Button(pantalla_principal, text="Salir", command=pantalla_principal.destroy)
Salir.place(x=90, y=600)

pantalla_principal.mainloop()