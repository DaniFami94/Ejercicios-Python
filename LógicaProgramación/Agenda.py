def my_agenda():
    agenda = {}

    def insert_contact(name):
        print(f"Entrando en insert_contact con name={name}")
        phone = input("Introduce el teléfono del contacto: ")
        if phone.isdigit() and len(phone) <= 11:
            agenda[name] = phone
            print(f"Contacto {name} añadido/actualizado correctamente.")
        else:
            print("Número inválido. Intenta de nuevo.")

    def contact_exists(name):
        print(f"Verificando si {name} existe en la agenda: {agenda}")
        if name in agenda:
            return True
        print(f"El contacto {name} no existe.")
        return False

    while True:
        print("\n1. Buscar contacto")
        print("2. Insertar contacto")
        print("3. Salir")

        option = input("\nSelecciona una opción: ")
        print(f"Opción seleccionada: {option}")

        match option:
            case "1":  # Buscar contacto
                name = input("Introduce el nombre del contacto a buscar: ")
                if contact_exists(name):
                    print(f"El número de teléfono de {name} es {agenda[name]}.")
            case "2":  # Insertar contacto
                name = input("Introduce el nombre del contacto: ")
                insert_contact(name)
            case "3":  # Salir
                print("Saliendo de la agenda.")
                break
            case _:  # Opción inválida
                print("Opción no válida.")
my_agenda()
