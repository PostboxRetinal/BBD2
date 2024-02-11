from MainComics import *

#pedir nombre del archivo plano:
file = input("Ingrese el nombre del archivo")

MiComic = Comics()
MiComic.loadDataFromCSV(file)
artista = input("Ingrese nombre del escritor del cómic: ")
MiComic.filterPlaylist("artist",artista)

titulo = input("Ingrese título del cómic que busca: ")
anno = input("Ingrese año de escritura: ")
MiComic.filterComics("title",titulo)

