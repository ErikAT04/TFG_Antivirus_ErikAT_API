from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DBUSER = "freedb_AT_Root"
DBPASSWORD = "RR5xHVqx2J#uVN?"

# URL de la BD
SQLALCHEMY_DATABASE_URL = f"mysql+mysqlconnector://{DBUSER}:{DBPASSWORD}@sql.freedb.tech:3306/freedb_PruebasAndroid"
# Motor de conexion Sde la bd
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