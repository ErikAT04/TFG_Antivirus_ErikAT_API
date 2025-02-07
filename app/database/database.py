from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL de la BD
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://freedb_AT_Root:RR5xHVqx2J#uVN?@sql.freedb.tech:3306/freedb_PruebasAndroid"
# Motor de conexion de la bd
engine = create_engine(SQLALCHEMY_DATABASE_URL)
# Crea el generador de sesiones de la BD
sessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
# Modelos de la BD
Base = declarative_base()

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()