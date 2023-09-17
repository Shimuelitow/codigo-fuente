from tkinter import *
from tkinter import ttk
from time import *

pantalla_principal = Tk()
pantalla_principal.title("Sistema institucional de votacion estudiantil")
pantalla_principal.geometry("1280x600")
pantalla_principal.resizable(False, False)
pantalla_principal.config(bg="#F4E9CD")

# Create a style object to configure ttk widgets
style = ttk.Style()
style.configure('TButton', font=("Cascadia Code SemiBold", 20), background="#726E75", foreground="black", width=20, height=2,)

# Text principal
title = Label(pantalla_principal, text="SIVES", font=("Cascadia Code SemiBold", 50), bg="#F4E9CD")
title.place(x=150, y=50)

global identificador
global selected_party

global pantalla_datos_del_votante
#funciones

def only_numeric_input(P):
    # checks if entry's value is an integer or empty and returns an appropriate boolean
    if P.isdigit() or P == "":  # if a digit was entered or nothing was entered
        return True
    return False

def only_letters_input(P):
    # checks if entry's value is an integer or empty and returns an appropriate boolean
    if P.isalpha() or P == "":  # if a digit was entered or nothing was entered
        return True
    return False

def devolver_a_pantalla_principal():
    global identificador
    if identificador == 0:
        pantalla_datos_del_votante.withdraw()
        pantalla_principal.deiconify()
    
    elif identificador == 1:
        pantalla_creditos.withdraw()
        pantalla_principal.deiconify()
    
    elif identificador == 2:
        # You can add your code here for what to do when returning from the "Conteo de votos" screen.
        pantalla_conteo_de_votos.withdraw()
        pantalla_principal.deiconify()

    elif identificador == 3:
        # You can add your code here for what to do when returning from the "Conteo de votos" screen.
        pantalla_conteo_de_votos.withdraw()
        pantalla_principal.deiconify()

    elif identificador == 4:
        # You can add your code here for what to do when returning from the "Conteo de votos" screen.
        pantalla_zona_de_votacion.withdraw()
        pantalla_principal.deiconify()
    elif identificador == 5:
        # You can add your code here for what to do when returning from the "Conteo de votos" screen.
        pantalla_gracias_por_votar.withdraw()
        pantalla_principal.deiconify()

#create a function that saves the name and cedula of the voter in a file
def save_data():
    zona_de_votacion()
    name = entry_nombre_temporal.get()
    cedula = entry_cedula_temporal.get()
    with open("voters.txt", "a") as f:
        f.write(f"{name}, {cedula}\n")
    entry_nombre_temporal.set("")
    entry_cedula_temporal.set("")


#the function guardar voto is gonna get whatever checkbox the user selected and save it in a file, then show a new toplabel that says "gracias por votar" and then goes back to the main screen
def guardar_voto():
    global selected_party
    if selected_party.get() == 1:
        with open("votos.txt", "a") as f:
            f.write("Partido 1\n")
    elif selected_party.get() == 2:
        with open("votos.txt", "a") as f:
            f.write("Partido 2\n")
    elif selected_party.get() == 3:
        with open("votos.txt", "a") as f:
            f.write("Partido 3\n")
    elif selected_party.get() == 4:
        with open("votos.txt", "a") as f:
            f.write("Partido 4\n")
    elif selected_party.get() == 5:
        with open("votos.txt", "a") as f:
            f.write("Voto nulo\n")

    pantalla_zona_de_votacion.withdraw()
    global pantalla_gracias_por_votar
    global identificador
    identificador = 5
    pantalla_gracias_por_votar = Toplevel()
    pantalla_gracias_por_votar.title("Gracias por votar")
    pantalla_gracias_por_votar.geometry("500x720")
    pantalla_gracias_por_votar.resizable(False, False)
    pantalla_gracias_por_votar.config(bg="#F4E9CD")

    #labels
    label_gracias_por_votar = Label(pantalla_gracias_por_votar, text="Gracias por votar", font=("Cascadia Code SemiBold", 25), bg="#F4E9CD")
    label_gracias_por_votar.place(x=90, y=50)

    #buttons
    devolver = ttk.Button(pantalla_gracias_por_votar, text="Devolver", command=devolver_a_pantalla_principal)
    devolver.place(x=90, y=600)

    





def zona_de_votacion():
    global identificador
    global selected_party
    selected_party = IntVar()
    identificador = 4
    pantalla_datos_del_votante.withdraw()
    global pantalla_zona_de_votacion
    pantalla_zona_de_votacion = Toplevel()
    pantalla_zona_de_votacion.title("Zona de votacion")
    pantalla_zona_de_votacion.geometry("1280x720")
    pantalla_zona_de_votacion.resizable(False, False)
    pantalla_zona_de_votacion.config(bg="#F4E9CD")

    #labels
    zona_de_votacion_label = Label(pantalla_zona_de_votacion, text="Zona de votacion", font=("Cascadia Code SemiBold", 25), bg="#F4E9CD")
    zona_de_votacion_label.place(x=520, y=50)
    zona_de_votacion_partido_1 = Label(pantalla_zona_de_votacion, text="Partido 1", font=("Cascadia Code SemiBold", 20), bg="#F4E9CD")
    zona_de_votacion_partido_1.place(x=100, y=200)
    zona_de_votacion_partido_2 = Label(pantalla_zona_de_votacion, text="Partido 2", font=("Cascadia Code SemiBold", 20), bg="#F4E9CD")
    zona_de_votacion_partido_2.place(x=400, y=200)
    zona_de_votacion_partido_3 = Label(pantalla_zona_de_votacion, text="Partido 3", font=("Cascadia Code SemiBold", 20), bg="#F4E9CD")
    zona_de_votacion_partido_3.place(x=700, y=200)
    zona_de_votacion_partido_4 = Label(pantalla_zona_de_votacion, text="Partido 4", font=("Cascadia Code SemiBold", 20), bg="#F4E9CD")
    zona_de_votacion_partido_4.place(x=1000, y=200)
    zona_de_votacion_nulo = Label(pantalla_zona_de_votacion, text="Voto nulo", font=("Cascadia Code SemiBold", 20), bg="#F4E9CD")
    zona_de_votacion_nulo.place(x=100, y=400)

    #checkboxes
    def get_selected_party():
        
        if selected_party.get() == 1:
            print("Se seleccionó el partido 1")
        elif selected_party.get() == 2:
            print("Se seleccionó el partido 2")
        elif selected_party.get() == 3:
            print("Se seleccionó el partido 3")
        elif selected_party.get() == 4:
            print("Se seleccionó el partido 4")
        elif selected_party.get() == 5:
            print("Se seleccionó el voto nulo")
    style = ttk.Style()
    style.configure('TCheckbutton', font=("Cascadia Code SemiBold", 0), background="#F4E9CD", foreground="#F4E9CD", width=0, height=0,)
    selected_party = IntVar()
    checkbox_partido_1 = ttk.Checkbutton(pantalla_zona_de_votacion, variable=selected_party, onvalue=1, offvalue=0, command=get_selected_party,)
    checkbox_partido_1.place(x=135, y=250)
    checkbox_partido_2 = ttk.Checkbutton(pantalla_zona_de_votacion, variable=selected_party, onvalue=2, offvalue=0, command=get_selected_party)
    checkbox_partido_2.place(x=435, y=250)
    checkbox_partido_3 = ttk.Checkbutton(pantalla_zona_de_votacion, variable=selected_party, onvalue=3, offvalue=0, command=get_selected_party)
    checkbox_partido_3.place(x=735, y=250)
    checkbox_partido_4 = ttk.Checkbutton(pantalla_zona_de_votacion, variable=selected_party, onvalue=4, offvalue=0, command=get_selected_party)
    checkbox_partido_4.place(x=1035, y=250)
    checkbox_nulo = ttk.Checkbutton(pantalla_zona_de_votacion, variable=selected_party, onvalue=5, offvalue=0, command=get_selected_party)
    checkbox_nulo.place(x=135, y=450)

    #buttons
    devolver = ttk.Button(pantalla_zona_de_votacion, text="Devolver", command=devolver_a_pantalla_principal)
    devolver.place(x=90, y=600)
    enviar_voto = ttk.Button(pantalla_zona_de_votacion, text="Enviar voto", command=guardar_voto)
    enviar_voto.place(x=90, y=500)
    

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
    # variables
    global entry_nombre_temporal
    entry_nombre_temporal = StringVar()
    global entry_cedula_temporal
    entry_cedula_temporal = StringVar()
    # labels
    label_datos_del_votante = Label(pantalla_datos_del_votante, text="Datos del votante", font=("Cascadia Code SemiBold", 25), bg="#F4E9CD")
    label_datos_del_votante.place(x=90, y=50)

    label_nombre = Label(pantalla_datos_del_votante, text="Nombre:", font=("Cascadia Code SemiBold", 20), bg="#F4E9CD")
    label_nombre.place(x=90, y=200)
    label_cedula = Label(pantalla_datos_del_votante, text="Cedula:", font=("Cascadia Code SemiBold", 20), bg="#F4E9CD")
    label_cedula.place(x=90, y=300)

    # entrys
    entry_nombre = ttk.Entry(pantalla_datos_del_votante, font=("Cascadia Code SemiBold", 20), textvariable=entry_nombre_temporal)
    entry_nombre.place(x=90, y=250)

    global entry_cedula
    entry_cedula = ttk.Entry(pantalla_datos_del_votante, font=("Cascadia Code SemiBold", 20), textvariable=entry_cedula_temporal)
    entry_cedula.place(x=90, y=350)

    # Set the validation function for entry_cedula
    validation = pantalla_datos_del_votante.register(only_numeric_input)
    entry_cedula.config(validate="key", validatecommand=(validation, "%P"))

    #set the validation function for entry_nombre
    validation = pantalla_datos_del_votante.register(only_letters_input)
    entry_nombre.config(validate="key", validatecommand=(validation, "%P"))


    # buttons
    devolver = ttk.Button(pantalla_datos_del_votante, text="Devolver", command=devolver_a_pantalla_principal)
    devolver.place(x=90, y=600)
    enviar = ttk.Button(pantalla_datos_del_votante, text="Enviar", command=save_data,)
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
    label_extras = Label(pantalla_creditos, text="Extras", font=("Cascadia Code SemiBold", 25), bg="#F4E9CD")
    label_extras.place(x=90, y=350)
    label_extras_1 = Label(pantalla_creditos, text="Yuba Rojas", font=("Cascadia Code SemiBold", 20), bg="#F4E9CD", fg="#726E75")
    label_extras_1.place(x=90, y=400)
    label_extras_2 = Label(pantalla_creditos, text="Fabricio Mendez", font=("Cascadia Code SemiBold", 20), bg="#F4E9CD", fg="#726E75")
    label_extras_2.place(x=90, y=450)
    label_extras_3 = Label(pantalla_creditos, text="Dylan Ugalde", font=("Cascadia Code SemiBold", 20), bg="#F4E9CD", fg="#726E75")
    label_extras_3.place(x=90, y=500)

    #buttons
    devolver = ttk.Button(pantalla_creditos, text="Devolver", command=devolver_a_pantalla_principal)
    devolver.place(x=130, y=600)

#esta funcion va a contar los votos en el archivo votos.txt, y luego mostrarlo en la pantalla de conteo de votos
def contador_de_votos():
    for i in range(1, 5):
        with open("votos.txt", "r") as f:
            votos = f.read()
            votos_partido_1 = votos.count("Partido 1")
            votos_partido_2 = votos.count("Partido 2")
            votos_partido_3 = votos.count("Partido 3")
            votos_partido_4 = votos.count("Partido 4")
            votos_nulos = votos.count("Voto nulo")

    #labels
    label_conteo_de_votos = Label(pantalla_conteo_de_votos, text="Conteo de votos", font=("Cascadia Code SemiBold", 25), bg="#F4E9CD")
    label_conteo_de_votos.place(x=100, y=25)
    botos_partido_1 = Label(pantalla_conteo_de_votos, text=f"Partido 1: {votos_partido_1}", font=("Cascadia Code SemiBold", 20), bg="#F4E9CD")
    botos_partido_1.place(x=100, y=100)
    botos_partido_2 = Label(pantalla_conteo_de_votos, text=f"Partido 2: {votos_partido_2}", font=("Cascadia Code SemiBold", 20), bg="#F4E9CD")
    botos_partido_2.place(x=100, y=200)
    botos_partido_3 = Label(pantalla_conteo_de_votos, text=f"Partido 3: {votos_partido_3}", font=("Cascadia Code SemiBold", 20), bg="#F4E9CD")
    botos_partido_3.place(x=100, y=300)
    botos_partido_4 = Label(pantalla_conteo_de_votos, text=f"Partido 4: {votos_partido_4}", font=("Cascadia Code SemiBold", 20), bg="#F4E9CD")
    botos_partido_4.place(x=100, y=400)
    botos_nulos = Label(pantalla_conteo_de_votos, text=f"Votos nulos: {votos_nulos}", font=("Cascadia Code SemiBold", 20), bg="#F4E9CD")
    botos_nulos.place(x=100, y=500)



def validation():
    if entry_usuario_temporal.get() == "admin" and entry_contraseña_temporal.get() == "admin":
        global identificador
        global pantalla_conteo_de_votos
    
        pantalla_conteo_de_votos.withdraw()
        #congifuracion de la pantalla de conteo de votos
        pantalla_conteo_de_votos = Toplevel()
        pantalla_conteo_de_votos.title("Conteo de votos")
        pantalla_conteo_de_votos.geometry("500x700")
        pantalla_conteo_de_votos.resizable(False, False)
        pantalla_conteo_de_votos.config(bg="#F4E9CD")
        #labels
        label_conteo_de_votos = Label(pantalla_conteo_de_votos, text="Conteo de votos", font=("Cascadia Code SemiBold", 25), bg="#F4E9CD")
        label_conteo_de_votos.place(x=100, y=25)
        botos_partido_1 = Label(pantalla_conteo_de_votos, text="Partido 1:", font=("Cascadia Code SemiBold", 20), bg="#F4E9CD")
        botos_partido_1.place(x=100, y=100)
        botos_partido_2 = Label(pantalla_conteo_de_votos, text="Partido 2:", font=("Cascadia Code SemiBold", 20), bg="#F4E9CD")
        botos_partido_2.place(x=100, y=200)
        botos_partido_3 = Label(pantalla_conteo_de_votos, text="Partido 3:", font=("Cascadia Code SemiBold", 20), bg="#F4E9CD")
        botos_partido_3.place(x=100, y=300)
        botos_partido_4 = Label(pantalla_conteo_de_votos, text="Partido 4:", font=("Cascadia Code SemiBold", 20), bg="#F4E9CD")
        botos_partido_4.place(x=100, y=400)
        botos_nulos = Label(pantalla_conteo_de_votos, text="Votos nulos:", font=("Cascadia Code SemiBold", 20), bg="#F4E9CD")
        botos_nulos.place(x=100, y=500)




        #buttons
        devolver = ttk.Button(pantalla_conteo_de_votos, text="Devolver", command=devolver_a_pantalla_principal)
        devolver.place(x=90, y=580)
        contar_votos = ttk.Button(pantalla_conteo_de_votos, text="Contar votos", command=contador_de_votos)
        contar_votos.place(x=90, y=650)




        
        
def conteo_de_votos():
    global identificador
    identificador = 3
    pantalla_principal.withdraw()
    global pantalla_conteo_de_votos
    pantalla_conteo_de_votos = Toplevel()
    pantalla_conteo_de_votos.title("Conteo de votos")
    pantalla_conteo_de_votos.geometry("500x700")
    pantalla_conteo_de_votos.resizable(False, False)
    pantalla_conteo_de_votos.config(bg="#F4E9CD")

    #labels
    label_conteo_de_votos = Label(pantalla_conteo_de_votos, text="Conteo de votos", font=("Cascadia Code SemiBold", 25), bg="#F4E9CD")
    label_conteo_de_votos.place(x=90, y=50)
    label_usuario = Label(pantalla_conteo_de_votos, text="Usuario:", font=("Cascadia Code SemiBold", 20), bg="#F4E9CD")
    label_usuario.place(x=90, y=200)
    label_contraseña = Label(pantalla_conteo_de_votos, text="Contraseña:", font=("Cascadia Code SemiBold", 20), bg="#F4E9CD")
    label_contraseña.place(x=90, y=300)
    #variables
    global entry_usuario_temporal
    entry_usuario_temporal = StringVar()
    global entry_contraseña_temporal
    entry_contraseña_temporal = StringVar()
    #entrys
    entry_usuario = ttk.Entry(pantalla_conteo_de_votos, font=("Cascadia Code SemiBold", 20), textvariable=entry_usuario_temporal)
    entry_usuario.place(x=90, y=250)
    entry_contraseña = ttk.Entry(pantalla_conteo_de_votos, font=("Cascadia Code SemiBold", 20), textvariable=entry_contraseña_temporal)
    entry_contraseña.place(x=90, y=350)


    #buttons
    devolver = ttk.Button(pantalla_conteo_de_votos, text="Devolver", command=devolver_a_pantalla_principal)
    devolver.place(x=90, y=600)
    enviar = ttk.Button(pantalla_conteo_de_votos, text="Enviar", command=validation)
    enviar.place(x=90, y=500)

# Buttons
Area_de_votacion = ttk.Button(pantalla_principal, text="Area de votacion", command=datos_del_votante)
Area_de_votacion.place(x=90, y=200)

Conteo_de_votos = ttk.Button(pantalla_principal, text="Conteo de votos", command=conteo_de_votos)
Conteo_de_votos.place(x=90, y=300)

Creditos = ttk.Button(pantalla_principal, text="Creditos", command=creditos)
Creditos.place(x=90, y=400)

Salir = ttk.Button(pantalla_principal, text="Salir", command=pantalla_principal.destroy)
Salir.place(x=90, y=500)
pantalla_principal.mainloop()