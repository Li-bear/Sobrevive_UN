from tkinter import *
from tkinter import messagebox
import random
import turtle


def continuar(dicc_tortugas,dicc_imagenes,dicc_ambitos,dicc_estadisticas,situaciones,dicc_textos):
    """
    Invoca a una situacion dependiendo de la semana en la cual se encuentre el usuario, o, si
    el usuario se encuentra actualmente en situaciones extensas.
    Aumenta en uno el valor de la llave "semana" del diccionario "dicc_ambitos".
    Comprueba si el usuario no ha perdido en la situacion que recien acaba de transcurrir del juego,
    de haber perdido, inovca a la funcion "game_over_total".

    parametros:
        dicc_tortugas: diccionario que contiene las variables del modulo turtle
        dicc_imagenes: diccionario que contiene las coordenadas y nombres de las imagenes de la
        situacion actual
        dicc_ambitos: diccionario que contiene las variables de cada ambito del usuario
        dicc_estadisticas: diccionario que contiene las variables del modulo tkinter las
        cuales se proyectan en pantalla
        situaciones: diccionario que contiene todas las posibles situaciones del juego
        dicc_textos: diccionario que contiene los mensajes que se proyectan en pantalla
    """
    global situacion_a_usar, situacion_extensa, resultado
    resultado = False
    
    if situacion_a_usar < 3:
        situacion_a_usar += 1
        situaciones[situacion_a_usar](dicc_tortugas,dicc_imagenes,dicc_ambitos,dicc_estadisticas,situaciones,dicc_textos)
    elif dicc_ambitos["Social_0"] < 1 or dicc_ambitos["Social_0"] > 99 or dicc_ambitos["Academico_0"] < 1 or dicc_ambitos["Academico_0"] > 99 \
         or dicc_ambitos["Salud_0"] < 1 or dicc_ambitos["Salud_0"] > 99 or dicc_ambitos["Economico_0"] < 1 or dicc_ambitos["Economico_0"] > 99 or dicc_ambitos["semana_0"] >= 16:
        game_over_total(dicc_imagenes,dicc_ambitos,dicc_estadisticas,dicc_textos)
    elif situacion_extensa > 49:
        resultado = False
        situaciones[situacion_extensa](dicc_tortugas,dicc_imagenes,dicc_ambitos,dicc_estadisticas,situaciones,dicc_textos)
    elif dicc_ambitos["semana_0"] == 5 or dicc_ambitos["semana_0"] == 8 or dicc_ambitos["semana_0"] == 12:
        situacion_a_usar = random.randint(10, 12)
        dicc_ambitos["semana_0"] += 1
        dicc_estadisticas["semana"].set(dicc_ambitos["semana_0"])
        resultado = False
        situaciones[situacion_a_usar](dicc_tortugas,dicc_imagenes,dicc_ambitos,dicc_estadisticas,situaciones,dicc_textos)
    elif dicc_ambitos["semana_0"] == 6:
        situacion_a_usar = 13
        dicc_ambitos["semana_0"] += 1
        dicc_estadisticas["semana"].set(dicc_ambitos["semana_0"])
        resultado = False
        situaciones[situacion_a_usar](dicc_tortugas,dicc_imagenes,dicc_ambitos,dicc_estadisticas,situaciones,dicc_textos)
    else:
        situacion_a_usar = random.randint(3, 9)
        dicc_ambitos["semana_0"] += 1
        dicc_estadisticas["semana"].set(dicc_ambitos["semana_0"])
        resultado = False
        situaciones[situacion_a_usar](dicc_tortugas,dicc_imagenes,dicc_ambitos,dicc_estadisticas,situaciones,dicc_textos)


def eleccion_1(dicc_tortugas,dicc_imagenes,dicc_ambitos,dicc_estadisticas,situaciones,dicc_textos):
    """
    Altera las estadisticas del usuario conforme a la decision numero uno

    Inicializa el Frame space_situacion para eliminar los textos, imagenes y botones de la
    situacion anterior.
    Asigna nuevos valores a las estadisticas del usuario si es que la eleccion que tomo
    generaba cambios en ellas, de ser asi, las tortugas del programa se desplazaran para
    ilustrar los nuevos valores de las estadisticas.
    Si el usuario no se encuentra en el tutorial, la funcion v_situaciones_1 es invocada.

    parametros:
        dicc_tortugas: diccionario que contiene las variables del modulo turtle
        dicc_imagenes: diccionario que contiene las coordenadas y nombres de las imagenes de la
        situacion actual
        dicc_ambitos: diccionario que contiene las variables de cada ambito del usuario
        dicc_estadisticas: diccionario que contiene las variables del modulo tkinter las
        cuales se proyectan en pantalla
        situaciones: diccionario que contiene todas las posibles situaciones del juego
        dicc_textos: diccionario que contiene los mensajes que se proyectan en pantalla
    """
    global situacion_a_usar, situacion_extensa, situacion_extensa_1, resultado, screen_situaciones

    space_situacion = Frame(screen_situaciones, width=480, height=300)
    space_situacion.place(x = 80 , y = 60)
    space_situacion.config(bg="black")
    
    dicc_imagenes["imagen"] = dicc_imagenes["imagen_1"]
    dicc_imagenes["coordenadas_imagen"] = dicc_imagenes["coordenadas_imagen_1"]

    situacion_extensa = situacion_extensa_1

    dicc_estadisticas["Academico"].set(dicc_ambitos["Academico_1"])
    dicc_ambitos["Academico_0"] = dicc_ambitos["Academico_1"]
    dicc_estadisticas["Salud"].set(dicc_ambitos["Salud_1"])
    dicc_ambitos["Salud_0"] = dicc_ambitos["Salud_1"]
    dicc_estadisticas["Economico"].set(dicc_ambitos["Economico_1"])
    dicc_ambitos["Economico_0"] = dicc_ambitos["Economico_1"]
    dicc_estadisticas["Social"].set(dicc_ambitos["Social_1"])
    dicc_ambitos["Social_0"] = dicc_ambitos["Social_1"]

    #codigo de tortuga

    if situacion_a_usar >=3:
        if dicc_tortugas["tortuga_academico1"] > 0:
            avanzar(dicc_tortugas["AcademicoT"],dicc_tortugas["tortuga_academico1"],dicc_tortugas["color_Academico"])
        elif dicc_tortugas["tortuga_academico1"] < 0:
            retroceder(dicc_tortugas["AcademicoT"],abs(dicc_tortugas["tortuga_academico1"]))

        if dicc_tortugas["tortuga_economico1"] > 0:
            avanzar(dicc_tortugas["EconomicoT"],dicc_tortugas["tortuga_economico1"],dicc_tortugas["color_Economico"])
        elif dicc_tortugas["tortuga_economico1"] < 0:
            retroceder(dicc_tortugas["EconomicoT"],abs(dicc_tortugas["tortuga_economico1"]))

        if dicc_tortugas["tortuga_salud1"] > 0:
            avanzar(dicc_tortugas["SaludT"],dicc_tortugas["tortuga_salud1"],dicc_tortugas["color_Salud"])
        elif dicc_tortugas["tortuga_salud1"] < 0:
            retroceder(dicc_tortugas["SaludT"],abs(dicc_tortugas["tortuga_salud1"]))

        if dicc_tortugas["tortuga_social1"] > 0:
            avanzar(dicc_tortugas["SocialT"],dicc_tortugas["tortuga_social1"],dicc_tortugas["color_Social"])
        elif dicc_tortugas["tortuga_social1"] < 0:
            retroceder(dicc_tortugas["SocialT"],abs(dicc_tortugas["tortuga_social1"]))

    #codigo de tortuga
    if situacion_a_usar < 3:
        continuar(dicc_tortugas,dicc_imagenes,dicc_ambitos,dicc_estadisticas,situaciones,dicc_textos)
    else:
        dicc_textos["txt_situacion"].set(dicc_textos["txt_1"])
        resultado = True
        v_situaciones_1(dicc_tortugas,dicc_imagenes,dicc_ambitos,dicc_estadisticas,situaciones,dicc_textos)
#

def eleccion_2(dicc_tortugas, dicc_imagenes,dicc_ambitos,dicc_estadisticas,situaciones,dicc_textos):
    """
    Altera las estadisticas del usuario conforme a la decision numero dos

    Inicializa el Frame space_situacion para eliminar los textos, imagenes y botones de la
    situacion anterior.
    Asigna nuevos valores a las estadisticas del usuario si es que la eleccion que tomo
    generaba cambios en ellas, de ser asi, las tortugas del programa se desplazaran para
    ilustrar los nuevos valores de las estadisticas.
    Si el usuario no se encuentra en el tutorial, la funcion v_situaciones_1 es invocada.

    parametros:
        dicc_tortugas: diccionario que contiene las variables del modulo turtle
        dicc_imagenes: diccionario que contiene las coordenadas y nombres de las imagenes de la
        situacion actual
        dicc_ambitos: diccionario que contiene las variables de cada ambito del usuario
        dicc_estadisticas: diccionario que contiene las variables del modulo tkinter las
        cuales se proyectan en pantalla
        situaciones: diccionario que contiene todas las posibles situaciones del juego
        dicc_textos: diccionario que contiene los mensajes que se proyectan en pantalla
    """
    global situacion_a_usar, situacion_extensa, situacion_extensa_2, resultado, screen_situaciones

    space_situacion = Frame(screen_situaciones, width=480, height=300)
    space_situacion.place(x = 80 , y = 60)
    space_situacion.config(bg="black")
    
    dicc_imagenes["imagen"] = dicc_imagenes["imagen_2"]
    dicc_imagenes["coordenadas_imagen"] = dicc_imagenes["coordenadas_imagen_2"]
    situacion_extensa = situacion_extensa_2

    dicc_estadisticas["Academico"].set(dicc_ambitos["Academico_2"])
    dicc_ambitos["Academico_0"] = dicc_ambitos["Academico_2"]
    dicc_estadisticas["Salud"].set(dicc_ambitos["Salud_2"])
    dicc_ambitos["Salud_0"] = dicc_ambitos["Salud_2"]
    dicc_estadisticas["Economico"].set(dicc_ambitos["Economico_2"])
    dicc_ambitos["Economico_0"] = dicc_ambitos["Economico_2"]
    dicc_estadisticas["Social"].set(dicc_ambitos["Social_2"])
    dicc_ambitos["Social_0"] = dicc_ambitos["Social_2"]

    #codigo de tortuga

    if situacion_a_usar >=3:
        if dicc_tortugas["tortuga_academico2"] > 0:
            avanzar(dicc_tortugas["AcademicoT"],dicc_tortugas["tortuga_academico2"],dicc_tortugas["color_Academico"])
        elif dicc_tortugas["tortuga_academico2"] < 0:
            retroceder(dicc_tortugas["AcademicoT"],abs(dicc_tortugas["tortuga_academico2"]))

        if dicc_tortugas["tortuga_economico2"] > 0:
            avanzar(dicc_tortugas["EconomicoT"],dicc_tortugas["tortuga_economico2"],dicc_tortugas["color_Economico"])
        elif dicc_tortugas["tortuga_economico2"] < 0:
            retroceder(dicc_tortugas["EconomicoT"],abs(dicc_tortugas["tortuga_economico2"]))

        if dicc_tortugas["tortuga_salud2"] > 0:
            avanzar(dicc_tortugas["SaludT,dicc_tortugas"],dicc_tortugas["tortuga_salud2"],dicc_tortugas["color_Salud"])
        elif dicc_tortugas["tortuga_salud2"] < 0:
            retroceder(dicc_tortugas["SaludT"],abs(dicc_tortugas["tortuga_salud2"]))

        if dicc_tortugas["tortuga_social2"] > 0:
            avanzar(dicc_tortugas["SocialT"],dicc_tortugas["tortuga_social2"],dicc_tortugas["color_Social"])
        elif dicc_tortugas["tortuga_social2"] < 0:
            retroceder(dicc_tortugas["SocialT"],abs(dicc_tortugas["tortuga_social2"]))
        
    #codigo de tortuga
    if situacion_a_usar < 3:
        continuar(dicc_tortugas,dicc_imagenes,dicc_ambitos,dicc_estadisticas,situaciones,dicc_textos)
    else:
        dicc_textos["txt_situacion"].set(dicc_textos["txt_2"])
        resultado = True
        v_situaciones_1(dicc_tortugas,dicc_imagenes,dicc_ambitos,dicc_estadisticas,situaciones,dicc_textos)


def tutorial(trampa):
    """
    Despliega mensajes para que el usuario ingrese los datos solicitiados, tales como "name",
    "Facultad" y "Carrera", si el usuario intenta seguir con el programa sin haber ingresado
    dichos datos, nuevos mensajes apareceran para que este sepa que no podra continuar hasta
    que los diligencie.

    parametro:
        trampa: variable booleana que permite conocer si el usuario ha intentado iniciar el
        juego sin haber ingresado los datos solicitados previamente
    """
    global screen_tutorial, name, Facultad, Carrera
    if not trampa:
        screen_inicio.withdraw()
        screen_tutorial = Toplevel()
        screen_tutorial.geometry("600x450+100+100")
        screen_tutorial.config(bg="black")
    else:
        screen_tutorial.withdraw()
        screen_tutorial = Toplevel()
        screen_tutorial.geometry("600x400+100+100")
        screen_tutorial.config(bg="black")

    global informacion
    informacion = Frame(screen_tutorial, width=500, height=150)
    informacion.pack(padx=5)
    informacion.config(bg="black")

    if not trampa:
        discurso = "\nEstás en en registro y control\n¡Es tu turno para conseguir el carne!\nLlena los siguientes datos"
    else:
        discurso = "\nVaya, parece que no has llenado\ntodos tus datos, o quizas estas mintiendo\nen algunos..."
    Label(informacion, text="\nBienvenido a la Unal", fg="gold", bg="black", font=("Courier New", 18)).pack()
    Label(informacion, text=discurso, fg="gold", bg="black", font=("Courier New", 10)).pack()

    global datos_espacio
    datos_espacio = Frame(screen_tutorial)
    datos_espacio.pack(pady=15)
    datos_espacio.config(bg="black")
    
    name = StringVar(screen_tutorial)
    Label(datos_espacio, text="Correo sin el @unal.edu.co ", font=("Courier New", 12), bg="black", fg="gold").grid(row=0, column=0)
    Entry(datos_espacio, justify=CENTER, textvariable=name).grid(row=0, column=1)

    Facultad = StringVar()
    Label(datos_espacio, text="Facultad ", font=("Courier New", 12), bg="black", fg="gold").grid(row=1, column=0)
    Entry(datos_espacio, justify=CENTER, textvariable=Facultad).grid(row=1, column=1)

    Carrera = StringVar()
    Label(datos_espacio, text="Carrera ", font=("Courier New", 12), bg="black", fg="gold").grid(row=2, column=0)
    Entry(datos_espacio, justify=CENTER, textvariable=Carrera).grid(row=2, column=1)

def verificar_perfiles(nombre_in, num_in, perfiles, lista_archivos, screen_puntajes):
    """
    Comprueba si ya hay algun registro de usuario en los archivos del juego, de ser así,
    comprueba si la contrasenia ingresada por el usuario corresponde a la que esta
    guardada en los archivos del programa, de ser asi, muestra en pantalla los puntajes
    obtenidos por el usuario en partidas anteriores.

    parametros:
        nombre_in: variable de tipo cadena del modulo tkinter, su valor es el nombre ingresado
        por el usuario en los tutoriales
        num_in: variable de tipo entero del modulo tkinter, su valor es la contraseña ingresada
        por el usuario en los tutoriales
        perfiles: variable que contiene la cantidad de registros existentes del juego
        lista_archivos: lista que contiene todos los registros existentes del juego
        screen_puntajes: pantalla del modulo tkinter 
    """
    if perfiles == 0:
        datos = "No hay registros de juego"
        Label(screen_puntajes, text=datos, font=("Courier New", 10), fg="gold", bg="black").pack(pady=15)
    else:
        encontrado = False
        try:
            usuario = nombre_in.get()
            num_entrada = num_in.get()
            cont = 0
            for i in range(len(lista_archivos)):
                if usuario == lista_archivos[i][0]:
                    encontrado = True
                    cont += 1
                    if int(lista_archivos[i][1]) == num_entrada:
                        datos = [int(i) for i in lista_archivos[i][2:]]
                        puntaje = sum(datos[:4])*(datos[4])
                        discurso = "Su mayor puntaje es: {}\nAcademico: {} Salud: {} Social: {} Economico: {} Semanas: {}".format(puntaje,datos[0],datos[1],datos[2],datos[3],datos[4])
                        Label(screen_puntajes, text=discurso, font=("Courier New", 10), fg="gold", bg="black").pack(pady=5)
                    else:
                        if cont > 1:
                            pass
                        else:
                            Label(screen_puntajes, text="Contraseña incorrecta", font=("Courier New", 10), fg="gold", bg="black").pack(pady=5)
            if encontrado == False:
                Label(screen_puntajes, text="Usuario no encontrado", font=("Courier New", 10), fg="gold", bg="black").pack(pady=5)
        except:
            Label(screen_puntajes, text="SOLO VALORES NUMERICOS EN CONTRASEÑA", font=("Courier New", 10), fg="gold", bg="black").pack(pady=5)

def tutorial_est(dicc_imagenes,dicc_estadisticas,situaciones,trampa):
    """
    Invoca a la funcion "tutorial()", inicializa las estadisticas del usuario,
    cada ambito con el valor entero de 50 guardando cada variable como un valor
    del diccionario "dicc_estadisticas"
    Inicializa el diccionario "dicc_tortugas" para que estas posteriormente grafiquen
    el valor de cada ambito por medio de una barra.
    Para poder continuar con el juego, el usuario debe accionar el boton "continuar",
    el cual invoca a la funcion "confimar_estandar()".
    
    parametros:
        dicc_imagenes: diccionario que contiene las coordenadas y nombres de las imagenes de la
        situacion actual.
        dicc_estadisticas: diccionario que contiene las variables del modulo tkinter las
        cuales se proyectan en pantalla.
        situaciones: diccionario que contiene todas las posibles situaciones del juego.
        trampa: variable booleana que permite conocer si el usuario ha intentado iniciar el
        juego sin haber ingresado los datos solicitados previamente.
    """
    tutorial(trampa)
    dicc_ambitos = {}
    dicc_ambitos["semana_0"] = 0
    dicc_estadisticas["semana"].set(dicc_ambitos["semana_0"])
    dicc_ambitos["Academico_0"] = 50
    dicc_estadisticas["Academico"].set(dicc_ambitos["Academico_0"])
    dicc_ambitos["Salud_0"] = 50
    dicc_estadisticas["Salud"].set(dicc_ambitos["Salud_0"])
    dicc_ambitos["Social_0"] = 50
    dicc_estadisticas["Social"].set(dicc_ambitos["Social_0"])
    dicc_ambitos["Economico_0"] = 50
    dicc_estadisticas["Economico"].set(dicc_ambitos["Economico_0"])


    dicc_tortugas = {}
    #codigo de turtle
    dicc_tortugas["academico_inicial"] = dicc_ambitos["Academico_0"] // 5
    dicc_tortugas["salud_inicial"] = dicc_ambitos["Academico_0"]  // 5
    dicc_tortugas["social_inicial"] = dicc_ambitos["Academico_0"] // 5
    dicc_tortugas["economico_inicial"] = dicc_ambitos["Academico_0"] // 5
    #codigo de turtle

    confirmar = Button(datos_espacio, text="Ok", font=("Courier New", 10), fg="gold", bg="gray22",
                       command= lambda :  confimar_estandar(dicc_imagenes,dicc_estadisticas,situaciones,dicc_tortugas,dicc_ambitos))
    confirmar.grid(column=1, padx=10)

def perfiles_inicio():
    """
    Crea una ventana emergente del modulo tkinter cada vez que se registra
    un usuario nuevo, y le dice la contraseña correspondiente a su perfil
    """
    perfiles, lineas_archivo = leer_puntajes()
    contrase = password()
    if perfiles == 0:
        messagebox.showinfo(message="Bienvenid@ " + name.get()+"\nsu contraseña es "+str(contrase), title="Registro usuario")
    else:
        encontrado = False
        for i in range(len(lineas_archivo)):
            if name.get() == lineas_archivo[i][0]:
                encontrado = True
                if lineas_archivo[i][1] == contrase:
                    messagebox.showinfo(message="Bienvenid@"+name.get(), title="Registro usuario")
        if encontrado == False:
            messagebox.showinfo(message="Bienvenid@ "+name.get()+"\nsu contraseña es "+str(contrase), title="Registro usuario")

def tutorial_per(dicc_imagenes,dicc_estadisticas,situaciones,trampa):
    """
    Invoca a la funcion "tutorial()", inicializa las estadisticas del usuario,
    cada ambito con el valor entero de 50 guardando cada variable como un valor
    del diccionario "dicc_estadisticas"
    Inicializa el diccionario "dicc_tortugas" para que estas posteriormente grafiquen
    el valor de cada ambito por medio de una barra.
    Para poder continuar con el juego, el usuario debe accionar el boton "continuar",
    el cual invoca a la funcion "confimar_estandar()".
    
    parametros:
        dicc_imagenes: diccionario que contiene las coordenadas y nombres de las imagenes de la
        situacion actual.
        dicc_estadisticas: diccionario que contiene las variables del modulo tkinter las
        cuales se proyectan en pantalla.
        situaciones: diccionario que contiene todas las posibles situaciones del juego.
        trampa: variable booleana que permite conocer si el usuario ha intentado iniciar el
        juego sin haber ingresado los datos solicitados previamente.
    """
    tutorial(trampa)
    dicc_ambitos = {}
    dicc_ambitos["semana_0"] = 0
    space_est_per = Frame(screen_tutorial)
    space_est_per.pack(pady=15)
    space_est_per.config(bg="gold")

    if not trampa:
        Label(informacion,
              text="Despues establece tus estadisticas, tienes 200\npuntos para distribuir en esos 4 aspectos.\nLos valores tienen que estar entre 1 y 99."
              , fg="gold", bg="black", font=("Courier New", 10)).pack()
    else:
        Label(informacion,
              text="¡Valores invalidos!, revisa bien...\nRecuerda que tus puntos deben sumar 200\nLos valores tienen que estar entre 1 y 99."
              , fg="gold", bg="black", font=("Courier New", 10)).pack()

    Label(space_est_per, text="Academico ", font=("Courier New", 12), bg="gold", fg="black").grid(row=0, column=0)
    Label(space_est_per, text="Salud ", font=("Courier New", 12), bg="gold", fg="black").grid(row=0, column=1)
    Label(space_est_per, text="Social ", font=("Courier New", 12), bg="gold", fg="black").grid(row=0, column=2)
    Label(space_est_per, text="Economico ", font=("Courier New", 12), bg="gold", fg="black").grid(row=0, column=3)

    academico_pers , salud_pers, social_pers , economico_pers = IntVar(value = 0), IntVar(value = 0), IntVar(value = 0), IntVar(value = 0)


    Entry(space_est_per, textvariable = academico_pers, justify=CENTER, width=6).grid(row=1, column=0)
    dicc_estadisticas["Academico"].set(academico_pers)
    Entry(space_est_per, textvariable = salud_pers, justify=CENTER, width=6).grid(row=1, column=1)
    dicc_estadisticas["Salud"].set(salud_pers)
    Entry(space_est_per, textvariable = social_pers, justify=CENTER, width=6).grid(row=1, column=2)
    dicc_estadisticas["Social"].set(social_pers)
    Entry(space_est_per, textvariable = economico_pers, justify=CENTER, width=6).grid(row=1, column=3)
    dicc_estadisticas["Economico"].set(economico_pers)

    confirmar = Button(space_est_per, text="Ok", font=("Courier New", 10), fg="gold", bg="gray22",
                       command= lambda : confirmar_datos(dicc_imagenes,academico_pers , salud_pers, social_pers , economico_pers,dicc_ambitos,dicc_estadisticas,situaciones,trampa), width=10)
    confirmar.grid(column=1, row=2, pady=5)

def confimar_estandar(dicc_imagenes,dicc_estadisticas,situaciones,dicc_tortugas,dicc_ambitos):
    """
    Comprueba si el usuario ingreso caracteres para todos los datos solicitados en la funcion,
    "tutorial()" de ser asi invoca a la funcion "tutor_explicacion()", de lo contrario, invoca
    a la funcion "tutorial_est()".

    parametros:
        dicc_imagenes: diccionario que contiene las coordenadas y nombres de las imagenes de la
        situacion actual.
        dicc_estadisticas: diccionario que contiene las variables del modulo tkinter las
        cuales se proyectan en pantalla.
        situaciones: diccionario que contiene todas las posibles situaciones del juego.
        dicc_tortugas: diccionario que contiene las variables del modulo turtle.
        dicc_ambitos: dicc_ambitos: diccionario que contiene las variables de cada ambito del usuario.
    """
    if name.get() and Carrera.get() and Facultad.get():
        perfiles_inicio()
        tutor_explicacion(dicc_tortugas,dicc_imagenes,dicc_ambitos,dicc_estadisticas,situaciones)
    else:
        trampa = True
        tutorial_est(dicc_imagenes,dicc_estadisticas,situaciones,trampa)
        

def confirmar_datos(dicc_imagenes,academico_pers , salud_pers, social_pers , economico_pers,dicc_ambitos,dicc_estadisticas,situaciones,trampa):
    """
    Comprueba si el usuario ingreso caracteres para todos los datos solicitados en la funcion,
    "tutorial()", de ser asi inicializa el diccionario "dicc_tortugas" e invoca a la funcion
    "tutor_explicacion()", de lo contrario, invoca a la funcion "tutorial_per()".

    parametros:
        dicc_imagenes: diccionario que contiene las coordenadas y nombres de las imagenes de la
        situacion actual.
        dicc_estadisticas: diccionario que contiene las variables del modulo tkinter las
        cuales se proyectan en pantalla.
        situaciones: diccionario que contiene todas las posibles situaciones del juego.
        dicc_ambitos: diccionario que contiene las variables de cada ambito del usuario.
        academico_pers: variable entera del modulo tkinter.
        social_pers: variable entera del modulo tkinter.
        economico_pers: variable entera del modulo tkinter.
        salud_pers: variable entera del modulo tkinter.
    """
    try:
        dicc_ambitos["Academico_0"] = academico_pers.get()
        dicc_ambitos["Salud_0"] = salud_pers.get()
        dicc_ambitos["Social_0"] = social_pers.get()
        dicc_ambitos["Economico_0"] = economico_pers.get()
        if dicc_ambitos["Academico_0"] + dicc_ambitos["Economico_0"] + dicc_ambitos["Salud_0"] + dicc_ambitos["Social_0"] == 200 \
           and (dicc_ambitos["Academico_0"] > 1 and dicc_ambitos["Academico_0"] < 100) and (dicc_ambitos["Economico_0"] > 1 and dicc_ambitos["Economico_0"] < 100) \
           and (dicc_ambitos["Salud_0"] > 1 and dicc_ambitos["Salud_0"] < 100) and (dicc_ambitos["Social_0"] > 1 and dicc_ambitos["Social_0"] < 100) \
           and (name.get() and Facultad.get() and Carrera.get()):
            perfiles_inicio()
            dicc_tortugas = {}
            #codigo de turtle
            dicc_tortugas["academico_inicial"] = dicc_ambitos["Academico_0"] // 5
            dicc_tortugas["salud_inicial"] = dicc_ambitos["Salud_0"] // 5
            dicc_tortugas["social_inicial"] = dicc_ambitos["Social_0"] // 5
            dicc_tortugas["economico_inicial"] = dicc_ambitos["Economico_0"] // 5
            #codigo de turtle

            dicc_estadisticas["Academico"].set(dicc_ambitos["Academico_0"])
            dicc_estadisticas["Salud"].set(dicc_ambitos["Salud_0"])
            dicc_estadisticas["Social"].set(dicc_ambitos["Social_0"])
            dicc_estadisticas["Economico"].set(dicc_ambitos["Economico_0"])
            tutor_explicacion(dicc_tortugas,dicc_imagenes,dicc_ambitos,dicc_estadisticas,situaciones)
        else:
            trampa = True
            tutorial_per(dicc_imagenes,dicc_estadisticas,situaciones,trampa)
    except:
        trampa = True
        tutorial_per(dicc_imagenes,dicc_estadisticas,situaciones,trampa)

def v_situaciones_1(dicc_tortugas,dicc_imagenes,dicc_ambitos,dicc_estadisticas,situaciones,dicc_textos):
    """
    Despliega en pantalla los textos e imagenes de cada situacion, muestra
    graficamente los valores de las estadisticas, y habilita los botones opcion_1,
    opcion_2, opcion_3 dependiendo de si se quiere mostrar una situacion, o el
    resultado de una situacion.
    Si la situacion actual es la primera del programa, se inicializa el diccionario
    "dicc_tortugas" mediante la funcion "iniciar_tortugas()".
    El boton "opcion_1" y "opcion_2" invocan a la funcion "eleccion_1()" y
    "eleccion_2()", y el boton "opcion_3" invoca a la funcion "continuar()".

    parametros:
        dicc_tortugas: diccionario que contiene las variables del modulo turtle.
        dicc_imagenes: diccionario que contiene las coordenadas y nombres de las imagenes de la
        situacion actual.
        dicc_ambitos: diccionario que contiene las variables de cada ambito del usuario.
        dicc_estadisticas: diccionario que contiene las variables del modulo tkinter las
        cuales se proyectan en pantalla.
        situaciones: diccionario que contiene todas las posibles situaciones del juego.
        dicc_textos: diccionario que contiene los mensajes que se proyectan en pantalla .
    """
    #global situacion_a_usar, screen_situaciones, opcion_1, opcion_2, opcion_3
    global situacion_a_usar, screen_situaciones
    if situacion_a_usar == -1:
        screen_tutorial.withdraw()
        screen_situaciones = Toplevel()
        screen_situaciones.geometry("600x400+100+100")
        screen_situaciones.config(bg="black")
        puntaje_academico = dicc_tortugas["academico_inicial"]
        puntaje_economico = dicc_tortugas["economico_inicial"]
        puntaje_salud = dicc_tortugas["salud_inicial"]
        puntaje_social = dicc_tortugas["social_inicial"]
        dicc_tortugas = iniciar_tortugas()
        avanzar1(dicc_tortugas["AcademicoT"],puntaje_academico,dicc_tortugas["color_Academico"])
        avanzar1(dicc_tortugas["EconomicoT"],puntaje_economico,dicc_tortugas["color_Economico"])
        avanzar1(dicc_tortugas["SocialT"],puntaje_social,dicc_tortugas["color_Social"])
        avanzar1(dicc_tortugas["SaludT"],puntaje_salud,dicc_tortugas["color_Salud"])
        
        

    space_est = Frame(screen_situaciones, width=85, height=80)
    space_est.place(x = 0 , y =0)
    space_est.config(bg="black")

    space_est2 = Frame(screen_situaciones, width=50, height=100)
    space_est2.place(x = 550 , y =0)
    space_est2.config(bg="black")

    Label(space_est, text="academico", font=("Courier New", 9), bg="black", fg="DeepSkyBlue").place(x =0, y =0)
    Label(space_est, text="salud", font=("Courier New", 9), bg="black", fg="gold").place(x =0, y =15)
    Label(space_est, text="social", font=("Courier New", 9), bg="black", fg="green").place( x =0, y =30)
    Label(space_est, text="economico", font=("Courier New", 9), bg="black", fg="red").place( x =0, y =45)
    Label(space_est, text="semanas ", font=("Courier New", 9), bg="black", fg="silver").place(x =0, y =60)

    Label(space_est2, textvariable=dicc_estadisticas["Academico"], font=("Courier New", 9), bg="black", fg="DeepSkyBlue").place(x =10, y =0)
    Label(space_est2, textvariable=dicc_estadisticas["Salud"], font=("Courier New", 9), bg="black", fg="gold").place(x =10, y =15)
    Label(space_est2, textvariable=dicc_estadisticas["Social"], font=("Courier New", 9), bg="black", fg="green").place(x =10, y =30)
    Label(space_est2, textvariable=dicc_estadisticas["Economico"], font=("Courier New", 9), bg="black", fg="red").place(x =10, y =45)
    Label(space_est2, textvariable=dicc_estadisticas["semana"], font=("Courier New", 10), bg="black", fg="silver").place(x =10, y =60)
    
    space_situacion = Frame(screen_situaciones, width=480, height=300)
    space_situacion.place(x = 80 , y = 60)
    space_situacion.config(bg="black")
    # Imagen situaciones

    Label(screen_situaciones, image=dicc_imagenes["imagen"]).place(x=dicc_imagenes["coordenadas_imagen"][0], y= dicc_imagenes["coordenadas_imagen"][1])

    # Texto situaciones
    Label(space_situacion, textvariable=dicc_textos["txt_situacion"], font=("Courier New", 11), bg="gold", fg="black",
          justify=LEFT).place(x=10, y=10)

    if situacion_a_usar < 3:
        opcion_1 = Button(space_situacion, text="(1)", font=("Courier New", 10), fg="gold", bg="gray22",
                                  command= lambda : eleccion_1(dicc_tortugas,dicc_imagenes,dicc_ambitos,dicc_estadisticas,situaciones,dicc_textos),width=10)
        opcion_1.place(x=80, y=270)

        opcion_2 = Button(space_situacion, text="(2)", font=("Courier New", 10), fg="gold", bg="gray22",
                                  command= lambda : eleccion_2(dicc_tortugas,dicc_imagenes,dicc_ambitos,dicc_estadisticas,situaciones,dicc_textos),width=10)
        opcion_2.place(x=280, y=270)
            
        opcion_3 = Button(space_situacion, text="continuar", font=("Courier New", 10), fg="gold", bg="gray22",
                              command= lambda : situacion_jugar(dicc_tortugas,dicc_imagenes,dicc_ambitos,dicc_estadisticas,situaciones,dicc_textos))
        opcion_3.place(x= 180,y = 270)

        
    else:
        if resultado == False:
            opcion_1 = Button(space_situacion, text="(1)", font=("Courier New", 10), fg="gold", bg="gray22",
                              command= lambda : eleccion_1(dicc_tortugas,dicc_imagenes,dicc_ambitos,dicc_estadisticas,situaciones,dicc_textos),width=10)
            opcion_1.place(x=80, y=270)

            opcion_2 = Button(space_situacion, text="(2)", font=("Courier New", 10), fg="gold", bg="gray22",
                              command= lambda : eleccion_2(dicc_tortugas,dicc_imagenes,dicc_ambitos,dicc_estadisticas,situaciones,dicc_textos),width=10)
            opcion_2.place(x=280, y=270)

        else:

            opcion_3 = Button(space_situacion, text="continuar", font=("Courier New", 10), fg="gold", bg="gray22",
                              command= lambda : continuar(dicc_tortugas,dicc_imagenes,dicc_ambitos,dicc_estadisticas,situaciones,dicc_textos))
            opcion_3.place(x= 180,y = 270)
        
def v_puntajes():
    """
    Crea una pantalla del modulo tkinter donde el usuario puede acceder a los puntajes
    que haya obtenido en partidas anteriores, mediante el boton buscar(), el cual invoca
    a la funcion "verificar_perfiles()" de ser accionado.
    """
    perfiles, lista_archivos = leer_puntajes()
    screen_puntajes = Tk()
    screen_puntajes.resizable(False, False)
    screen_puntajes.geometry("600x400+100+100")
    screen_puntajes.title("Sobreviviendo en la UN")
    screen_puntajes.config(bg="black")

    datos = Frame(screen_puntajes, bg="black")
    datos.pack(pady=20)
    Label(datos, text="Usuario",bg="black", fg="gold", font=("Courier New", 15)).grid(row=0, column=0)
    Label(datos, text="Contraseña", bg="black", fg="gold", font=("Courier New", 15)).grid(row=1, column=0)

    entrada_usuario = StringVar(screen_puntajes)
    Entry(datos, justify=CENTER, textvariable=entrada_usuario).grid(row=0, column=1)

    entrada_contrasenia = IntVar(screen_puntajes)
    Entry(datos, justify=CENTER, textvariable=entrada_contrasenia).grid(row=1,column=1)

    buscar = Button(screen_puntajes, text="Buscar", font=("Courier New", 10), fg = "gold", bg="gray22",
                    command=lambda: verificar_perfiles(entrada_usuario, entrada_contrasenia, perfiles, lista_archivos, screen_puntajes))
    buscar.pack()

    salir = Button(screen_puntajes, text="Salir", font=("Courier New", 10), fg="gold", bg="gray22", command=screen_puntajes.destroy)
    salir.pack(pady=20)

def leer_puntajes():
    """
    Lee el archivo "records_usuario" y guarda este en la variable prueba, para
    conocer los puntajes actuales existentes en el programa.
    """
    prueba = open("records_usuario", "r")
    prueba.seek(0)
    lineas_archivo = []
    for linea in prueba:
        lectura = list(linea.rstrip().split(","))
        lineas_archivo.append(lectura)
    prueba.close()
    cont_puntajes = len(lineas_archivo)
    return cont_puntajes, lineas_archivo


def pantalla_game_over(dicc_imagenes,dicc_estadisticas,dicc_textos):
    """
    Despliega en pantalla un texto e imagen descriptivos del porque
    termino el juego.
    Guarda en un archivo el puntaje final del usuario.
    Mediante el boton "opcion_3" el usuario puede volver a jugar desde
    cero, llamando a la funcion "main()".
    
    parametros:
        dicc_imagenes: diccionario que contiene las coordenadas y nombres de las imagenes de la
        situacion actual.
        dicc_estadisticas: diccionario que contiene las variables del modulo tkinter las
        cuales se proyectan en pantalla.
        dicc_textos: diccionario que contiene los mensajes que se proyectan en pantalla.
    """
    global screen_situaciones
    screen_situaciones.withdraw()
    screen_situaciones = Toplevel()
    screen_situaciones.geometry("600x400+100+100")
    screen_situaciones.config(bg="black")

    space_est = Frame(screen_situaciones, width=500, height=80)
    space_est.pack(padx=5)
    space_est.config(bg="black")

    Label(space_est, text="Academico ", font=("Courier New", 9), bg="black", fg="gold").grid(row=0, column=0)
    Label(space_est, text="Salud ", font=("Courier New", 9), bg="black", fg="gold").grid(row=0, column=1)
    Label(space_est, text="Social ", font=("Courier New", 9), bg="black", fg="gold").grid(row=0, column=2)
    Label(space_est, text="Economico ", font=("Courier New", 9), bg="black", fg="gold").grid(row=0, column=3)
    Label(space_est, text="Semanas ", font=("Courier New", 9), bg="black", fg="gold").grid(row=0, column=4)

    Label(space_est, textvariable=dicc_estadisticas["Academico"], font=("Courier New", 9), bg="black", fg="gold").grid(row=1, column=0)
    Label(space_est, textvariable=dicc_estadisticas["Salud"], font=("Courier New", 9), bg="black", fg="gold").grid(row=1, column=1)
    Label(space_est, textvariable=dicc_estadisticas["Social"], font=("Courier New", 9), bg="black", fg="gold").grid(row=1, column=2)
    Label(space_est, textvariable=dicc_estadisticas["Economico"], font=("Courier New", 9), bg="black", fg="gold").grid(row=1, column=3)
    Label(space_est, textvariable=dicc_estadisticas["semana"], font=("Courier New", 9), bg="black", fg="gold").grid(row=1, column=4)

    space_situacion = Frame(screen_situaciones, width=500, height=300)
    space_situacion.pack(padx=5, pady=10)
    space_situacion.config(bg="black")
    # imagenes resultantes
    Label(screen_situaciones, image=dicc_imagenes["imagen"]).place(x=dicc_imagenes["coordenadas_imagen"][0], y=dicc_imagenes["coordenadas_imagen"][1])
    # Texto situaciones
    Label(space_situacion, textvariable=dicc_textos["txt_situacion"], font=("Courier New", 12), bg="gold", fg="black",
          justify=LEFT).place(x=10, y=10)
    Label(space_situacion, textvariable=name, font=("Courier New", 12), bg="gold", fg="black",
          justify=LEFT).place(x=10, y=100)
    Label(space_situacion, textvariable=Facultad, font=("Courier New", 12), bg="gold", fg="black",
          justify=LEFT).place(x=10, y=150)
    Label(space_situacion, textvariable=Carrera, font=("Courier New", 12), bg="gold", fg="black",
          justify=LEFT).place(x=10, y=200)

    record = open("records_usuario", "a+")
    encontrado = False
    perfiles, lineas_archivo = leer_puntajes()
    for i in range(len(lineas_archivo)):
        if name == lineas_archivo[i][0]:
            encontrado = True
            puntaje_actual = (dicc_estadisticas["Academico"].get() + dicc_estadisticas["Salud"].get() + dicc_estadisticas["Social"] + dicc_economico) * dicc_estadisticas["semana"].get()
            datos = [int(num) for num in lineas_archivo[i][2:6]]
            puntaje = sum(datos[:4]) * datos[4]
            if puntaje_actual>puntaje:
                lineas_archivo[i][2] = dicc_estadisticas["Academico"].get()
                lineas_archivo[i][3] = dicc_estadisticas["Salud"].get()
                lineas_archivo[i][4] = dicc_estadisticas["Social"].get()
                lineas_archivo[i][5] = dicc_estadisticas["Economico"].get()
                lineas_archivo[i][6] = dicc_estadisticas["semana"].get()
    if encontrado == False:
        record.write("{},{},{},{},{},{},{}\n".format(name.get(), password(),dicc_estadisticas["Academico"].get(), dicc_estadisticas["Salud"].get(), dicc_estadisticas["Social"].get(),
                                    dicc_estadisticas["Economico"].get(), dicc_estadisticas["semana"].get()))
    else:
        record.seek(0)
        for lineas in lineas_archivo:
            record.write(lineas)
    record.close()

    global opcion_3
    opcion_3 = Button(screen_situaciones, text="volver al menu", font=("Courier New", 10), fg="gold", bg="gray22",
                      command=lambda: [screen_inicio.destroy(), main()])
    opcion_3.pack(side=BOTTOM)


def tutor_explicacion(dicc_tortugas,dicc_imagenes,dicc_ambitos,dicc_estadisticas,situaciones):
    """
    Cambia los valores de los diccionarios "dicc_ambitos", "dicc_textos", y de las variables
    situacion_extensa_1 y situacion_extensa_2.
    Invoca a la funcion "password()".
    Invoca a la funcion "v_situaciones_1()"
    
    parametros:
        dicc_tortugas: diccionario que contiene las variables del modulo turtle.
        dicc_imagenes: diccionario que contiene las coordenadas y nombres de las imagenes de la
        situacion actual.
        dicc_ambitos: diccionario que contiene las variables de cada ambito del usuario.
        dicc_estadisticas: diccionario que contiene las variables del modulo tkinter las
        cuales se proyectan en pantalla.
        situaciones: diccionario que contiene todas las posibles situaciones del juego.
    """
    global situacion_extensa_1, situacion_extensa_2
    situacion_extensa_1 = 0
    situacion_extensa_2 = 0
    #password()

    dicc_ambitos["Academico_1"] = dicc_ambitos["Academico_0"]
    dicc_ambitos["Academico_2"] = dicc_ambitos["Academico_0"]
    dicc_ambitos["Social_1"] = dicc_ambitos["Social_0"]
    dicc_ambitos["Social_2"] = dicc_ambitos["Social_0"]
    dicc_ambitos["Salud_1"] = dicc_ambitos["Salud_0"]
    dicc_ambitos["Salud_2"] = dicc_ambitos["Salud_0"]
    dicc_ambitos["Economico_1"] = dicc_ambitos["Economico_0"]
    dicc_ambitos["Economico_2"] = dicc_ambitos["Economico_0"]



    dicc_textos = {}
    dicc_textos["txt_1"] = "Bienvenido a la semana de induccion\nAhi esta tu tutor, ¿vas a hablar con el?\n(1) Si\n(2) Si\n(continuar) Ya conoces como va esto..."
    dicc_textos["txt_2"] = "Bienvenido a la semana de induccion\nAhi esta tu tutor, ¿vas a hablar con el?\n(1) Si\n(2) Si\n(continuar) Ya conoces como va esto..."
    dicc_textos["txt_situacion"] = StringVar(
        value="Bienvenido a la semana de induccion\nAhi esta tu tutor, ¿vas a hablar con el?\n(1) Si\n(2) Si\n(continuar) Ya conoces como va esto...")
    v_situaciones_1(dicc_tortugas,dicc_imagenes,dicc_ambitos,dicc_estadisticas,situaciones,dicc_textos)


def textos_situacion_tutor(dicc_tortugas,dicc_imagenes,dicc_ambitos,dicc_estadisticas,situaciones,dicc_textos):
    """
    Cambia los valores de los diccionarios "dicc_ambitos", "dicc_textos", e invoca a la funcion
    "v_situaciones_1()".
    
    parametros:
        dicc_tortugas: diccionario que contiene las variables del modulo turtle.
        dicc_imagenes: diccionario que contiene las coordenadas y nombres de las imagenes de la
        situacion actual.
        dicc_ambitos: diccionario que contiene las variables de cada ambito del usuario.
        dicc_estadisticas: diccionario que contiene las variables del modulo tkinter las
        cuales se proyectan en pantalla.
        situaciones: diccionario que contiene todas las posibles situaciones del juego.
        dicc_textos: diccionario que contiene los mensajes que se proyectan en pantalla.
    """
    dicc_textos["txt_1"] = "Para sobrevivir en la U tienes que\nmanejar bien tu vida, es decir los ambitos\nmas importantes\n-El Academico\n-El Economico\n-El Social\n-Tu Salud"
    dicc_textos["txt_2"] = "Para sobrevivir en la U tienes que\nmanejar bien tu vida, es decir los ambitos\nmas importantes\n-El Academico\n-El Economico\n-El Social\n-Tu Salud"
    dicc_textos["txt_situacion"].set(dicc_textos["txt_1"])
    v_situaciones_1(dicc_tortugas,dicc_imagenes,dicc_ambitos,dicc_estadisticas,situaciones,dicc_textos)


def textos_situacion_tutor2(dicc_tortugas,dicc_imagenes,dicc_ambitos,dicc_estadisticas,situaciones,dicc_textos):
    """
    Cambia los valores de los diccionarios "dicc_ambitos", "dicc_textos", e invoca a la funcion
    "v_situaciones_1()".

    parametros:
        dicc_tortugas: diccionario que contiene las variables del modulo turtle.
        dicc_imagenes: diccionario que contiene las coordenadas y nombres de las imagenes de la
        situacion actual.
        dicc_ambitos: diccionario que contiene las variables de cada ambito del usuario.
        dicc_estadisticas: diccionario que contiene las variables del modulo tkinter las
        cuales se proyectan en pantalla.
        situaciones: diccionario que contiene todas las posibles situaciones del juego.
        dicc_textos: diccionario que contiene los mensajes que se proyectan en pantalla.
    """
    dicc_textos["txt_1"] = "Tus deciciones afectaran tu desempeño\nTen cuidado con cada elección que haces\nPodria ser la ultima...\nNO te aceleres a tomar decisiones, siempre\nespera a ver su resultado, o algo podria\nsalir mal(NO HAGAS CLICK EN LOS BOTONES\nHASTA QUE TUS ESTADISTICAS SE ESTABILICEN)"
    dicc_textos["txt_2"] = "Tus deciciones afectaran tu desempeño\nTen cuidado con cada elección que haces\nPodria ser la ultima...\nNO te aceleres a tomar decisiones, siempre\nespera a ver su resultado, o algo podria\nsalir mal(NO HAGAS CLICK EN LOS BOTONES\nHASTA QUE TUS ESTADISTICAS SE ESTABILICEN)"
    dicc_textos["txt_situacion"].set(dicc_textos["txt_1"])
    v_situaciones_1(dicc_tortugas,dicc_imagenes,dicc_ambitos,dicc_estadisticas,situaciones,dicc_textos)


def textos_situacion_tutor3(dicc_tortugas,dicc_imagenes,dicc_ambitos,dicc_estadisticas,situaciones,dicc_textos):
    """
    Cambia los valores de los diccionarios "dicc_ambitos", "dicc_textos", e invoca a la funcion
    "v_situaciones_1()".

    parametros:
        dicc_tortugas: diccionario que contiene las variables del modulo turtle.
        dicc_imagenes: diccionario que contiene las coordenadas y nombres de las imagenes de la
        situacion actual.
        dicc_ambitos: diccionario que contiene las variables de cada ambito del usuario.
        dicc_estadisticas: diccionario que contiene las variables del modulo tkinter las
        cuales se proyectan en pantalla.
        situaciones: diccionario que contiene todas las posibles situaciones del juego.
        dicc_textos: diccionario que contiene los mensajes que se proyectan en pantalla.
    """
    dicc_textos["txt_1"] = "Tu tutor sale del salon y no lo vuelves\nA ver en todo el semestre"
    dicc_textos["txt_2"] = "Tu tutor sale del salon y no lo vuelves\nA ver en todo el semestre"
    dicc_textos["txt_situacion"].set(dicc_textos["txt_1"])
    v_situaciones_1(dicc_tortugas,dicc_imagenes,dicc_ambitos,dicc_estadisticas,situaciones,dicc_textos)


def situacion_jugar(dicc_tortugas,dicc_imagenes,dicc_ambitos,dicc_estadisticas,situaciones,dicc_textos):
    """
    Cambia los valores de los diccionarios "dicc_ambitos", "dicc_textos", "dicc_imagenes", "dicc_tortugas"
    y de las variables "situacion_a_usar", "situacion_extensa_1" y "situacion_extensa_2"
    Invoca a la funcion "v_situaciones_1()".
    Corresponde a una situacion simple, por lo que la situacion que sigue a esta es aleatoria.

    parametros:
        dicc_tortugas: diccionario que contiene las variables del modulo turtle.
        dicc_imagenes: diccionario que contiene las coordenadas y nombres de las imagenes de la
        situacion actual.
        dicc_ambitos: diccionario que contiene las variables de cada ambito del usuario.
        dicc_estadisticas: diccionario que contiene las variables del modulo tkinter las
        cuales se proyectan en pantalla.
        situaciones: diccionario que contiene todas las posibles situaciones del juego.
        dicc_textos: diccionario que contiene los mensajes que se proyectan en pantalla.
    """
    global situacion_a_usar, situacion_extensa_1, situacion_extensa_2

    dicc_imagenes["imagen"] = PhotoImage(file="rsz_imagen_jugar.png")
    dicc_imagenes["imagen_1"] = PhotoImage(file="jugar_1.png")
    dicc_imagenes["imagen_2"] = PhotoImage(file="jugar_2.png")
    dicc_imagenes["coordenadas_imagen"] = (200, 170)
    dicc_imagenes["coordenadas_imagen_1"] = (183, 170)
    dicc_imagenes["coordenadas_imagen_2"] = (135, 150)

    situacion_a_usar = 3
    situacion_extensa_1 = 0
    situacion_extensa_2 = 0
    dicc_textos["txt_situacion"].set("Tienes un poco de sueño pero tus amigos \nte invitan a jugar una partida\n(1)irte a dormir"
                      " (Salud-Social)\n(2)Jugar una partida (Salud-Social)")
    dicc_textos["txt_1"] = "Mejor duermo, \nno es conveniente trasnocharme"
    dicc_textos["txt_2"] = "Una partidita no hace daño, pero\nterminas jugando hasta las 2 a.m"

    dicc_ambitos["Academico_1"] = dicc_ambitos["Academico_0"]
    dicc_ambitos["Academico_2"] = dicc_ambitos["Academico_0"]
    dicc_ambitos["Social_1"] = dicc_ambitos["Social_0"] - 5
    dicc_ambitos["Social_2"] = dicc_ambitos["Social_0"] + 5
    dicc_ambitos["Salud_1"] = dicc_ambitos["Salud_0"] + 5
    dicc_ambitos["Salud_2"] = dicc_ambitos["Salud_0"] - 10
    dicc_ambitos["Economico_1"] = dicc_ambitos["Economico_0"]
    dicc_ambitos["Economico_2"] = dicc_ambitos["Economico_0"]

    #codigo turtle
    dicc_tortugas["tortuga_academico1"] = 0
    dicc_tortugas["tortuga_academico2"] = 0
    dicc_tortugas["tortuga_social1"] = -1
    dicc_tortugas["tortuga_social2"] = 1
    dicc_tortugas["tortuga_salud1"] = 1
    dicc_tortugas["tortuga_salud2"] = -2
    dicc_tortugas["tortuga_economico1"] = 0
    dicc_tortugas["tortuga_economico2"] = 0
    #codigo turtle
    v_situaciones_1(dicc_tortugas,dicc_imagenes,dicc_ambitos,dicc_estadisticas,situaciones,dicc_textos)


def situacion_bicirrun(dicc_tortugas,dicc_imagenes,dicc_ambitos,dicc_estadisticas,situaciones,dicc_textos):
    """
    Cambia los valores de los diccionarios "dicc_ambitos", "dicc_textos", "dicc_imagenes" y "dicc_tortugas".
    Invoca a la funcion "v_situaciones_1()".
    Corresponde a una situacion simple, por lo que la situacion que sigue a esta es aleatoria.

    parametros:
        dicc_tortugas: diccionario que contiene las variables del modulo turtle.
        dicc_imagenes: diccionario que contiene las coordenadas y nombres de las imagenes de la
        situacion actual.
        dicc_ambitos: diccionario que contiene las variables de cada ambito del usuario.
        dicc_estadisticas: diccionario que contiene las variables del modulo tkinter las
        cuales se proyectan en pantalla.
        situaciones: diccionario que contiene todas las posibles situaciones del juego.
        dicc_textos: diccionario que contiene los mensajes que se proyectan en pantalla.
    """
    global situacion_extensa_1, situacion_extensa_2

    dicc_imagenes["imagen"] = PhotoImage(file="bicirrun.png")
    dicc_imagenes["imagen_1"] = PhotoImage(file="bicirrun_1.png")
    dicc_imagenes["imagen_2"] = PhotoImage(file="bicirrun_2.png")
    dicc_imagenes["coordenadas_imagen"] = (200, 160)
    dicc_imagenes["coordenadas_imagen_1"] = (175, 160)
    dicc_imagenes["coordenadas_imagen_2"] = (200, 160)

    situacion_extensa_1 = 0
    situacion_extensa_2 = 0
    
    dicc_textos["txt_situacion"].set(
        "Vas de camino a clases, disfruntando \nmiras la hora, y te das cuenta que vas tarde\n(1)Usar bicirrun"
        " (Salud)\n(2)Ir caminando (Academico)")
    dicc_textos["txt_1"] = "llegare más rapido si voy \nen bici"
    dicc_textos["txt_2"] = "Solo llegare tarde unos 15 \nminuticos"

    dicc_ambitos["Academico_1"] = dicc_ambitos["Academico_0"]
    dicc_ambitos["Academico_2"] = dicc_ambitos["Academico_0"] - 5
    dicc_ambitos["Social_1"] = dicc_ambitos["Social_0"]
    dicc_ambitos["Social_2"] = dicc_ambitos["Social_0"]
    dicc_ambitos["Salud_1"] = dicc_ambitos["Salud_0"] + 5
    dicc_ambitos["Salud_2"] = dicc_ambitos["Salud_0"]
    dicc_ambitos["Economico_1"] = dicc_ambitos["Economico_0"]
    dicc_ambitos["Economico_2"] = dicc_ambitos["Economico_0"]

    #codigo turtle
    dicc_tortugas["tortuga_academico1"] = 0
    dicc_tortugas["tortuga_academico2"] = -1
    dicc_tortugas["tortuga_social1"] = 0
    dicc_tortugas["tortuga_social2"] = 0
    dicc_tortugas["tortuga_salud1"] = 1
    dicc_tortugas["tortuga_salud2"] = 0
    dicc_tortugas["tortuga_economico1"] = 0
    dicc_tortugas["tortuga_economico2"] = 0
    #codigo turtle

    
    v_situaciones_1(dicc_tortugas,dicc_imagenes,dicc_ambitos,dicc_estadisticas,situaciones,dicc_textos)


def situacion_amigos(dicc_tortugas,dicc_imagenes,dicc_ambitos,dicc_estadisticas,situaciones,dicc_textos):
    """
    Cambia los valores de los diccionarios "dicc_ambitos", "dicc_textos", "dicc_imagenes" y "dicc_tortugas".
    Invoca a la funcion "v_situaciones_1()".
    Corresponde a una situacion simple, por lo que la situacion que sigue a esta es aleatoria.

    parametros:
        dicc_tortugas: diccionario que contiene las variables del modulo turtle.
        dicc_imagenes: diccionario que contiene las coordenadas y nombres de las imagenes de la
        situacion actual.
        dicc_ambitos: diccionario que contiene las variables de cada ambito del usuario.
        dicc_estadisticas: diccionario que contiene las variables del modulo tkinter las
        cuales se proyectan en pantalla.
        situaciones: diccionario que contiene todas las posibles situaciones del juego.
        dicc_textos: diccionario que contiene los mensajes que se proyectan en pantalla.
    """
    global situacion_extensa_1, situacion_extensa_2

    dicc_imagenes["imagen"] = PhotoImage(file="amigos.png")
    dicc_imagenes["imagen_1"] = PhotoImage(file="amigos_1.png")
    dicc_imagenes["imagen_2"] = PhotoImage(file="amigos_2.png")
    dicc_imagenes["coordenadas_imagen"] = (165, 175)
    dicc_imagenes["coordenadas_imagen_1"] = (210, 160)
    dicc_imagenes["coordenadas_imagen_2"] = (140, 140)
    
    situacion_extensa_1 = 0
    situacion_extensa_2 = 0
    dicc_textos["txt_situacion"].set(
        "Acabaste las clases del dia y tus \namigos te invitan a pasar la tarde en la U\npero tu querias estudiar en casa\n(1)Quedarse en la U"
        " (Social-Academico)\n(2)Irte a casa a estudiar (Social-Academico)")
    dicc_textos["txt_1"] = "Me quedare por hoy"
    dicc_textos["txt_2"] = "Primero el estudio, despues el ocio"

    dicc_ambitos["Academico_1"] = dicc_ambitos["Academico_0"] - 10
    dicc_ambitos["Academico_2"] = dicc_ambitos["Academico_0"] + 15
    dicc_ambitos["Social_1"] = dicc_ambitos["Social_0"] + 15
    dicc_ambitos["Social_2"] = dicc_ambitos["Social_0"] - 10
    dicc_ambitos["Salud_1"] = dicc_ambitos["Salud_0"]
    dicc_ambitos["Salud_2"] = dicc_ambitos["Salud_0"]
    dicc_ambitos["Economico_1"] = dicc_ambitos["Economico_0"]
    dicc_ambitos["Economico_2"] = dicc_ambitos["Economico_0"]

    #codigo turtle
    dicc_tortugas["tortuga_academico1"] = -2
    dicc_tortugas["tortuga_academico2"] = 3
    dicc_tortugas["tortuga_social1"] = 3
    dicc_tortugas["tortuga_social2"] = -2
    dicc_tortugas["tortuga_salud1"] = 0
    dicc_tortugas["tortuga_salud2"] = 0
    dicc_tortugas["tortuga_economico1"] = 0
    dicc_tortugas["tortuga_economico2"] = 0
    #codigo turtle
    
    v_situaciones_1(dicc_tortugas,dicc_imagenes,dicc_ambitos,dicc_estadisticas,situaciones,dicc_textos)


def situacion_parcial_biblioteca(dicc_tortugas,dicc_imagenes,dicc_ambitos,dicc_estadisticas,situaciones,dicc_textos):
    """
    Cambia los valores de los diccionarios "dicc_ambitos", "dicc_textos", "dicc_imagenes" y "dicc_tortugas".
    Invoca a la funcion "v_situaciones_1()".
    Corresponde a una situacion simple, por lo que la situacion que sigue a esta es aleatoria.

    parametros:
        dicc_tortugas: diccionario que contiene las variables del modulo turtle.
        dicc_imagenes: diccionario que contiene las coordenadas y nombres de las imagenes de la
        situacion actual.
        dicc_ambitos: diccionario que contiene las variables de cada ambito del usuario.
        dicc_estadisticas: diccionario que contiene las variables del modulo tkinter las
        cuales se proyectan en pantalla.
        situaciones: diccionario que contiene todas las posibles situaciones del juego.
        dicc_textos: diccionario que contiene los mensajes que se proyectan en pantalla.
    """
    dicc_imagenes["imagen"] = PhotoImage(file="parcial_biblioteca.png")
    dicc_imagenes["imagen_1"] = PhotoImage(file="parcial_biblioteca_1.png")
    dicc_imagenes["imagen_2"] = PhotoImage(file="parcial_biblioteca_1.png")
    dicc_imagenes["coordenadas_imagen"] = (177, 175)
    dicc_imagenes["coordenadas_imagen_1"] = (160, 130)
    dicc_imagenes["coordenadas_imagen_2"] = (160, 130)

    dicc_textos["txt_situacion"].set(
        "Es semana de parciales, estudiaras en tu casa\no te quedaras en la U en la biblioteca 24 horas\n(1)Quedarse en la U (Academico-Salud)"
        "\n(2)Irse a la casa a estudiar (Academico)")
    dicc_textos["txt_1"] = "Necesito todo el tiempo disponible"
    dicc_textos["txt_2"] = "Prefiero estudiar en casa"

    dicc_ambitos["Academico_1"] = dicc_ambitos["Academico_0"] + 15
    dicc_ambitos["Academico_2"] = dicc_ambitos["Academico_0"] + 5
    dicc_ambitos["Social_1"] = dicc_ambitos["Social_0"]
    dicc_ambitos["Social_2"] = dicc_ambitos["Social_0"]
    dicc_ambitos["Salud_1"] = dicc_ambitos["Salud_0"] - 10
    dicc_ambitos["Salud_2"] = dicc_ambitos["Salud_0"]
    dicc_ambitos["Economico_1"] = dicc_ambitos["Economico_0"]
    dicc_ambitos["Economico_2"] = dicc_ambitos["Economico_0"]

    #codigo turtle
    dicc_tortugas["tortuga_academico1"] = 3
    dicc_tortugas["tortuga_academico2"] = 1
    dicc_tortugas["tortuga_social1"] = 0
    dicc_tortugas["tortuga_social2"] = 0
    dicc_tortugas["tortuga_salud1"] = -2
    dicc_tortugas["tortuga_salud2"] = 0
    dicc_tortugas["tortuga_economico1"] = 0
    dicc_tortugas["tortuga_economico2"] = 0
    #codigo turtle
    
    v_situaciones_1(dicc_tortugas,dicc_imagenes,dicc_ambitos,dicc_estadisticas,situaciones,dicc_textos)


def situacion_parcial(dicc_tortugas,dicc_imagenes,dicc_ambitos,dicc_estadisticas,situaciones,dicc_textos):
    """
    Cambia los valores de los diccionarios "dicc_ambitos", "dicc_textos", "dicc_imagenes" y "dicc_tortugas".
    Invoca a la funcion "v_situaciones_1()".
    Corresponde a una situacion simple, por lo que la situacion que sigue a esta es aleatoria.

    parametros:
        dicc_tortugas: diccionario que contiene las variables del modulo turtle.
        dicc_imagenes: diccionario que contiene las coordenadas y nombres de las imagenes de la
        situacion actual.
        dicc_ambitos: diccionario que contiene las variables de cada ambito del usuario.
        dicc_estadisticas: diccionario que contiene las variables del modulo tkinter las
        cuales se proyectan en pantalla.
        situaciones: diccionario que contiene todas las posibles situaciones del juego.
        dicc_textos: diccionario que contiene los mensajes que se proyectan en pantalla.
    """
    dicc_imagenes["imagen"] = PhotoImage(file="parcial_biblioteca.png")
    dicc_imagenes["imagen_1"] = PhotoImage(file="parcial_1.png")
    dicc_imagenes["imagen_2"] = PhotoImage(file="parcial_2.png")
    dicc_imagenes["coordenadas_imagen"] = (177, 175)
    dicc_imagenes["coordenadas_imagen_1"] = (190, 160)
    dicc_imagenes["coordenadas_imagen_2"] = (190, 160)

    dicc_textos["txt_situacion"].set(
        "LLegaste a tu casa demasiado tarde,\nes de noche pero mañana tienes un parcial\n(1)Irte a dormir (Academico-Salud)"
        "\n(2)Estudiar (Academico-Salud)")
    dicc_textos["txt_1"] = "Mejor duermo para no estar cansado\nmañana"
    dicc_textos["txt_2"] = "Necesito estudiar, tengo miedo"

    dicc_ambitos["Academico_1"] = dicc_ambitos["Academico_0"] - 10
    dicc_ambitos["Academico_2"] = dicc_ambitos["Academico_0"] + 10
    dicc_ambitos["Social_1"] = dicc_ambitos["Social_0"]
    dicc_ambitos["Social_2"] = dicc_ambitos["Social_0"]
    dicc_ambitos["Salud_1"] = dicc_ambitos["Salud_0"] + 5
    dicc_ambitos["Salud_2"] = dicc_ambitos["Salud_0"] - 10
    dicc_ambitos["Economico_1"] = dicc_ambitos["Economico_0"]
    dicc_ambitos["Economico_2"] = dicc_ambitos["Economico_0"]

    #codigo turtle
    dicc_tortugas["tortuga_academico1"] = -2
    dicc_tortugas["tortuga_academico2"] = 2
    dicc_tortugas["tortuga_social1"] = 0
    dicc_tortugas["tortuga_social2"] = 0
    dicc_tortugas["tortuga_salud1"] = 1
    dicc_tortugas["tortuga_salud2"] = -2
    dicc_tortugas["tortuga_economico1"] = 0
    dicc_tortugas["tortuga_economico2"] = 0
    #codigo turtle
    
    v_situaciones_1(dicc_tortugas,dicc_imagenes,dicc_ambitos,dicc_estadisticas,situaciones,dicc_textos)


def situacion_danza(dicc_tortugas,dicc_imagenes,dicc_ambitos,dicc_estadisticas,situaciones,dicc_textos):
    """
    Cambia los valores de los diccionarios "dicc_ambitos", "dicc_textos", "dicc_imagenes" y "dicc_tortugas".
    Invoca a la funcion "v_situaciones_1()".
    Corresponde a una situacion simple, por lo que la situacion que sigue a esta es aleatoria.

    parametros:
        dicc_tortugas: diccionario que contiene las variables del modulo turtle.
        dicc_imagenes: diccionario que contiene las coordenadas y nombres de las imagenes de la
        situacion actual.
        dicc_ambitos: diccionario que contiene las variables de cada ambito del usuario.
        dicc_estadisticas: diccionario que contiene las variables del modulo tkinter las
        cuales se proyectan en pantalla.
        situaciones: diccionario que contiene todas las posibles situaciones del juego.
        dicc_textos: diccionario que contiene los mensajes que se proyectan en pantalla.
    """
    dicc_imagenes["imagen"] = PhotoImage(file="danza.png")
    dicc_imagenes["imagen_1"] = PhotoImage(file="danza_1.png")
    dicc_imagenes["imagen_2"] = PhotoImage(file="danza_2.png")
    dicc_imagenes["coordenadas_imagen"] = (205, 150)
    dicc_imagenes["coordenadas_imagen_1"] = (175, 140)
    dicc_imagenes["coordenadas_imagen_2"] = (175, 140)

    dicc_textos["txt_situacion"].set(
        "Ves un cartel sobre un curso de danza, \nPero estas un poco colgado en algunas materias\n(1)Inscribirte (Academico-Social-Economico)"
        "\n(2)centrarte en lo Academico (Academico)")
    dicc_textos["txt_1"] = "Necesito distraerme de vez en cuando"
    dicc_textos["txt_2"] = "No me queda tiempo para eso"

    dicc_ambitos["Academico_1"] = dicc_ambitos["Academico_0"] - 10
    dicc_ambitos["Academico_2"] = dicc_ambitos["Academico_0"] + 15
    dicc_ambitos["Social_1"] = dicc_ambitos["Social_0"] + 20
    dicc_ambitos["Social_2"] = dicc_ambitos["Social_0"]
    dicc_ambitos["Salud_1"] = dicc_ambitos["Salud_0"]
    dicc_ambitos["Salud_2"] = dicc_ambitos["Salud_0"]
    dicc_ambitos["Economico_1"] = dicc_ambitos["Economico_0"] - 10
    dicc_ambitos["Economico_2"] = dicc_ambitos["Economico_0"]

    #codigo turtle
    dicc_tortugas["tortuga_academico1"] = -2
    dicc_tortugas["tortuga_academico2"] = 3
    dicc_tortugas["tortuga_social1"] = 4
    dicc_tortugas["tortuga_social2"] = 0
    dicc_tortugas["tortuga_salud1"] = 0
    dicc_tortugas["tortuga_salud2"] = 0
    dicc_tortugas["tortuga_economico1"] = -2
    dicc_tortugas["tortuga_economico2"] = 0
    #codigo turtle

    v_situaciones_1(dicc_tortugas,dicc_imagenes,dicc_ambitos,dicc_estadisticas,situaciones,dicc_textos)


def situacion_tropel(dicc_tortugas,dicc_imagenes,dicc_ambitos,dicc_estadisticas,situaciones,dicc_textos):
    """
    Cambia los valores de los diccionarios "dicc_ambitos", "dicc_textos", "dicc_imagenes", "dicc_tortugas"
    y de la variable "situacion_extensa_1".
    Invoca a la funcion "v_situaciones_1()".
    Corresponde a una situacion extensa, por lo que la situacion que sigue puede ser "situacion_tropel_1" o
    una situacion aleatoria, dependiendo de la eleccion hecha por el usuario posteriormente en la funcion
    "v_situaciones_1()".

    parametros:
        dicc_tortugas: diccionario que contiene las variables del modulo turtle.
        dicc_imagenes: diccionario que contiene las coordenadas y nombres de las imagenes de la
        situacion actual.
        dicc_ambitos: diccionario que contiene las variables de cada ambito del usuario.
        dicc_estadisticas: diccionario que contiene las variables del modulo tkinter las
        cuales se proyectan en pantalla.
        situaciones: diccionario que contiene todas las posibles situaciones del juego.
        dicc_textos: diccionario que contiene los mensajes que se proyectan en pantalla.
    """
    global  situacion_extensa_1

    dicc_imagenes["imagen"] = PhotoImage(file="tropel.png")
    dicc_imagenes["imagen_1"] = PhotoImage(file="tropel_1.png")
    dicc_imagenes["imagen_2"] = PhotoImage(file="tropel_2.png")
    dicc_imagenes["coordenadas_imagen"] = (205, 150)
    dicc_imagenes["coordenadas_imagen_1"] = (230, 150)
    dicc_imagenes["coordenadas_imagen_2"] = (160, 110)

    dicc_textos["txt_situacion"].set(
        "Vas de salida de la U pero hay un tropel\njusto por donde casi siempre sales\n(1)Quedarte a ver (?)"
        "\n(2)Buscar otra salida (Nada de nada...)")
    dicc_textos["txt_1"] = "Vere solo un rato"
    dicc_textos["txt_2"] = "Das media vuelta y te vas a tu casa"
    situacion_extensa_1 = 50

    dicc_ambitos["Academico_1"] = dicc_ambitos["Academico_0"]
    dicc_ambitos["Academico_2"] = dicc_ambitos["Academico_0"]
    dicc_ambitos["Social_1"] = dicc_ambitos["Social_0"]
    dicc_ambitos["Social_2"] = dicc_ambitos["Social_0"]
    dicc_ambitos["Salud_1"] = dicc_ambitos["Salud_0"]
    dicc_ambitos["Salud_2"] = dicc_ambitos["Salud_0"]
    dicc_ambitos["Economico_1"] = dicc_ambitos["Economico_0"]
    dicc_ambitos["Economico_2"] = dicc_ambitos["Economico_0"]

    #codigo turtle
    dicc_tortugas["tortuga_academico1"] = 0
    dicc_tortugas["tortuga_academico2"] = 0
    dicc_tortugas["tortuga_social1"] = 0
    dicc_tortugas["tortuga_social2"] = 0
    dicc_tortugas["tortuga_salud1"] = 0
    dicc_tortugas["tortuga_salud2"] = 0
    dicc_tortugas["tortuga_economico1"] = 0
    dicc_tortugas["tortuga_economico2"] = 0
    #codigo turtle
    
    v_situaciones_1(dicc_tortugas,dicc_imagenes,dicc_ambitos,dicc_estadisticas,situaciones,dicc_textos)


def situacion_tropel_1(dicc_tortugas,dicc_imagenes, dicc_ambitos,dicc_estadisticas,situaciones,dicc_textos):
    """
    Cambia los valores de los diccionarios "dicc_ambitos", "dicc_textos", "dicc_imagenes", "dicc_tortugas"
    y de la variable "situacion_extensa_1".
    Invoca a la funcion "v_situaciones_1()".
    Corresponde al final de una situacion extensa, por lo que la situacion que siguea esta es aleatoria.
    
    parametros:
        dicc_tortugas: diccionario que contiene las variables del modulo turtle.
        dicc_imagenes: diccionario que contiene las coordenadas y nombres de las imagenes de la
        situacion actual.
        dicc_ambitos: diccionario que contiene las variables de cada ambito del usuario.
        dicc_estadisticas: diccionario que contiene las variables del modulo tkinter las
        cuales se proyectan en pantalla.
        situaciones: diccionario que contiene todas las posibles situaciones del juego.
        dicc_textos: diccionario que contiene los mensajes que se proyectan en pantalla.
    """
    global situacion_extensa_1

    dicc_imagenes["imagen"] = PhotoImage(file="tropel_1_1.png")
    dicc_imagenes["imagen_1"] = PhotoImage(file="tropel_1_1_1.png")
    dicc_imagenes["imagen_2"] = PhotoImage(file="tropel_1_1_2.png")
    dicc_imagenes["coordenadas_imagen"] = (220, 150)
    dicc_imagenes["coordenadas_imagen_1"] = (190, 130)
    dicc_imagenes["coordenadas_imagen_2"] = (200, 130)

    dicc_textos["txt_situacion"].set(
        "Vere solo un rato\n(1)Ver de cerca (?)"
        "\n(2)Ver de lejos (?)")
    dicc_textos["txt_1"] = "No paso nada..."
    dicc_textos["txt_2"] = "Te cayo una granada lacrimogena a tu lado..."
    situacion_extensa_1 = 0

    dicc_ambitos["Academico_1"] = dicc_ambitos["Academico_0"]
    dicc_ambitos["Academico_2"] = dicc_ambitos["Academico_0"]
    dicc_ambitos["Social_1"] = dicc_ambitos["Social_0"]
    dicc_ambitos["Social_2"] = dicc_ambitos["Social_0"]
    dicc_ambitos["Salud_1"] = dicc_ambitos["Salud_0"]
    dicc_ambitos["Salud_2"] = dicc_ambitos["Salud_0"] - 15
    dicc_ambitos["Economico_1"] = dicc_ambitos["Economico_0"]
    dicc_ambitos["Economico_2"] = dicc_ambitos["Economico_0"]

    #codigo turtle
    dicc_tortugas["tortuga_salud2"] = -3
    #codigo turtle
    
    v_situaciones_1(dicc_tortugas,dicc_imagenes,dicc_ambitos,dicc_estadisticas,situaciones,dicc_textos)


def situacion_comer(dicc_tortugas,dicc_imagenes,dicc_ambitos,dicc_estadisticas,situaciones,dicc_textos):
    """
    Cambia los valores de los diccionarios "dicc_ambitos", "dicc_textos", "dicc_imagenes", "dicc_tortugas"
    y de las variables "situacion_extensa_1" y "situacion_extensa_2".
    Invoca a la funcion "v_situaciones_1()".
    Corresponde a una situacion extensa, por lo que la situacion que sigue puede ser "situacion_comer_1" o
    "situacion_comer_2", dependiendo de la eleccion hecha por el usuario posteriormente en la funcion
    "v_situaciones_1()".

    parametros:
        dicc_tortugas: diccionario que contiene las variables del modulo turtle.
        dicc_imagenes: diccionario que contiene las coordenadas y nombres de las imagenes de la
        situacion actual.
        dicc_ambitos: diccionario que contiene las variables de cada ambito del usuario.
        dicc_estadisticas: diccionario que contiene las variables del modulo tkinter las
        cuales se proyectan en pantalla.
        situaciones: diccionario que contiene todas las posibles situaciones del juego.
        dicc_textos: diccionario que contiene los mensajes que se proyectan en pantalla.
    """
    global situacion_extensa_1, situacion_extensa_2

    dicc_imagenes["imagen"] = PhotoImage(file="comer.png")
    dicc_imagenes["imagen_1"] = PhotoImage(file="comer_1.png")
    dicc_imagenes["imagen_2"] = PhotoImage(file="comer_2.png")
    dicc_imagenes["coordenadas_imagen"] = (240, 170)
    dicc_imagenes["coordenadas_imagen_1"] = (190, 110)
    dicc_imagenes["coordenadas_imagen_2"] = (120, 90)

    dicc_textos["txt_situacion"].set(
        "Sales de clase al medio día y tienes bastante\nhambre piensas si comeras en una\nchaza o en una cafeteria\n(1)Comer en una chaza (Salud-Economico)"
        "\n(2)Comer en una cafeteria (?)")
    dicc_textos["txt_1"] = "Hoy quiero algo distinto, comere en una\nchaza"
    dicc_textos["txt_2"] = "No me fio de esas chazas, ire a una cafeteria"
    situacion_extensa_1 = 51
    situacion_extensa_2 = 52

    dicc_ambitos["Academico_1"] = dicc_ambitos["Academico_0"]
    dicc_ambitos["Academico_2"] = dicc_ambitos["Academico_0"]
    dicc_ambitos["Social_1"] = dicc_ambitos["Social_0"]
    dicc_ambitos["Social_2"] = dicc_ambitos["Social_0"]
    dicc_ambitos["Salud_1"] = dicc_ambitos["Salud_0"] - 15
    dicc_ambitos["Salud_2"] = dicc_ambitos["Salud_0"]
    dicc_ambitos["Economico_1"] = dicc_ambitos["Economico_0"] - 5
    dicc_ambitos["Economico_2"] = dicc_ambitos["Economico_0"]

    #codigo turtle
    dicc_tortugas["tortuga_academico1"] = 0
    dicc_tortugas["tortuga_academico2"] = 0
    dicc_tortugas["tortuga_social1"] = 0
    dicc_tortugas["tortuga_social2"] = 0
    dicc_tortugas["tortuga_salud1"] = -3
    dicc_tortugas["tortuga_salud2"] = 0
    dicc_tortugas["tortuga_economico1"] = -1
    dicc_tortugas["tortuga_economico2"] = 0
    #codigo turtle
    
    v_situaciones_1(dicc_tortugas,dicc_imagenes,dicc_ambitos,dicc_estadisticas,situaciones,dicc_textos)


def situacion_comer_1(dicc_tortugas,dicc_imagenes,dicc_ambitos,dicc_estadisticas,situaciones,dicc_textos):
    """
    Cambia los valores de los diccionarios "dicc_ambitos", "dicc_textos", "dicc_imagenes", "dicc_tortugas"
    y de las variables "situacion_extensa_1" y "situacion_extensa_2".
    Invoca a la funcion "v_situaciones_1()".
    Corresponde al final de una situacion extensa, por lo que la situacion que sigue a esta es aleatoria.

    parametros:
        dicc_tortugas: diccionario que contiene las variables del modulo turtle.
        dicc_imagenes: diccionario que contiene las coordenadas y nombres de las imagenes de la
        situacion actual.
        dicc_ambitos: diccionario que contiene las variables de cada ambito del usuario.
        dicc_estadisticas: diccionario que contiene las variables del modulo tkinter las
        cuales se proyectan en pantalla.
        situaciones: diccionario que contiene todas las posibles situaciones del juego.
        dicc_textos: diccionario que contiene los mensajes que se proyectan en pantalla.
    """
    global situacion_extensa_1, situacion_extensa_2

    dicc_imagenes["imagen"] = PhotoImage(file="comer_1_1.png")
    dicc_imagenes["imagen_1"] = PhotoImage(file="comer_1_1_1.png")
    dicc_imagenes["imagen_2"] = PhotoImage(file="comer_1_1_2.png")
    dicc_imagenes["coordenadas_imagen"] = (210, 170)
    dicc_imagenes["coordenadas_imagen_1"] = (180, 180)
    dicc_imagenes["coordenadas_imagen_2"] = (230, 140)

    dicc_textos["txt_situacion"].set(
        "Eres muy salad@ y te enfermaste\n(1)Ir a la enfermeria (Salud)"
        "\n(2)Ir a la clase (?)")
    dicc_textos["txt_1"] = "No puedo ir a clase así, mejor voy\na la enfermeria\n(al poco tiempo de estar en la enfermeria)\n¡Milagrosamente de curaste!"
    dicc_textos["txt_2"] = "Esta clase es muy importante, mejor\nno me la pierdo. Llegas al lugar de la clase\n a esperar al profesor pero despues de " \
            "una hora\nte das cuenta que no asistira"
    situacion_extensa_1 = 0
    situacion_extensa_2 = 0

    dicc_ambitos["Academico_1"] = dicc_ambitos["Academico_0"]
    dicc_ambitos["Academico_2"] = dicc_ambitos["Academico_0"]
    dicc_ambitos["Social_1"] = dicc_ambitos["Social_0"]
    dicc_ambitos["Social_2"] = dicc_ambitos["Social_0"]
    dicc_ambitos["Salud_1"] = dicc_ambitos["Salud_0"] + 15
    dicc_ambitos["Salud_2"] = dicc_ambitos["Salud_0"]
    dicc_ambitos["Economico_1"] = dicc_ambitos["Economico_0"]
    dicc_ambitos["Economico_2"] = dicc_ambitos["Economico_0"]

    #codigo turtle
    dicc_tortugas["tortuga_academico1"] = 0
    dicc_tortugas["tortuga_academico2"] = 0
    dicc_tortugas["tortuga_social1"] = 0
    dicc_tortugas["tortuga_social2"] = 0
    dicc_tortugas["tortuga_salud1"] = 3
    dicc_tortugas["tortuga_salud2"] = 0
    dicc_tortugas["tortuga_economico1"] = 0
    dicc_tortugas["tortuga_economico2"] = 0
    #codigo turtle
    
    v_situaciones_1(dicc_tortugas,dicc_imagenes,dicc_ambitos,dicc_estadisticas,situaciones,dicc_textos)


def situacion_comer_2(dicc_tortugas,dicc_imagenes,dicc_ambitos,dicc_estadisticas,situaciones,dicc_textos):
    """
    Cambia los valores de los diccionarios "dicc_ambitos", "dicc_textos", "dicc_imagenes", "dicc_tortugas"
    y de las variables "situacion_extensa_1" y "situacion_extensa_2" y hace uso del modulo random para
    obtener un valor aleatorio guardado en la varibale "billete".
    Invoca a la funcion "v_situaciones_1()".
    Corresponde al final de una situacion extensa, por lo que la situacion que sigue a esta es aleatoria.

    parametros:
        dicc_tortugas: diccionario que contiene las variables del modulo turtle.
        dicc_imagenes: diccionario que contiene las coordenadas y nombres de las imagenes de la
        situacion actual.
        dicc_ambitos: diccionario que contiene las variables de cada ambito del usuario.
        dicc_estadisticas: diccionario que contiene las variables del modulo tkinter las
        cuales se proyectan en pantalla.
        situaciones: diccionario que contiene todas las posibles situaciones del juego.
        dicc_textos: diccionario que contiene los mensajes que se proyectan en pantalla.
    """
    global situacion_extensa_1, situacion_extensa_2
    dicc_imagenes["imagen"] = PhotoImage(file="comer_2_1.png")
    dicc_imagenes["imagen_1"] = PhotoImage(file="comer_2_1_1.png")
    dicc_imagenes["imagen_2"] = PhotoImage(file="comer_2_1_2.png")
    dicc_imagenes["coordenadas_imagen"] = (235, 190)
    dicc_imagenes["coordenadas_imagen_1"] = (180, 140)
    dicc_imagenes["coordenadas_imagen_2"] = (240, 160)

    dicc_textos["txt_situacion"].set(
        "Al llegar te encuentras una fila gigantesca y\n tienes poco tiempo antes de tu otra clase\n"
        "\n(1)Esperare, no me aguanto el hambre (?)"
        "\n(2)No puedo esperar tanto tiempo,\ndebo ir a clase (Salud-Academico)")
    dicc_textos["txt_1"] = "La fila no resulto  ser tan larga, y en ella\n¡te encuentras un billete!"
    dicc_textos["txt_2"] = "Te diriges a tu clase con demasiada hambre\ny no logras concentrarte"
    situacion_extensa_1 = 0
    situacion_extensa_2 = 0

    dicc_ambitos["Academico_1"] = dicc_ambitos["Academico_0"]
    dicc_ambitos["Academico_2"] = dicc_ambitos["Academico_0"] - 5
    dicc_ambitos["Social_1"] = dicc_ambitos["Social_0"]
    dicc_ambitos["Social_2"] = dicc_ambitos["Social_0"]
    dicc_ambitos["Salud_1"] = dicc_ambitos["Salud_0"]
    dicc_ambitos["Salud_2"] = dicc_ambitos["Salud_0"] - 10
    lista_valores_billete = [5,10,15]
    billete = random.choice(lista_valores_billete)
    dicc_ambitos["Economico_1"] = dicc_ambitos["Economico_0"] + billete
    dicc_ambitos["Economico_2"] = dicc_ambitos["Economico_0"]

    #codigo turtle
    dicc_tortugas["tortuga_academico1"] = 0
    dicc_tortugas["tortuga_academico2"] = 0
    dicc_tortugas["tortuga_social1"] = 0
    dicc_tortugas["tortuga_social2"] = -1
    dicc_tortugas["tortuga_salud1"] = 0
    dicc_tortugas["tortuga_salud2"] = -2
    dicc_tortugas["tortuga_economico1"] = billete // 5
    dicc_tortugas["tortuga_economico2"] = 0
    #codigo turtle
    
    v_situaciones_1(dicc_tortugas,dicc_imagenes,dicc_ambitos,dicc_estadisticas,situaciones,dicc_textos)


def situacion_copia(dicc_tortugas,dicc_imagenes,dicc_ambitos,dicc_estadisticas,situaciones,dicc_textos):
    """
    Cambia los valores de los diccionarios "dicc_ambitos", "dicc_textos", "dicc_imagenes", "dicc_tortugas" y
    hace uso del modulo random para obtener un valor aleatorio guardado en la variable "evento".
    Invoca a la funcion "v_situaciones_1()".
    Corresponde a una situacion simple, por lo que la situacion que le sigue a esta es aleatoria.

    parametros:
        dicc_tortugas: diccionario que contiene las variables del modulo turtle.
        dicc_imagenes: diccionario que contiene las coordenadas y nombres de las imagenes de la
        situacion actual.
        dicc_ambitos: diccionario que contiene las variables de cada ambito del usuario.
        dicc_estadisticas: diccionario que contiene las variables del modulo tkinter las
        cuales se proyectan en pantalla.
        situaciones: diccionario que contiene todas las posibles situaciones del juego.
        dicc_textos: diccionario que contiene los mensajes que se proyectan en pantalla.
    """
    global situacion_extensa_1, situacion_extensa_2

    dicc_imagenes["imagen"] = PhotoImage(file="copiar.png")
    dicc_imagenes["imagen_1"] = PhotoImage(file="copiar_1.png")
    dicc_imagenes["imagen_2"] = PhotoImage(file="copiar_2.png")
    dicc_imagenes["coordenadas_imagen"] = (225, 113)
    dicc_imagenes["coordenadas_imagen_1"] = (220, 180)
    dicc_imagenes["coordenadas_imagen_2"] = (150, 140)

    dicc_textos["txt_situacion"].set(
        "Adivina que.. ¡parcial sopresa! (1)Copiar (?)"
        "\n(2)A la de Diosito (Academico)")
    evento = random.randint(0, 100)
    if evento >= 0 and evento <= 50:
        dicc_textos["txt_1"] = "No quiero perder esta nota, voy a copiar\n...\nObtuviste la mejor nota de la clase\npero... ¿para que?"
        dicc_ambitos["Academico_1"] = dicc_ambitos["Academico_0"] + 20
        #codigo de turtle
        dicc_tortugas["tortuga_academico1"] = 4
        #codigo de turtle
    elif evento >= 51 and evento <= 100:
        dicc_textos["txt_1"] = "No quiero perder esta nota, voy a copiar\n...\nEl profesor te descubre con las manos en la \nmasa, pero solo te anula esta nota\nTe baja el promedio"
        dicc_ambitos["Academico_1"] = dicc_ambitos["Academico_0"] - 30
        #codigo de turtle
        dicc_tortugas["tortuga_academico1"] = -6
        #codigo de turtle
    if dicc_ambitos["Academico_0"] > 50:
        if evento >= 0 and evento <= 50:
            dicc_textos["txt_2"] = "Al pinochazo\n...\nperdiste el quiz"
            dicc_ambitos["Academico_2"] = dicc_ambitos["Academico_0"] - 20
            #codigo de turtle
            dicc_tortugas["tortuga_academico2"] = -4
            #codigo de turtle
        elif evento >= 50 and evento <= 100:
            dicc_textos["txt_2"] = "Al pinochazo\n...\nSirvio haber estudiado estos ultimos días"
            dicc_ambitos["Academico_2"] = dicc_ambitos["Academico_0"] + 10
            #codigo de turlte
            dicc_tortugas["tortuga_academico2"] = 2
            #codigo de turtle
    else:
        if evento >= 0 and evento <= 70:
            dicc_textos["txt_2"] = "Al pinochazo\n...\nperdiste el quiz"
            dicc_ambitos["Academico_2"] = dicc_ambitos["Academico_0"] - 20
            #codigo de turtle
            dicc_tortugas["tortuga_academico2"] = -4
            #codigo de turtle
        elif evento >= 71 and evento <= 100:
            dicc_textos["txt_2"] = "Al pinochazo\n...\nNo sabes como, pero pasaste raspando"
            dicc_ambitos["Academico_2"] = dicc_ambitos["Academico_0"] + 10
            #codigo de turtle
            dicc_tortugas["tortuga_academico2"] = 2
            #codigo de turtle
            
    dicc_ambitos["Social_1"] = dicc_ambitos["Social_0"]
    dicc_ambitos["Social_2"] = dicc_ambitos["Social_0"]
    dicc_ambitos["Salud_1"] = dicc_ambitos["Salud_0"]
    dicc_ambitos["Salud_2"] = dicc_ambitos["Salud_0"]
    dicc_ambitos["Economico_1"] = dicc_ambitos["Economico_0"]
    dicc_ambitos["Economico_2"] = dicc_ambitos["Economico_0"]

    #codigo turtle
    dicc_tortugas["tortuga_social1"] = 0
    dicc_tortugas["tortuga_social2"] = 0
    dicc_tortugas["tortuga_salud1"] = 0
    dicc_tortugas["tortuga_salud2"] = 0
    dicc_tortugas["tortuga_economico1"] = 0
    dicc_tortugas["tortuga_economico2"] = 0
    #codigo turtle
    
    v_situaciones_1(dicc_tortugas,dicc_imagenes,dicc_ambitos,dicc_estadisticas,situaciones,dicc_textos)


def situacion_prestamo(dicc_tortugas,dicc_imagenes,dicc_ambitos,dicc_estadisticas,situaciones,dicc_textos):
    """
    Cambia los valores de los diccionarios "dicc_ambitos", "dicc_textos", "dicc_imagenes", "dicc_tortugas".
    Invoca a la funcion "v_situaciones_1()".
    Corresponde a una situacion simple, por lo que la situacion que le sigue a esta es aleatoria.

    parametros:
        dicc_tortugas: diccionario que contiene las variables del modulo turtle.
        dicc_imagenes: diccionario que contiene las coordenadas y nombres de las imagenes de la
        situacion actual.
        dicc_ambitos: diccionario que contiene las variables de cada ambito del usuario.
        dicc_estadisticas: diccionario que contiene las variables del modulo tkinter las
        cuales se proyectan en pantalla.
        situaciones: diccionario que contiene todas las posibles situaciones del juego.
        dicc_textos: diccionario que contiene los mensajes que se proyectan en pantalla.
    """
    dicc_imagenes["imagen"] = PhotoImage(file="prestamo.png")
    dicc_imagenes["imagen_1"] = PhotoImage(file="prestamo_1.png")
    dicc_imagenes["imagen_2"] = PhotoImage(file="prestamo_2.png")
    dicc_imagenes["coordenadas_imagen"] = (210, 170)
    dicc_imagenes["coordenadas_imagen_1"] = (180, 130)
    dicc_imagenes["coordenadas_imagen_2"] = (150, 160)

    dicc_textos["txt_situacion"].set("Vas caminando con un amigo, y te pide\nprestado para unas fotocopias\n(1)Prestarle a tu amigo"
                      " (Economico-Social)\n(2)Decirle que solo tienes lo justo (Social)")
    dicc_textos["txt_1"] = "Claro que le prestas, igualmente no era\nmucho dinero..."
    dicc_textos["txt_2"] = "Eran 800 pesos..."

    dicc_ambitos["Academico_1"] = dicc_ambitos["Academico_0"]
    dicc_ambitos["Academico_2"] = dicc_ambitos["Academico_0"]
    dicc_ambitos["Social_1"] = dicc_ambitos["Social_0"] + 10
    dicc_ambitos["Social_2"] = dicc_ambitos["Social_0"] - 10
    dicc_ambitos["Salud_1"] = dicc_ambitos["Salud_0"]
    dicc_ambitos["Salud_2"] = dicc_ambitos["Salud_0"]
    dicc_ambitos["Economico_1"] = dicc_ambitos["Economico_0"] - 5
    dicc_ambitos["Economico_2"] = dicc_ambitos["Economico_0"]

    #codigo turtle
    dicc_tortugas["tortuga_academico1"] = 0
    dicc_tortugas["tortuga_academico2"] = 0
    dicc_tortugas["tortuga_social1"] = 2
    dicc_tortugas["tortuga_social2"] = -2
    dicc_tortugas["tortuga_salud1"] = 0
    dicc_tortugas["tortuga_salud2"] = 0
    dicc_tortugas["tortuga_economico1"] = -1
    dicc_tortugas["tortuga_economico2"] = 0
    #codigo turtle
    
    v_situaciones_1(dicc_tortugas,dicc_imagenes,dicc_ambitos,dicc_estadisticas,situaciones,dicc_textos)


def situacion_freud(dicc_tortugas,dicc_imagenes,dicc_ambitos,dicc_estadisticas,situaciones,dicc_textos):
    """
    Cambia los valores de los diccionarios "dicc_ambitos", "dicc_textos", "dicc_imagenes", "dicc_tortugas"
    y de las variables "situacion_extensa_1" y "situacion_extensa_2".
    Invoca a la funcion "v_situaciones_1()".
    Corresponde a una situacion extensa, por lo que la situacion que sigue puede ser "situacion_freud_1" o
    una situacion aleatoria, dependiendo de la eleccion hecha por el usuario posteriormente en la funcion
    "v_situaciones_1()".

    parametros:
        dicc_tortugas: diccionario que contiene las variables del modulo turtle.
        dicc_imagenes: diccionario que contiene las coordenadas y nombres de las imagenes de la
        situacion actual.
        dicc_ambitos: diccionario que contiene las variables de cada ambito del usuario.
        dicc_estadisticas: diccionario que contiene las variables del modulo tkinter las
        cuales se proyectan en pantalla.
        situaciones: diccionario que contiene todas las posibles situaciones del juego.
        dicc_textos: diccionario que contiene los mensajes que se proyectan en pantalla.
    """
    global situacion_extensa_1, situacion_extensa_2

    dicc_imagenes["imagen"] = PhotoImage(file="freud.png")
    dicc_imagenes["imagen_1"] = PhotoImage(file="freud_1.png")
    dicc_imagenes["imagen_2"] = PhotoImage(file="freud_2.png")
    dicc_imagenes["coordenadas_imagen"] = (220, 140)
    dicc_imagenes["coordenadas_imagen_1"] = (180, 140)
    dicc_imagenes["coordenadas_imagen_2"] = (220, 180)

    dicc_textos["txt_situacion"].set(
        "Es jueves por la tarde y pasas por el Freud,\ntodos parecen divertirse (1)Quedarte un rato (?)"
        "\n(2)Irte a estudiar (Academico-Social)")
    dicc_textos["txt_1"] = "Me quedare solo un rato"
    dicc_textos["txt_2"] = "Otro día quizas..."
    situacion_extensa_1 = 53
    situacion_extensa_2 = 0

    dicc_ambitos["Academico_1"] = dicc_ambitos["Academico_0"]
    dicc_ambitos["Academico_2"] = dicc_ambitos["Academico_0"] + 10
    dicc_ambitos["Social_1"] = dicc_ambitos["Social_0"]
    dicc_ambitos["Social_2"] = dicc_ambitos["Social_0"] - 10
    dicc_ambitos["Salud_1"] = dicc_ambitos["Salud_0"]
    dicc_ambitos["Salud_2"] = dicc_ambitos["Salud_0"]
    dicc_ambitos["Economico_1"] = dicc_ambitos["Economico_0"]
    dicc_ambitos["Economico_2"] = dicc_ambitos["Economico_0"]

    #codigo turtle
    dicc_tortugas["tortuga_academico1"] = 0
    dicc_tortugas["tortuga_academico2"] = 2
    dicc_tortugas["tortuga_social1"] = 0
    dicc_tortugas["tortuga_social2"] = -2
    dicc_tortugas["tortuga_salud1"] = 0
    dicc_tortugas["tortuga_salud2"] = 0
    dicc_tortugas["tortuga_economico1"] = 0
    dicc_tortugas["tortuga_economico2"] = 0
    #codigo turtle
    
    v_situaciones_1(dicc_tortugas,dicc_imagenes,dicc_ambitos,dicc_estadisticas,situaciones,dicc_textos)


def situacion_freud_1(dicc_tortugas,dicc_imagenes,dicc_ambitos,dicc_estadisticas,situaciones,dicc_textos):
    """
    Cambia los valores de los diccionarios "dicc_ambitos", "dicc_textos", "dicc_imagenes", "dicc_tortugas"
    y de las variables "situacion_extensa_1" y "situacion_extensa_2".
    Invoca a la funcion "v_situaciones_1()".
    Corresponde a una situacion extensa, por lo que la situacion que sigue es "situacion_freud_2".
    parametros:
        dicc_tortugas: diccionario que contiene las variables del modulo turtle.
        dicc_imagenes: diccionario que contiene las coordenadas y nombres de las imagenes de la
        situacion actual.
        dicc_ambitos: diccionario que contiene las variables de cada ambito del usuario.
        dicc_estadisticas: diccionario que contiene las variables del modulo tkinter las
        cuales se proyectan en pantalla.
        situaciones: diccionario que contiene todas las posibles situaciones del juego.
        dicc_textos: diccionario que contiene los mensajes que se proyectan en pantalla.
    """
    global situacion_extensa_1, situacion_extensa_2

    dicc_imagenes["imagen"] = PhotoImage(file="freud_1_1.png")
    dicc_imagenes["imagen_1"] = PhotoImage(file="freud_1_1_1.png")
    # imagen reutilizada
    dicc_imagenes["imagen_2"] = PhotoImage(file="tropel_1_1_2.png")
    dicc_imagenes["coordenadas_imagen"] = (180, 135)
    dicc_imagenes["coordenadas_imagen_1"] = (180, 140)
    dicc_imagenes["coordenadas_imagen_2"] = (190, 150)

    dicc_textos["txt_situacion"].set(
        "A lo lejos ves algunos amigos tuyos\n(1)Juntarte con ellos (Social)"
        "\n(2)Ir solo, tratar de conocer a alguie mas (Social)")
    dicc_textos["txt_1"] = "Prefiero estar con alguien conocido"
    dicc_textos["txt_2"] = "Nadie te habla"
    situacion_extensa_1 = 54
    situacion_extensa_2 = 54

    dicc_ambitos["Academico_1"] = dicc_ambitos["Academico_0"]
    dicc_ambitos["Academico_2"] = dicc_ambitos["Academico_0"]
    dicc_ambitos["Social_1"] = dicc_ambitos["Social_0"] + 10
    dicc_ambitos["Social_2"] = dicc_ambitos["Social_0"] - 5
    dicc_ambitos["Salud_1"] = dicc_ambitos["Salud_0"]
    dicc_ambitos["Salud_2"] = dicc_ambitos["Salud_0"]
    dicc_ambitos["Economico_1"] = dicc_ambitos["Economico_0"]
    dicc_ambitos["Economico_2"] = dicc_ambitos["Economico_0"]

    #codigo turtle
    dicc_tortugas["tortuga_academico1"] = 0
    dicc_tortugas["tortuga_academico2"] = 0
    dicc_tortugas["tortuga_social1"] = 2
    dicc_tortugas["tortuga_social2"] = -1
    dicc_tortugas["tortuga_salud1"] = 0
    dicc_tortugas["tortuga_salud2"] = 0
    dicc_tortugas["tortuga_economico1"] = 0
    dicc_tortugas["tortuga_economico2"] = 0
    #codigo turtle
    
    v_situaciones_1(dicc_tortugas,dicc_imagenes,dicc_ambitos,dicc_estadisticas,situaciones,dicc_textos)


def situacion_freud_2(dicc_tortugas,dicc_imagenes,dicc_ambitos,dicc_estadisticas,situaciones,dicc_textos):
    """
    Cambia los valores de los diccionarios "dicc_ambitos", "dicc_textos", "dicc_imagenes", "dicc_tortugas"
    y de las variables "situacion_extensa_1" y "situacion_extensa_2".
    Invoca a la funcion "v_situaciones_1()".
    Corresponde a una situacion extensa, por lo que la situacion que sigue es "situacion_freud_3".

    parametros:
        dicc_tortugas: diccionario que contiene las variables del modulo turtle.
        dicc_imagenes: diccionario que contiene las coordenadas y nombres de las imagenes de la
        situacion actual.
        dicc_ambitos: diccionario que contiene las variables de cada ambito del usuario.
        dicc_estadisticas: diccionario que contiene las variables del modulo tkinter las
        cuales se proyectan en pantalla.
        situaciones: diccionario que contiene todas las posibles situaciones del juego.
        dicc_textos: diccionario que contiene los mensajes que se proyectan en pantalla.
    """
    global situacion_extensa_1, situacion_extensa_2

    dicc_imagenes["imagen"] = PhotoImage(file="freud_2_1.png")
    dicc_imagenes["imagen_2"] = PhotoImage(file="freud_2_1_2.png")
    dicc_imagenes["coordenadas_imagen"] = (220, 140)
    dicc_imagenes["coordenadas_imagen_2"] = (215, 180)

    dicc_textos["txt_situacion"].set(
        "Te ofrecen una bebida misteriosa\n(1)Aceptar (?)"
        "\n(2)Rechazar (Nada de nada...)")
    dicc_textos["txt_2"] = "No gracias, así estoy bien"
    situacion_extensa_1 = 55
    situacion_extensa_2 = 55
    evento = random.randint(0, 100)
    if evento >= 0 and evento <= 50:
        dicc_imagenes["imagen_1"] = PhotoImage(file="freud_2_1_0.png")
        dicc_textos["txt_1"] = "Pruebas la bebida\n...\nEra una deliciosa bebida artesanal"
        dicc_imagenes["coordenadas_imagen_1"] = (140, 140)
        dicc_ambitos["Social_1"] = dicc_ambitos["Social_0"] + 5
        dicc_ambitos["Salud_1"] = dicc_ambitos["Salud_0"]
        #codigo de turtle
        dicc_tortugas["tortuga_social1"] = 1
        dicc_tortugas["tortuga_salud1"] = 0
        #codigo de turtle
    elif evento >= 51 and evento <= 100:
        dicc_imagenes["imagen_1"] = PhotoImage(file="freud_2_1_1.png")
        dicc_textos["txt_1"] = "Pruebas la bebida\n...\nTe sientes bastante mareado"
        dicc_imagenes["coordenadas_imagen_1"] = (200, 130)
        dicc_ambitos["Salud_1"] = dicc_ambitos["Salud_0"] - 15
        dicc_ambitos["Social_1"] = dicc_ambitos["Social_0"]
        #codigo de turtle
        dicc_tortugas["tortuga_social1"] = 0
        dicc_tortugas["tortuga_salud1"] = -3
        #codigo de turtle
        
    dicc_ambitos["Academico_1"] = dicc_ambitos["Academico_0"]
    dicc_ambitos["Academico_2"] = dicc_ambitos["Academico_0"]
    dicc_ambitos["Social_2"] = dicc_ambitos["Social_0"]
    dicc_ambitos["Salud_2"] = dicc_ambitos["Salud_0"]
    dicc_ambitos["Economico_1"] = dicc_ambitos["Economico_0"]
    dicc_ambitos["Economico_2"] = dicc_ambitos["Economico_0"]

    #codigo turtle
    dicc_tortugas["tortuga_academico1"] = 0
    dicc_tortugas["tortuga_academico2"] = 0
    dicc_tortugas["tortuga_social2"] = 0
    dicc_tortugas["tortuga_salud2"] = 0
    dicc_tortugas["tortuga_economico1"] = 0
    dicc_tortugas["tortuga_economico2"] = 0
    #codigo turtle
    
    v_situaciones_1(dicc_tortugas,dicc_imagenes,dicc_ambitos,dicc_estadisticas,situaciones,dicc_textos)


def situacion_freud_3(dicc_tortugas,dicc_imagenes,dicc_ambitos,dicc_estadisticas,situaciones,dicc_textos):
    """
    Cambia los valores de los diccionarios "dicc_ambitos", "dicc_textos", "dicc_imagenes", "dicc_tortugas"
    y de las variables "situacion_extensa_1" y "situacion_extensa_2".
    Invoca a la funcion "v_situaciones_1()".
    Corresponde a una situacion extensa, por lo que la situacion que sigue puede ser "situacion_freud_4" o
    una situacion aleatoria, dependiendo de la eleccion hecha por el usuario posteriormente en la funcion
    "v_situaciones_1()".

    parametros:
        dicc_tortugas: diccionario que contiene las variables del modulo turtle.
        dicc_imagenes: diccionario que contiene las coordenadas y nombres de las imagenes de la
        situacion actual.
        dicc_ambitos: diccionario que contiene las variables de cada ambito del usuario.
        dicc_estadisticas: diccionario que contiene las variables del modulo tkinter las
        cuales se proyectan en pantalla.
        situaciones: diccionario que contiene todas las posibles situaciones del juego.
        dicc_textos: diccionario que contiene los mensajes que se proyectan en pantalla.
    """
    global situacion_extensa_1, situacion_extensa_2

    dicc_imagenes["imagen"] = PhotoImage(file="freud_tiempo_1.png")
    # imagen reutilizada
    dicc_imagenes["imagen_1"] = PhotoImage(file="tropel_1_1_1.png")
    # imagen reutilizada
    dicc_imagenes["imagen_2"] = PhotoImage(file="bicirrun_2.png")
    dicc_imagenes["coordenadas_imagen"] = (200, 160)
    dicc_imagenes["coordenadas_imagen_1"] = (180, 140)
    dicc_imagenes["coordenadas_imagen_2"] = (200, 160)

    dicc_textos["txt_situacion"].set(
        "Ves como empieza a atardecer, te\niras a tu casa\n(1)Quedarte (?)"
        "\n(2)Irte a tu casa (Nada de nada...)")
    dicc_textos["txt_1"] = "Solo un ratico mas"
    dicc_textos["txt_2"] = "Pasaste un buen rato"
    situacion_extensa_1 = 56
    situacion_extensa_2 = 0

    dicc_ambitos["Academico_1"] = dicc_ambitos["Academico_0"]
    dicc_ambitos["Academico_2"] = dicc_ambitos["Academico_0"]
    dicc_ambitos["Social_1"] = dicc_ambitos["Social_0"]
    dicc_ambitos["Social_2"] = dicc_ambitos["Social_0"]
    dicc_ambitos["Salud_1"] = dicc_ambitos["Salud_0"]
    dicc_ambitos["Salud_2"] = dicc_ambitos["Salud_0"]
    dicc_ambitos["Economico_1"] = dicc_ambitos["Economico_0"]
    dicc_ambitos["Economico_2"] = dicc_ambitos["Economico_0"]

    #codigo turtle
    dicc_tortugas["tortuga_academico1"] = 0
    dicc_tortugas["tortuga_academico2"] = 0
    dicc_tortugas["tortuga_social1"] = 0
    dicc_tortugas["tortuga_social2"] = 0
    dicc_tortugas["tortuga_salud1"] = 0
    dicc_tortugas["tortuga_salud2"] = 0
    dicc_tortugas["tortuga_economico1"] = 0
    dicc_tortugas["tortuga_economico2"] = 0
    #codigo turtle
    
    v_situaciones_1(dicc_tortugas,dicc_imagenes,dicc_ambitos,dicc_estadisticas,situaciones,dicc_textos)


def situacion_freud_4(dicc_tortugas,dicc_imagenes,dicc_ambitos,dicc_estadisticas,situaciones,dicc_textos):
    """
    Cambia los valores de los diccionarios "dicc_ambitos", "dicc_textos", "dicc_imagenes", "dicc_tortugas"
    y de las variables "situacion_extensa_1" y "situacion_extensa_2".
    Invoca a la funcion "v_situaciones_1()".
    Corresponde a una situacion extensa, por lo que la situacion que sigue puede ser "situacion_comer_1" o
    "situacion_comer_2", dependiendo de la eleccion hecha por el usuario posteriormente en la funcion
    "v_situaciones_1()".

    parametros:
        dicc_tortugas: diccionario que contiene las variables del modulo turtle.
        dicc_imagenes: diccionario que contiene las coordenadas y nombres de las imagenes de la
        situacion actual.
        dicc_ambitos: diccionario que contiene las variables de cada ambito del usuario.
        dicc_estadisticas: diccionario que contiene las variables del modulo tkinter las
        cuales se proyectan en pantalla.
        situaciones: diccionario que contiene todas las posibles situaciones del juego.
        dicc_textos: diccionario que contiene los mensajes que se proyectan en pantalla.
    """
    global situacion_extensa_1, situacion_extensa_2

    dicc_imagenes["imagen"] = PhotoImage(file="freud_4_1.png")
    # imagen reutilizada
    dicc_imagenes["imagen_2"] = PhotoImage(file="freud_2_1_2.png")
    dicc_imagenes["coordenadas_imagen"] = (255, 140)
    dicc_imagenes["coordenadas_imagen_1"] = (180, 140)
    dicc_imagenes["coordenadas_imagen_2"] = (215, 180)

    dicc_textos["txt_situacion"].set(
        "Te ofrecen un poco de comida\n(1)Aceptar (?)"
        "\n(2)Rechazar (Social)")
    dicc_textos["txt_2"] = "No te da mucha confianza"
    situacion_extensa_1 = 57
    situacion_extensa_2 = 57
    evento = random.randint(0, 100)
    if evento >= 0 and evento <= 20:
        # imagen reutilizada
        dicc_imagenes["imagen_1"] = PhotoImage(file="comer_1_1.png")
        dicc_textos["txt_1"] = "Aceptas con gusto\nSientes dolor en el estomago"
        dicc_imagenes["coordenadas_imagen_1"] = (200, 170)
        dicc_ambitos["Salud_1"] = dicc_ambitos["Salud_0"] - 10
        dicc_ambitos["Social_1"] = dicc_ambitos["Social_0"]
        #codigo turtle
        dicc_tortugas["tortuga_social1"] = 0
        dicc_tortugas["tortuga_salud1"] = -2
        #codigo turtle
    elif evento >= 21 and evento <= 100:
        # imagen reutilizada
        dicc_imagenes["imagen_1"] = PhotoImage(file="tropel_1_1_1.png")
        dicc_textos["txt_1"] = "Aceptas con gusto\nTenia un buen sabor"
        dicc_ambitos["Social_1"] = dicc_ambitos["Social_0"]
        dicc_ambitos["Salud_1"] = dicc_ambitos["Salud_0"]
        #codigo turtle
        dicc_tortugas["tortuga_social1"] = 0
        dicc_tortugas["tortuga_salud1"] = 0
        #codigo turtle

    dicc_ambitos["Academico_1"] = dicc_ambitos["Academico_0"]
    dicc_ambitos["Academico_2"] = dicc_ambitos["Academico_0"]
    dicc_ambitos["Social_2"] = dicc_ambitos["Social_0"]
    dicc_ambitos["Salud_2"] = dicc_ambitos["Salud_0"]
    dicc_ambitos["Economico_1"] = dicc_ambitos["Economico_0"]
    dicc_ambitos["Economico_2"] = dicc_ambitos["Economico_0"]

    #codigo turtle
    dicc_tortugas["tortuga_academico1"] = 0
    dicc_tortugas["tortuga_academico2"] = 0
    dicc_tortugas["tortuga_social2"] = 0
    dicc_tortugas["tortuga_salud2"] = 0
    dicc_tortugas["tortuga_economico1"] = 0
    dicc_tortugas["tortuga_economico2"] = 0
    #codigo turtle
    
    v_situaciones_1(dicc_tortugas,dicc_imagenes,dicc_ambitos,dicc_estadisticas,situaciones,dicc_textos)


def situacion_freud_5(dicc_tortugas,dicc_imagenes,dicc_ambitos,dicc_estadisticas,situaciones,dicc_textos):
    """
    Cambia los valores de los diccionarios "dicc_ambitos", "dicc_textos", "dicc_imagenes", "dicc_tortugas"
    y de las variables "situacion_extensa_1" y "situacion_extensa_2".
    Invoca a la funcion "v_situaciones_1()".
    Corresponde a una situacion extensa, por lo que la situacion que sigue puede ser "situacion_freud_6" o
    una situacion aleatoria, dependiendo de la eleccion hecha por el usuario posteriormente en la funcion
    "v_situaciones_1()".

    parametros:
        dicc_tortugas: diccionario que contiene las variables del modulo turtle.
        dicc_imagenes: diccionario que contiene las coordenadas y nombres de las imagenes de la
        situacion actual.
        dicc_ambitos: diccionario que contiene las variables de cada ambito del usuario.
        dicc_estadisticas: diccionario que contiene las variables del modulo tkinter las
        cuales se proyectan en pantalla.
        situaciones: diccionario que contiene todas las posibles situaciones del juego.
        dicc_textos: diccionario que contiene los mensajes que se proyectan en pantalla.
    """
    global situacion_extensa_1, situacion_extensa_2
    # 3 imagenes reutilizadas

    dicc_imagenes["imagen"] = PhotoImage(file="freud_tiempo_1.png")
    dicc_imagenes["imagen_1"] = PhotoImage(file="tropel_1_1_1.png")
    dicc_imagenes["imagen_2"] = PhotoImage(file="bicirrun_2.png")
    dicc_imagenes["coordenadas_imagen"] = (200, 160)
    dicc_imagenes["coordenadas_imagen_1"] = (180, 140)
    dicc_imagenes["coordenadas_imagen_2"] = (200, 160)

    dicc_textos["txt_situacion"].set(
        "Sientes el frio de la noche, dudas si\nquedarate o irte a casa\n(1)Quedarte (?)"
        "\n(2)Irte a tu casa (Nada de nada...)")
    dicc_textos["txt_1"] = "Solo un momentico mas"
    dicc_textos["txt_2"] = "Pasaste un buen rato"
    situacion_extensa_1 = 58
    situacion_extensa_2 = 0

    dicc_ambitos["Academico_1"] = dicc_ambitos["Academico_0"]
    dicc_ambitos["Academico_2"] = dicc_ambitos["Academico_0"]
    dicc_ambitos["Social_1"] = dicc_ambitos["Social_0"]
    dicc_ambitos["Social_2"] = dicc_ambitos["Social_0"]
    dicc_ambitos["Salud_1"] = dicc_ambitos["Salud_0"]
    dicc_ambitos["Salud_2"] = dicc_ambitos["Salud_0"]
    dicc_ambitos["Economico_1"] = dicc_ambitos["Economico_0"]
    dicc_ambitos["Economico_2"] = dicc_ambitos["Economico_0"]

    #codigo turtle
    dicc_tortugas["tortuga_academico1"] = 0
    dicc_tortugas["tortuga_academico2"] = 0
    dicc_tortugas["tortuga_social1"] = 0
    dicc_tortugas["tortuga_social2"] = 0
    dicc_tortugas["tortuga_salud1"] = 0
    dicc_tortugas["tortuga_salud2"] = 0
    dicc_tortugas["tortuga_economico1"] = 0
    dicc_tortugas["tortuga_economico2"] = 0
    #codigo turtle
    
    v_situaciones_1(dicc_tortugas,dicc_imagenes,dicc_ambitos,dicc_estadisticas,situaciones,dicc_textos)


def situacion_freud_6(dicc_tortugas,dicc_imagenes,dicc_ambitos,dicc_estadisticas,situaciones,dicc_textos):
    """
    Cambia los valores de los diccionarios "dicc_ambitos", "dicc_textos", "dicc_imagenes", "dicc_tortugas"
    y de las variables "situacion_extensa_1" y "situacion_extensa_2".
    Invoca a la funcion "v_situaciones_1()".
    Corresponde a una situacion extensa, por lo que la situacion que sigue es "situacion_freud_7".

    parametros:
        dicc_tortugas: diccionario que contiene las variables del modulo turtle.
        dicc_imagenes: diccionario que contiene las coordenadas y nombres de las imagenes de la
        situacion actual.
        dicc_ambitos: diccionario que contiene las variables de cada ambito del usuario.
        dicc_estadisticas: diccionario que contiene las variables del modulo tkinter las
        cuales se proyectan en pantalla.
        situaciones: diccionario que contiene todas las posibles situaciones del juego.
        dicc_textos: diccionario que contiene los mensajes que se proyectan en pantalla.
    """
    global situacion_extensa_1, situacion_extensa_2

    dicc_imagenes["imagen"] = PhotoImage(file="freud_6_0.png")
    # imagen reutilizada
    dicc_imagenes["imagen_2"] = PhotoImage(file="freud_2_1_2.png")
    dicc_imagenes["coordenadas_imagen"] = (180, 180)
    dicc_imagenes["coordenadas_imagen_1"] = (180, 130)
    dicc_imagenes["coordenadas_imagen_2"] = (215, 180)

    dicc_textos["txt_situacion"].set(
        "Me quedare un rato más\n...\nalguien te ofrecen fumar\n(1)Aceptar (?)"
        "\n(2)Rechazar (Nada de nada...)")
    dicc_textos["txt_2"] = "No te da mucha confianza..."
    evento = random.randint(0, 100)
    if evento >= 0 and evento <= 10:
        dicc_imagenes["imagen_1"] = PhotoImage(file="freud_6_1.png")
        dicc_textos["txt_1"] = "Aceptas\nEra una porro... toses bastante"
        dicc_ambitos["Salud_1"] = dicc_ambitos["Salud_0"] - 15
        #codigo de turtle
        dicc_tortugas["tortuga_salud1"] = -3
        #codigo de turtle
    elif evento >= 11 and evento <= 100:
        dicc_imagenes["imagen_1"] = PhotoImage(file="freud_6_1.png")
        dicc_textos["txt_1"] = "Aceptas\npfff... nunca habia probado cigarrillo"
        dicc_ambitos["Salud_1"] = dicc_ambitos["Salud_0"] - 5
        #codigo de turtle
        dicc_tortugas["tortuga_salud1"] = -1
        #codigo de turlte
    situacion_extensa_1 = 59
    situacion_extensa_2 = 59

    dicc_ambitos["Academico_1"] = dicc_ambitos["Academico_0"]
    dicc_ambitos["Academico_2"] = dicc_ambitos["Academico_0"]
    dicc_ambitos["Social_1"] = dicc_ambitos["Social_0"]
    dicc_ambitos["Social_2"] = dicc_ambitos["Social_0"]
    dicc_ambitos["Salud_2"] = dicc_ambitos["Salud_0"]
    dicc_ambitos["Economico_1"] = dicc_ambitos["Economico_0"]
    dicc_ambitos["Economico_2"] = dicc_ambitos["Economico_0"]

    #codigo turtle
    dicc_tortugas["tortuga_academico1"] = 0
    dicc_tortugas["tortuga_academico2"] = 0
    dicc_tortugas["tortuga_social1"] = 0
    dicc_tortugas["tortuga_social2"] = 0
    dicc_tortugas["tortuga_salud2"] = 0
    dicc_tortugas["tortuga_economico1"] = 0
    dicc_tortugas["tortuga_economico2"] = 0
    #codigo turtle

    v_situaciones_1(dicc_tortugas,dicc_imagenes,dicc_ambitos,dicc_estadisticas,situaciones,dicc_textos)


def situacion_freud_7(dicc_tortugas,dicc_imagenes,dicc_ambitos,dicc_estadisticas,situaciones,dicc_textos):
    """
    Cambia los valores de los diccionarios "dicc_ambitos", "dicc_textos", "dicc_imagenes", "dicc_tortugas"
    y de las variables "situacion_extensa_1" y "situacion_extensa_2".
    Invoca a la funcion "v_situaciones_1()".
    Corresponde a una situacion extensa, por lo que la situacion que sigue puede ser "situacion_freud_8" o
    una situacion aleatoria, dependiendo de la eleccion hecha por el usuario posteriormente en la funcion
    "v_situaciones_1()".

    parametros:
        dicc_tortugas: diccionario que contiene las variables del modulo turtle.
        dicc_imagenes: diccionario que contiene las coordenadas y nombres de las imagenes de la
        situacion actual.
        dicc_ambitos: diccionario que contiene las variables de cada ambito del usuario.
        dicc_estadisticas: diccionario que contiene las variables del modulo tkinter las
        cuales se proyectan en pantalla.
        situaciones: diccionario que contiene todas las posibles situaciones del juego.
        dicc_textos: diccionario que contiene los mensajes que se proyectan en pantalla.
    """
    global situacion_extensa_1, situacion_extensa_2
    # 3 imagenes reutilizadas

    dicc_imagenes["imagen"] = PhotoImage(file="freud_tiempo_1.png")
    dicc_imagenes["imagen_1"] = PhotoImage(file="tropel_1_1_1.png")
    dicc_imagenes["imagen_2"] = PhotoImage(file="bicirrun_2.png")
    dicc_imagenes["coordenadas_imagen"] = (200, 160)
    dicc_imagenes["coordenadas_imagen_1"] = (180, 140)
    dicc_imagenes["coordenadas_imagen_2"] = (200, 160)

    dicc_textos["txt_situacion"].set(
        "Ya han pasado bastantes horas,\n¿te iras a tu casa?\n(1)Quedarte (?)"
        "\n(2)Irte a tu casa (Nada de nada...)")
    dicc_textos["txt_1"] = "¡La noche es joven!"
    dicc_textos["txt_2"] = "Pasaste un buen rato"
    situacion_extensa_1 = 60
    situacion_extensa_2 = 0

    dicc_ambitos["Academico_1"] = dicc_ambitos["Academico_0"]
    dicc_ambitos["Academico_2"] = dicc_ambitos["Academico_0"]
    dicc_ambitos["Social_1"] = dicc_ambitos["Social_0"]
    dicc_ambitos["Social_2"] = dicc_ambitos["Social_0"]
    dicc_ambitos["Salud_1"] = dicc_ambitos["Salud_0"]
    dicc_ambitos["Salud_2"] = dicc_ambitos["Salud_0"]
    dicc_ambitos["Economico_1"] = dicc_ambitos["Economico_0"]
    dicc_ambitos["Economico_2"] = dicc_ambitos["Economico_0"]

    #codigo turtle
    dicc_tortugas["tortuga_academico1"] = 0
    dicc_tortugas["tortuga_academico2"] = 0
    dicc_tortugas["tortuga_social1"] = 0
    dicc_tortugas["tortuga_social2"] = 0
    dicc_tortugas["tortuga_salud1"] = 0
    dicc_tortugas["tortuga_salud2"] = 0
    dicc_tortugas["tortuga_economico1"] = 0
    dicc_tortugas["tortuga_economico2"] = 0
    #codigo turtle

    v_situaciones_1(dicc_tortugas,dicc_imagenes,dicc_ambitos,dicc_estadisticas,situaciones,dicc_textos)


def situacion_freud_8(dicc_tortugas,dicc_imagenes,dicc_ambitos,dicc_estadisticas,situaciones,dicc_textos):
    """
    Cambia los valores de los diccionarios "dicc_ambitos", "dicc_textos", "dicc_imagenes", "dicc_tortugas"
    y de las variables "situacion_extensa_1" y "situacion_extensa_2".
    Invoca a la funcion "v_situaciones_1()".
    Corresponde a una situacion extensa, por lo que la situacion que sigue puede ser "situacion_freud_9" o
    una situacion aleatoria, dependiendo de la eleccion hecha por el usuario posteriormente en la funcion
    "v_situaciones_1()".

    parametros:
        dicc_tortugas: diccionario que contiene las variables del modulo turtle.
        dicc_imagenes: diccionario que contiene las coordenadas y nombres de las imagenes de la
        situacion actual.
        dicc_ambitos: diccionario que contiene las variables de cada ambito del usuario.
        dicc_estadisticas: diccionario que contiene las variables del modulo tkinter las
        cuales se proyectan en pantalla.
        situaciones: diccionario que contiene todas las posibles situaciones del juego.
        dicc_textos: diccionario que contiene los mensajes que se proyectan en pantalla.
    """
    global situacion_extensa_1, situacion_extensa_2
    dicc_imagenes["imagen"] = PhotoImage(file="freud_8.png")
    dicc_imagenes["imagen_1"] = PhotoImage(file="freud_8_1.png")
    # imagen reutilizada
    dicc_imagenes["imagen_2"] = PhotoImage(file="freud_2_1_2.png")
    dicc_imagenes["coordenadas_imagen"] = (200, 160)
    dicc_imagenes["coordenadas_imagen_1"] = (155, 140)
    dicc_imagenes["coordenadas_imagen_2"] = (215, 180)
    
    dicc_textos["txt_situacion"].set("Te invitan a jugar volleyball\n(1)Jugar (Saud-Social)"
                      "\n(2)Rechazar la invitacion (Social)")
    dicc_textos["txt_1"] = "Jugare un rato"
    dicc_textos["txt_2"] = "Que pereza..."
    situacion_extensa_1 = 61
    situacion_extensa_2 = 61

    dicc_ambitos["Academico_1"] = dicc_ambitos["Academico_0"]
    dicc_ambitos["Academico_2"] = dicc_ambitos["Academico_0"]
    dicc_ambitos["Social_1"] = dicc_ambitos["Social_0"] + 5
    dicc_ambitos["Social_2"] = dicc_ambitos["Social_0"] - 15
    dicc_ambitos["Salud_1"] = dicc_ambitos["Salud_0"] + 10
    dicc_ambitos["Salud_2"] = dicc_ambitos["Salud_0"]
    dicc_ambitos["Economico_1"] = dicc_ambitos["Economico_0"]
    dicc_ambitos["Economico_2"] = dicc_ambitos["Economico_0"]

    #codigo turtle
    dicc_tortugas["tortuga_academico1"] = 0
    dicc_tortugas["tortuga_academico2"] = 0
    dicc_tortugas["tortuga_social1"] = 1
    dicc_tortugas["tortuga_social2"] = -3
    dicc_tortugas["tortuga_salud1"] = 2
    dicc_tortugas["tortuga_salud2"] = 0
    dicc_tortugas["tortuga_economico1"] = 0
    dicc_tortugas["tortuga_economico2"] = 0
    #codigo turtle
 
    v_situaciones_1(dicc_tortugas,dicc_imagenes,dicc_ambitos,dicc_estadisticas,situaciones,dicc_textos)


def situacion_freud_9(dicc_tortugas,dicc_imagenes,dicc_ambitos,dicc_estadisticas,situaciones,dicc_textos):
    """
    Cambia los valores de los diccionarios "dicc_ambitos", "dicc_textos", "dicc_imagenes", "dicc_tortugas"
    y de las variables "situacion_extensa_1" y "situacion_extensa_2".
    Invoca a la funcion "v_situaciones_1()".
    Corresponde al final de una situacion extensa, por lo que la situacion que sigue a esta es aleatoria.

    parametros:
        dicc_tortugas: diccionario que contiene las variables del modulo turtle.
        dicc_imagenes: diccionario que contiene las coordenadas y nombres de las imagenes de la
        situacion actual.
        dicc_ambitos: diccionario que contiene las variables de cada ambito del usuario.
        dicc_estadisticas: diccionario que contiene las variables del modulo tkinter las
        cuales se proyectan en pantalla.
        situaciones: diccionario que contiene todas las posibles situaciones del juego.
        dicc_textos: diccionario que contiene los mensajes que se proyectan en pantalla.
    """
    global situacion_extensa_1, situacion_extensa_2

    dicc_imagenes["imagen"] = PhotoImage(file="freud_9.png")
    dicc_imagenes["imagen_1"] = PhotoImage(file="freud_9_1.png")
    # imagen reutilizada
    dicc_imagenes["imagen_2"] = PhotoImage(file="bicirrun_2.png")
    dicc_imagenes["coordenadas_imagen"] = (215, 170)
    dicc_imagenes["coordenadas_imagen_1"] = (190, 180)
    dicc_imagenes["coordenadas_imagen_2"] = (200, 160)

    dicc_textos["txt_situacion"].set(
        "Hace bastante frio, y no sabes\n¿Irte a tu casa?\n(1)Quedarte (???)"
        "\n(2)Irte a tu casa (Nada de nada)")
    dicc_textos["txt_1"] = "¡Se te hizo muy tarde!\nvas tan rapido como puedes a tu casa\npero en el camino te robaron...\nesta haciendo bastante frio, y no llevaste\nchaqueta" \
            " porque creiste que\nvolverias temprano"
    dicc_textos["txt_2"] = "Pasaste un buen rato"
    situacion_extensa_1 = 0
    situacion_extensa_2 = 0

    dicc_ambitos["Academico_1"] = dicc_ambitos["Academico_0"]
    dicc_ambitos["Academico_2"] = dicc_ambitos["Academico_0"]
    dicc_ambitos["Social_1"] = dicc_ambitos["Social_0"]
    dicc_ambitos["Social_2"] = dicc_ambitos["Social_0"]
    dicc_ambitos["Salud_1"] = dicc_ambitos["Salud_0"] - 15
    dicc_ambitos["Salud_2"] = dicc_ambitos["Salud_0"]
    dicc_ambitos["Economico_1"] = dicc_ambitos["Economico_0"] - 15
    dicc_ambitos["Economico_2"] = dicc_ambitos["Economico_0"]

    #codigo turtle
    dicc_tortugas["tortuga_academico1"] = 0
    dicc_tortugas["tortuga_academico2"] = 0
    dicc_tortugas["tortuga_social1"] = 0
    dicc_tortugas["tortuga_social2"] = 0
    dicc_tortugas["tortuga_salud1"] = -3
    dicc_tortugas["tortuga_salud2"] = 0
    dicc_tortugas["tortuga_economico1"] = -3
    dicc_tortugas["tortuga_economico2"] = 0
    #codigo turtle

    v_situaciones_1(dicc_tortugas,dicc_imagenes,dicc_ambitos,dicc_estadisticas,situaciones,dicc_textos)


def game_over_total(dicc_imagenes , dicc_ambitos,dicc_estadisticas,dicc_textos):
    """
    Comprueba la razón por la cual el jugador ha perdido, verificando el valor de todas las
    estadisticas; asigna nuevos valores a los diccionarios "dicc_imagenes", "dicc_ambitos" y
    "dicc_textos", Invoca a la funcion "pantalla_game_over()".
      
    parametros:
        dicc_imagenes: diccionario que contiene las coordenadas y nombres de las imagenes de la
        situacion actual.
        dicc_ambitos: diccionario que contiene las variables de cada ambito del usuario.
        dicc_estadisticas: diccionario que contiene las variables del modulo tkinter las
        cuales se proyectan en pantalla.
        dicc_textos: diccionario que contiene los mensajes que se proyectan en pantalla.
    """
    if dicc_ambitos["Academico_0"] < 1:
        dicc_textos["txt_situacion"].set("Perdiste la calidad de estudiante, \ntu papa quedo por debajo de 3.0")
        dicc_imagenes["imagen"] = PhotoImage(file="game_over_academico_negativo.png")
        dicc_imagenes["coordenadas_imagen"] = (215, 140)
    elif dicc_ambitos["Academico_0"] > 99:
        dicc_textos["txt_situacion"].set("Te convertiste en un raton de biblioteca")
        dicc_imagenes["imagen"] = PhotoImage(file="game_over_academico_positivo.png")
        dicc_imagenes["coordenadas_imagen"] = (215, 140)
    elif dicc_ambitos["Salud_0"] < 1:
        dicc_textos["txt_situacion"].set("Te enfermas, eres hospitalizado y \nno regresas. F")
        dicc_imagenes["imagen"] = PhotoImage(file="game_over_salud_negativo.png")
        dicc_imagenes["coordenadas_imagen"] = (215, 140)
    elif dicc_ambitos["Salud_0"] > 99:
        dicc_textos["txt_situacion"].set("Estas sano pero dejaste de \nlado lo demás")
        dicc_imagenes["imagen"] = PhotoImage(file="game_over_academico_positivo.png")
        dicc_imagenes["coordenadas_imagen"] = (215, 140)
    elif dicc_ambitos["Social_0"] < 1:
        dicc_textos["txt_situacion"].set("Te quedaste solo")
        dicc_imagenes["imagen"] = PhotoImage(file="game_over_social_negativo.png")
        dicc_imagenes["coordenadas_imagen"] = (215, 140)
    elif dicc_ambitos["Social_0"] > 99:
        dicc_textos["txt_situacion"].set("Te volviste muy social y dejaste \nlo demas abandonado")
        dicc_imagenes["imagen"] = PhotoImage(file="game_over_social_positivo.png")
        dicc_imagenes["coordenadas_imagen"] = (215, 140)
    elif dicc_ambitos["Economico_0"] < 1:
        dicc_textos["txt_situacion"].set("Te quedaste sin dinero para ir a \nla U")
        dicc_imagenes["imagen"] = PhotoImage(file="game_over_economico_negativo.png")
        dicc_imagenes["coordenadas_imagen"] = (215, 140)
    elif dicc_ambitos["Economico_0"] > 99:
        dicc_textos["txt_situacion"].set("Ahorraste sin tener en cuenta tu \nvida")
        dicc_imagenes["imagen"] = PhotoImage(file="game_over_economico_positivo.png")
        dicc_imagenes["coordenadas_imagen"] = (215, 140)
    elif dicc_ambitos["semana_0"] == 16:
        dicc_textos["txt_situacion"].set("Felicidades! \nHas terminado tu semestre")
        dicc_imagenes["imagen"] = PhotoImage(file="game_over_semana.png")
        dicc_imagenes["coordenadas_imagen"] = (215, 140)
    pantalla_game_over(dicc_imagenes,dicc_estadisticas,dicc_textos)


def menu(screen,dicc_imagenes,dicc_estadisticas,situaciones):
    """
    Despliega textos para que el usuario escoja 3 posibles opciones e invoque a la funcion
    correspondiente, jugar en el modo estandar "tutorial_estandar()", jugar en el modo
    personalizado "tutorial_per()" o ver el puntaje maximo actual "v_puntajes()".

    parametros:
        screen: pantalla del modulo tkinter.
        dicc_imagenes: diccionario que contiene las coordenadas y nombres de las imagenes de la
        situacion actual.
        dicc_estadisticas: diccionario que contiene las variables del modulo tkinter las
        cuales se proyectan en pantalla.
        situaciones: diccionario que contiene todas las posibles situaciones del juego.
    """
    trampa = False
    espacio = Frame(screen, width=600, height=400)
    espacio.config(bg="black")
    espacio.place(x = 0, y = 0)

    Label(espacio, text="Sobreviviendo en la UN", bg="black", fg="gold", font=("Courier New", 18)).place(x="150",
                                                                                                         y="50")
    Label(espacio, text="Escoge tu modo de juego", bg="black", fg="gold", font=("Courier New", 12)).place(x="200",
                                                                                                          y="100")
    
    j_estandar = Button(espacio, text="Juego estandar", font=("Courier New", 10), fg="gold", bg="gray22", width=20,
                        command= lambda : tutorial_est(dicc_imagenes,dicc_estadisticas,situaciones,trampa))
    j_estandar.place(x=230, y=140)

    j_perso = Button(espacio, text="Juego personalizado", font=("Courier New", 10), fg="gold", bg="gray22",width=20,
                 command= lambda : tutorial_per(dicc_imagenes,dicc_estadisticas,situaciones,trampa))
    j_perso.place(x=230, y=175)

    puntajes = Button(espacio, text="Puntajes", font=("Courier New", 10), fg="gold", bg="gray22", width=20, command=v_puntajes)
    puntajes.place(x= 230, y =210)

    salida = Button(espacio, text="Salir", font=("Courier New", 10), fg="gold", bg="gray22",width= 20,command=exit)
    salida.place(x= 230, y =245)

    Label(espacio, text="V. 21.05.20", bg="black", fg="gold", font=("Courier New", 10)).place(x="100", y="290")
    Label(espacio, text="Created by:", bg="black", fg="gold", font=("Courier New", 10)).place(x="100", y="310")
    Label(espacio, text="Allison Castellanos  Camilo Chacon  Diego Cortes", bg="black", fg="gold",
          font=("Courier New", 10)).place(x="100", y="330")
    Label(espacio, text="Programacion de computadores 2020-1 UNAL", bg="black", fg="gold",
          font=("Courier New", 10)).place(x="100", y="350")

def iniciar_tortugas():
    """
    Inicializa todas las variables del modulo turtle y las guarda en un diccionario

    Inicializa las tortugas que representaran los valores de las estadisticas del usuario,
    junto con sus caracteristicas, tales como su color, su grosor, su velocidad y su
    posicion.

    retorno:
        dicc_tortugas: diccionario que contiene todas las variables que el juego
        requiere del modulo turtle
    """
    dicc_tortugas = {}
    canvass = Canvas(master = screen_situaciones, width = 470 , height = 60)
    pantalla_turtle = turtle.TurtleScreen(canvass)
    pantalla_turtle.bgcolor("black")
    canvass.place( x = 80 , y = 0)
    

    velocidad = 10000000
    grosor = 5

    dicc_tortugas["color_Academico"] = "DeepSkyBlue"
    dicc_tortugas["AcademicoT"] = turtle.RawTurtle(pantalla_turtle)
    dicc_tortugas["AcademicoT"].hideturtle()
    dicc_tortugas["AcademicoT"].pensize(grosor)
    dicc_tortugas["AcademicoT"].speed(velocidad)
    head =dicc_tortugas["AcademicoT"].heading()

    dicc_tortugas["color_Economico"] = "red"
    dicc_tortugas["EconomicoT"] = turtle.RawTurtle(pantalla_turtle)
    dicc_tortugas["EconomicoT"].hideturtle()
    dicc_tortugas["EconomicoT"].pensize(grosor)
    dicc_tortugas["EconomicoT"].speed(velocidad)

    dicc_tortugas["color_Salud"] = "yellow"
    dicc_tortugas["SaludT"] = turtle.RawTurtle(pantalla_turtle)
    dicc_tortugas["SaludT"].hideturtle()
    dicc_tortugas["SaludT"].pensize(grosor)
    dicc_tortugas["SaludT"].speed(velocidad)

    dicc_tortugas["color_Social"] = "green"
    dicc_tortugas["SocialT"] = turtle.RawTurtle(pantalla_turtle)
    dicc_tortugas["SocialT"].hideturtle()
    dicc_tortugas["SocialT"].pensize(grosor)
    dicc_tortugas["SocialT"].speed(velocidad)

    dicc_tortugas["AcademicoT"].up()
    dicc_tortugas["AcademicoT"].goto(-215,24)
    dicc_tortugas["AcademicoT"].right(head)
    dicc_tortugas["EconomicoT"].up()
    dicc_tortugas["EconomicoT"].goto(-215,-21)
    dicc_tortugas["EconomicoT"].right(head)
    dicc_tortugas["SocialT"].up()
    dicc_tortugas["SocialT"].goto(-215,-6)
    dicc_tortugas["SocialT"].right(head)
    dicc_tortugas["SaludT"].up()
    dicc_tortugas["SaludT"].goto(-215,9)
    dicc_tortugas["SaludT"].right(head)


    dicc_tortugas["AcademicoT"].down()
    dicc_tortugas["EconomicoT"].down()
    dicc_tortugas["SaludT"].down()
    dicc_tortugas["SocialT"].down()
    return dicc_tortugas

def logo_bienvenida():
    """
    Dibuja un logo representativo del programa mediante los modulos
    turtle y tkinter, invoca a las funciones "pintar_S()", "pintar_U()"
    y "pintar_N()".
    """
    canvvas = Canvas(master = screen_inicio,width =  600, height = 400)
    ventana = turtle.TurtleScreen(canvvas)
    ventana.bgcolor("black")
    canvvas.pack()
    Label(canvvas, text="CARGANDO", font=("Courier New", 15), bg="black", fg="DeepSkyBlue").place(x = 240 , y = 310)
    Label(canvvas, text="Sobreviviendo en la UN", font=("Courier New", 20), bg="black", fg="yellow").place(x = 120 , y = 20)
    grosor = 1
    hola = turtle.RawTurtle(ventana)
    hola.hideturtle()
    hola.speed(0)
    hola.pensize(grosor)
    head = hola.heading()
    cargando = turtle.RawTurtle(ventana)
    cargando.hideturtle()
    cargando .pensize(10)
    cargando.penup()
    cargando.goto(-240,-90)
    cargando.right(head)
    cargando.pendown()
    cargando.color("white")
    hola.penup()
    hola.goto(-120,50)
    hola.right(head)
    hola.left(90)
    hola.pendown()
    z = 0
    pintar_S(hola,cargando,1,z)
    grosor = 5
    hola.hideturtle()
    hola.penup()
    hola.goto(-40,77)
    hola.right(head)
    hola.right(180)
    hola.pendown()
    hola.color("blue")
    z = 0
    pintar_U(hola,cargando,z,grosor)
    hola.penup()
    hola.goto(90,-40)
    grosor = 5
    hola.right(head)
    hola.pendown()
    hola.color("purple")
    z = 0
    pintar_N(hola,cargando,z,grosor)
    
def pintar_S(hola,cargando,grosor,z):
    """
    Dibuja de forma recursiva una letra S la cual varia de grosor en sus extremos,
    y cambia su cuando ya se ha dibujado la mitad de la letra.

    parametros:
        hola: objeto de clase tortuga del modulo turtle
        cargando: objeto de clase tortuga del modulo turtle
        grosor: entero que determina el grosor con el que la letra sera dibujada
        z: entero que determina la forma que se debe tomar para dibujar la letra
    """
    if z == 540:
        pass
    elif z <= 270:
        hola.color("yellow")
        hola.pensize(grosor)
        if z % 2 == 0:
            grosor += 0.1
            hola.pensize(grosor)
        hola.forward(0.6)
        hola.left(1)
        cargando.forward(0.5)
        pintar_S(hola,cargando,grosor,z+1)
        
    else:
        hola.color("red")
        hola.pensize(grosor)
        if z % 2 == 0:
            grosor -= 0.1
        hola.forward(0.6)
        hola.right(1)
        cargando.forward(0.5)
        pintar_S(hola,cargando,grosor,z+1)

def pintar_U(hola,cargando,z,grosor):
    """
    Dibuja de forma recursiva una letra U la cual varia de grosor en sus extremos,
    y cambia su cuando ya se ha dibujado la mitad de la letra.

    parametros:
        hola: objeto de clase tortuga del modulo turtle
        cargando: objeto de clase tortuga del modulo turtle
        grosor: entero que determina el grosor con el que la letra sera dibujada
        z: entero que determina la forma que se debe tomar para dibujar la letra
    """
    if z == 240:
        pass
    elif z <= 30:
        hola.pensize(grosor)
        if z % 2 == 0:
            grosor += 0.8
        hola.forward(2.9)
        pintar_U(hola,cargando,z+1,grosor)
        
    elif z > 30 and z <= 210:
        if z == 120:
            hola.color("green")
        hola.forward(0.5)
        hola.left(1)
        cargando.forward(0.5)
        pintar_U(hola,cargando,z+1,grosor)
    else:
        hola.pensize(grosor)
        if z % 2 == 0:
            grosor -= 0.8
        hola.forward(2.9)
        pintar_U(hola,cargando,z+1,grosor)
        

def pintar_N(hola,cargando,z,grosor):
    """
    Dibuja de forma recursiva una letra N la cual varia de grosor en sus extremos,
    y cambia su cuando ya se ha dibujado la mitad de la letra.

    parametros:
        hola: objeto de clase tortuga del modulo turtle
        cargando: objeto de clase tortuga del modulo turtle
        grosor: entero que determina el grosor con el que la letra sera dibujada
        z: entero que determina la forma que se debe tomar para dibujar la letra
    """
    if z == 180:
        pass
    elif z <= 40:
        if z % 2 == 0:
            grosor += 0.7
        hola.pensize(grosor)
        hola.forward(2.8)
        cargando.forward(0.5)
        pintar_N(hola,cargando,z+1,grosor)
            
    elif z > 40 and z <= 140:
        if z == 41:
            hola.right(145)
        elif z == 90:
            hola.color("orange")
        hola.forward(1.3)
        cargando.forward(0.5)
        pintar_N(hola,cargando,z+1,grosor)

    else:
        if z == 141:
            hola.left(145)
        if z % 2 == 0:
            grosor -= 0.7
        hola.pensize(grosor)
        hola.forward(2.8)
        cargando.forward(0.5)
        pintar_N(hola,cargando,z+1,grosor)


def avanzar(tortuga,valor,color_tortuga):
    """
    La tortuga avanzara serpenteando varias veces dependiendo del valor del parametro
    "valor" para aumentar el area de la barra que representa el valor de la
    estadisticas del usuario.

    parametros:
        tortuga:
        valor:
        color_tortuga:
    """
    tortuga.color(color_tortuga)
    tortuga.right(180)
    tortuga.forward(4)
    tortuga.right(90)
    for a in range(valor):
        for b in range(4):
            tortuga.right(90)
            tortuga.forward(4)
            tortuga.left(90)
            tortuga.forward(2.5)
            tortuga.left(90)
            tortuga.forward(4)
            tortuga.right(90)
            tortuga.forward(2.5)
    tortuga.right(90)
    tortuga.forward(4)

    
def avanzar1(tortuga,valor,color_tortuga):
    """
    Dibuja las barras horizontales que representan el valor de las
    estadisticas iniciales del usuario

    parametros:
        tortuga:
        valor:
    """
    tortuga.color(color_tortuga)
    for a in range(valor):
        for b in range(4):
            tortuga.right(90)
            tortuga.forward(4)
            tortuga.left(90)
            tortuga.forward(2.5)
            tortuga.left(90)
            tortuga.forward(4)
            tortuga.right(90)
            tortuga.forward(2.5)
    tortuga.right(90)
    tortuga.forward(4)

def retroceder(tortuga,valor):
    """
    La tortuga retrocedera serpenteando varias veces dependiendo del valor del parametro
    "valor" para disminuir el area de la barra que representa el valor de las estadisticas
    del usuario.

    parametros:
        tortuga:
        valor:
    """
    tortuga.right(90)
    tortuga.color("black")
    for c in range(valor):
        for d in range(4):
            tortuga.right(90)
            tortuga.forward(4)
            tortuga.left(90)
            tortuga.forward(2.5)
            tortuga.left(90)
            tortuga.forward(4)
            tortuga.right(90)
            tortuga.forward(2.5)
    tortuga.right(90)
    tortuga.forward(4)
    tortuga.right(180)
    tortuga.forward(4)

def password():
    """
    Obtiene el valor de la variable "name" del modulo tkinter,
    guarda este valor en la varibale "mensaje", y retira los caracteres
    "," y "." de dicho valor. Invoca a la funcion "peso()"
    """
    mensaje = name.get().split()
    semilla = 7
    lim = 2
    cont = 0

    for i in mensaje:
        nueva = ""
        if "," in i or "." in i:
            for letras in i:
                if letras != "," and letras != ".":
                    nueva += letras
            mensaje.remove(i)
            mensaje.insert(cont, nueva)
        cont += 1
    return peso(mensaje)

def peso(lista):
    """
    Retorna el valor del residuo de la division entre la suma
    del resultado anterior y el peso de la palabra y la semilla.
    """
    cont = 0
    checksum = 0
    lista_pesos = []
    lista_check = []
    for i in lista:
        peso_act = peso_mot(i)
        lista_pesos.append(peso_act)
        if cont == 0:
            checksum = peso_mot(lista[cont])*7
            lista_check.append(checksum)
        else:
            checksum = (lista_check[cont - 1]+ peso_act)*7
            if checksum > 2:
                checksum = checksum % 2
            lista_check.append(checksum)

        cont += 1
    indice = lista_pesos.index(max(lista_pesos))
    return checksum

def peso_mot(palabra):
    """
    Calcula el peso de cada palabra, y retorna la suma de los residuos
    entre el resultado de la multiplicacion de cada letra "su representacion
    en ASCII con la posicion" en la palabra empezando en 1 y la semilla, la cual
    tiene un valor entero de 7.
    """
    peso = 0
    cont = 1
    for parte in palabra:
        peso += (ord(parte) * cont) % 7
        cont += 1
    return peso

def main():
    """
    Inicializa el diccionario "situaciones", la pantalla del modulo tkinter "screen_inicio", el diccionario
    "dicc_imagenes", el diccionario "dicc_estadisticas", las variables de tipo entero del modulo tkinter
    "Academico", "Salud", "Social", "Economico", y la variable de tipo cadena "txt_situacion".
    Invoca a la funcion menu().
    """
    global txt_situacion, situacion_a_usar
    situaciones = {0: textos_situacion_tutor, 1: textos_situacion_tutor2, 2: textos_situacion_tutor3,
                   3: situacion_jugar,
                   4: situacion_bicirrun, 5: situacion_amigos, 6: situacion_prestamo, 7: situacion_danza,
                   8: situacion_tropel,
                   9: situacion_comer, 10: situacion_parcial, 11: situacion_copia, 12: situacion_parcial_biblioteca,
                   13: situacion_freud,
                   50: situacion_tropel_1, 51: situacion_comer_1, 52: situacion_comer_2, 53: situacion_freud_1,
                   54: situacion_freud_2, 55: situacion_freud_3, 56: situacion_freud_4, 57: situacion_freud_5,
                   58: situacion_freud_6,
                   59: situacion_freud_7, 60: situacion_freud_8, 61: situacion_freud_9}
    situacion_a_usar = -1

    # ------ Ventana -------
    global screen_inicio, resultado
    screen_inicio = Tk()
    screen_inicio.resizable(False, False)
    screen_inicio.geometry("600x400+100+100")
    screen_inicio.title("Sobreviviendo en la UN")
    screen_inicio.config(bg="black")
    # logo_bienvenida()
    resultado = False

    dicc_imagenes = {}
    dicc_imagenes["imagen"] = PhotoImage(file="rsz_tutor.png")
    dicc_imagenes["coordenadas_imagen"] = (277, 210)
    dicc_imagenes["imagen_1"] = PhotoImage(file="rsz_tutor.png")
    dicc_imagenes["coordenadas_imagen_1"] = (277, 210)
    dicc_imagenes["imagen_2"] = PhotoImage(file="rsz_tutor.png")
    dicc_imagenes["coordenadas_imagen_2"] = (277, 210)

    Academico, Salud, Social, Economico, semana = IntVar(value=0), IntVar(value=0), IntVar(value=0), IntVar(value=0), IntVar(value=0)
    dicc_estadisticas = {"Academico" : Academico, "Salud" : Salud, "Social" : Social, "Economico" : Economico, "semana" : semana}
    txt_situacion = StringVar()



    menu(screen_inicio,dicc_imagenes,dicc_estadisticas,situaciones)
    screen_inicio.mainloop()

if __name__ == '__main__':
    main()
