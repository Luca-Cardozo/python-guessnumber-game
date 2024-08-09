def mostrar_menu():
    print("\nAgenda de contactos: ")
    print("1. Agregar contacto")
    print("2. Eliminar contacto existente")
    print("3. Buscar contacto")
    print("4. Lista de contactos")
    print("5. Salir del programa")
    print("\n")


def agregar_contacto(agenda):
    nombre = input("Por favor introduzca el nombre completo del contacto: ")
    telefono = input("Por favor introduzca el teléfono del contacto: ")
    email = input("Por favor introduzca el email del contacto: ")
    agenda[nombre] = {"Teléfono": telefono, "Email": email}
    print(f"Se ha agregado el contacto {nombre} exitosamente!")


def eliminar_contacto(agenda):
    nombre = input(
        "Por favor introduzca el nombre completo del contacto a eliminar: ")
    if nombre in agenda:
        del agenda[nombre]
        print(f"El contacto {nombre} ha sido eliminado exitosamente")
    else:
        print(f"No se ha encontrado el contacto con el nombre {nombre}")


def buscar_contacto(agenda):
    nombre = input(
        "Por favor introduzca el nombre completo del contacto a buscar: ")
    if nombre in agenda:
        print(f"Nombre: {nombre}")
        print(f"Teléfono: {agenda[nombre]["Teléfono"]}")
        print(f"Email: {agenda[nombre]["Email"]}")
    else:
        print(f"No se ha encontrado el contacto con el nombre {nombre}")


def listar_contacto(agenda):
    if agenda:
        print("\nLista de contactos: ")
        for nombre, info in agenda.items():
            print(f"Nombre: {nombre}")
            print(f"Teléfono: {info["Teléfono"]}")
            print(f"Email: {info["Email"]}")
            print("-" * 20)
    else:
        print(f"La agenda aún está vacía")


def agenda_contactos():
    agenda = {}

    while True:
        mostrar_menu()
        opcion = input("Por favor elija una opción: ")
        print("\n")

        if opcion == "1":
            agregar_contacto(agenda)
        elif opcion == "2":
            eliminar_contacto(agenda)
        elif opcion == "3":
            buscar_contacto(agenda)
        elif opcion == "4":
            listar_contacto(agenda)
        elif opcion == "5":
            print("Saliendo de la agenda de contactos, hasta luego!")
            break
        else:
            print("Por favor seleccione una opción válida (del 1 al 5): ")


agenda_contactos()
