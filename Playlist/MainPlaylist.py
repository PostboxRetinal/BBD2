from ejercicio1 import *
file = input("Ingrese la ruta del archivo: ")

MiPlaylist = Playlist()
MiPlaylist.loadDataFromCSV(file)
parametro = input('Artista por el que quieras filtrar: ')
MiPlaylist.filterPlaylist2('artist', parametro)