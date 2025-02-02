from app.repository.Schemas import Signature

with open("app/files/virusDef.txt", "r") as file:
    with open("db.sql", "w") as database:
        database.write("INSERT INTO signature(signature, type, extended_type) VALUES (")
        for line in file.readlines():
            lista = line.split("|")
            sig:Signature = Signature(signature= lista[1], extended_type= lista[2] , type=lista[3])
            database.write(f"('{sig.signature}', '{sig.type}', '{sig.extended_type}'),\n")
        database.write(");")