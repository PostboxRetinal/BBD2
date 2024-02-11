#Adaptado según requerido
#Hecho por Sebastian Balanta
class Comics:
    numQueries = 0    
    def __init__(self) -> None:
        self.comics = []   

    def loadDataFromCSV(self, file):
        with open(file, 'r') as f:
            for line in f:
                line = line.strip()
                values = line.split(sep=';')             
                comic = {"artist":values[0], "title":values[1], "year":values[2]}
                self.comics.append(comic)
        
        print(self.comics)

    def filterComics(this, key, value):
        filteredList =  list(filter(lambda x: x[key] == value, this.comics))
        print(filteredList)

    def filterComics2(this, key, value):
        filteredList2 = [f for f in this.comics if f[key] == value]
        print(filteredList2)


  