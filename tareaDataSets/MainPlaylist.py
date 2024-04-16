from MainComics import *

#Input de archivo
file = input("Ingrese la ruta del archivo: ")
opc = int(input('Ingrese la opción de filtro deseada:\n1. Filtrar por artista\n2. Filtrar por título y año\n'))
MiComic = Comics()
MiComic.loadDataFromCSV(file)

if (opc == 1):
    artista = input("Ingrese nombre del escritor del cómic: ")
    MiComic.filterPlaylist("artist", artista)

elif (opc == 2):
    MiComic = Comics()
    MiComic.loadDataFromCSV(file)
    titulo = input("Ingrese título del cómic que busca: ")
    anno = input("Ingrese año de escritura: ")
    MiComic.filterComicsListComprehension("titulo", titulo)
    MiComic.filterComics("title", titulo)

else:
    print("Ingresa una opción válida!")