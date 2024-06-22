import os

lista_libros = []
encabezados = ['Título','Autor','Año de Publicación','SKU']
prest_enca = ['USUARIO','TITULO','FECHA DEL PRESTAMO']
titulos = []
prestados =[]

def reg_libros():
    try:
        titulo = input("Ingrese el título del libro: ")
        autor = input("Ingrese el autor del libro: ")
        año_publi = int(input("Ingrese el año de publicación del libro: "))
        sku = input("Ingrese el SKU del libro: ")

        if titulo == "" or autor == "" or año_publi == "" or sku == "":
            print("Datos ingresados no corresponden, ingreselos nuevamnete")
        
    except ValueError:
        print("El dato ingresado no correponde, intente nuevamente")

    fila = [titulo, autor, año_publi, sku]
    lista_libros.append(fila)
    titulos.append(titulo)

def prestar():
    try:
        usuario = input("Ingrese su nombre de usuario: ")
        lib_prestar = input("Ingrese el título del libro que busca: ")
        for lib_prestar in lista_libros:
            if lib_prestar == titulos:
                print("Libro encontrado")
                fech = input("Ingrese la fecha de préstamo: ")
            else:
                print("El libro buscado no se encuentra en los registros, intente nuevamente")
    except ValueError:
        print("Datos erroneos")

    usuarios = [usuario, lib_prestar, fech]
    prestados.append(usuarios)


def listar_lib():
    if lista_libros:
        for titulo in lista_libros:
            print(titulo)
    else:
        print("No hay libros registrados")


def imp_rep():
    with open("prestamos.txt", "w") as file:
        file.write("\t".join(prest_enca) + "\n")
        for titulo in prestados:
            file.write("\t".join(map(str, titulo)) + "\n")
    print("Planilla de libros prestados impresa...\n")


def menu():
    while True:
        try:
            print("\n- - - MENU - - -\n")
            print("1. Registrar libro\n2. Prestar libro\n3. Listar todos los libros\n4. Imprimir reporte de préstamos\n5. Salir del Programa\n")
            op = int(input("Ingrese la opción que desea: "))
            if op == 1:
                reg_libros()
            elif op == 2:
                prestar()
            elif op == 3:
                listar_lib()
            elif op == 4:
                imp_rep()
            elif op == 5:
                print("Programa finalizado...\nDesarrollado por Francisco Olivares\nRUT: 19.222.372-5")
                break
            else:
                print("La opción ingresada no corresponde, ingrese nuevamente")
        except ValueError:
            print("Error en el tipo de dato ingresado, intente nuevamente")
