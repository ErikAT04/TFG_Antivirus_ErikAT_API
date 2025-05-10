from app.repository.Schemas import Hash

with open("app/files/virusDef.txt", "r") as file:
    with open("db.sql", "w") as database:
        database.write("INSERT INTO hash(hash, type, extended_type) VALUES (")
        for line in file.readlines():
            lista = line.split("|")
            hash:Hash = Hash(hash= lista[1], extended_type= lista[2] , type=lista[3])
            database.write(f"('{hash.hash}', '{hash.type}', '{hash.extended_type}'),\n")
        database.write(");")