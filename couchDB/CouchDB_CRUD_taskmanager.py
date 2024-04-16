import couchdb

conn_string = "http://admin:24C29O3095B*-@localhost:5984"
server = couchdb.Server(conn_string)
db_name = "taskmanager"

if db_name in server:
    print("Conectado con la BD")
    db = server[db_name]
else:
    print("--- Creando BBDD")
    db = server.create(db_name)

#   --CRUD
    #   READ
for doc_id in db:
    print(db[doc_id])
    
    #   SELECT x ID
    id_doc = input('Ingrese el ID del documento')
    doc = db[id_doc]
    print(doc)

    #   SELECT x llave y valor
        #NEW DOC
    new_developer = {
        "Id":"94472846",
        "Nombre":"Luis Umaña"
        }
    #Al crear nuevo doc recibe el _id y el rev dado por couchdb
    doc_new_dev_id, doc_new_dev_rev = db.save(new_developer)