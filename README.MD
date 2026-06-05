# BBD2 - Database II projects

Short collection of exercises and scripts for the "Bases de Datos 2" course.

## Contents
- `couchDB/`: CouchDB examples and CRUD scripts
- `Playlist/`: Playlist exercises and data
- `proyectoCouchDB/`: CouchDB project workspace
- `tareaDataSets/`: Dataset exercises (comics, playlists)

## Quick start
1. Python 3.8+
2. (optional) Create venv and activate:

```bash
python3 -m venv .venv
source .venv/bin/activate
```
3. Install common deps if needed:

```bash
pip install pandas requests couchdb
```

## Run
Run a script:

```bash
python3 path/to/script.py
```

For CouchDB examples: ensure server at http://127.0.0.1:5984 and update credentials in the script.

## Examples
- `couchDB/CouchDB_CRUD_taskmanager.py`: CRUD with CouchDB
- `Playlist/MainPlaylist.py`: reads `data.csv`
