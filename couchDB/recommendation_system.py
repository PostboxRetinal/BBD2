import couchdb
conn_string = "htp://admin:24C29O3095B*-@localhost:5984"
server = couchdb.Server(conn_string)
db_name = 'recommendation'
if db_name in server:
    print('Conectado con la BD')
    db = server[db_name]
else:
    print("--- Creando base de datos")
    db = server.create(db_name)

    #Funciones CRUD
    def Create(collection, data):
        doc_id, doc_rev = db.save(data)

    def Update(doc_id, data):
        doc = db[doc_id]
        doc.update(data)
        db.save(doc)

    def SelectAll(collection):
        docs = [doc for doc in db.view(f"{collection}/all")]

    def Select_By_Criteria(collection, criteria):
        docs = [doc for doc in db.view(f"{collection}/by_criteria", key=criteria)]

    def Delete(doc_id):
        doc = db[doc_id]
        db.delete(doc)

    guitarra = {
        "id":"g001",
        "nombre":"Guitarra acústica básico",
        "categoria": "Musica",
        "descripcion":"guitarra acústica básica",
        "duracion":40,
        "precio":0.0,
        "remoto":False
    }
    pintura = {
        "id":"g001",
        "nombre":"Lo pinto: básico",
        "categoria": "Musica",
        "descripcion":"guitarra acústica básica",
        "duracion":40,
        "precio":0.4,
        "remoto":False
    }

    Create("cursos", guitarra)
    Create("cursos", pintura)

    #REVISAR UPDATE
    guitarra["duracion"] = 45
    Update(guitarra)

    lista_cursos = SelectAll("cursos")