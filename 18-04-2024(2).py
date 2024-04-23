Persona = []


def registrar_Persona():
   
    nombre = input("Nombre y apellidos: ")
    identificacion = input("Identificación: ")
    correo = input("Correo electrónico: ")
    contacto = input("Contacto: ")
    edad = int(input("Edad: "))
    experiencia = int(input("Años de experiencia: "))
    profesion = input("Profesión: ")
    ciudad = input("Ciudad: ")
    sexo = input("Sexo: ")

   
    if 25 <= edad <= 32 and (profesion == "Ing. sistemas" or profesion == "ing. informatico") and 2 <= experiencia <= 4:
        
        Persona = {
            "Nombre": nombre,
            "Identificación": identificacion,
            "Correo electrónico": correo,
            "Contacto": contacto,
            "Edad": edad,
            "Años de experiencia": experiencia,
            "Profesión": profesion,
            "Ciudad": ciudad,
            "Sexo": sexo
        }

       
       
        Personas.append(Persona)
        print("Persona registrado exitosamente.")
    else:
        print("La Persona no cumple con las condiciones.")

def consultar_Persona():
    for Persona in Persona:
        print(Persona)


while True:
    print("1. Registrar Persona")
    print("2. Consultar Persona")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_Persona()
    elif opcion == "2":
        consultar_Persona()
    elif opcion == "3":
        break
    else:
        print("Opción inválida. Intente nuevamente.")

   