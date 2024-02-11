# Bases de datos 2, 2024 - Actividad preparatoria
#una lista de tuplas como una versión de una "bd" "key/value"
class Playlist:
    numQueries = 0    
    def __init__(self) -> None:
        self.playlist = []   

    def loadDataFromCSV(self, file):
        with open(file) as f:
            for line in f:
                line = line.strip()
                values = line.split(sep=';')     
                #estructura de un registro en un "store" key/value:
                #"artist" es la llave, lo que sigue es el valor           
                record = {"artist":values[0], "song":values[1], "genre":values[2], "time":values[3]}
                self.playlist.append(record)
        
        print(self.playlist)


    def filterPlaylist(this, key, value):
        filteredList =  list(filter(lambda x: x[key] == value,this.Playlist))
        print(filteredList)

    def filterPlaylist2(this,key,value):
        filteredPlaylist = [ f for f in this.playlist if f[key] == value]
        print(filteredPlaylist)


  