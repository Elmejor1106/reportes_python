from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

# --- IMPORTANTE ---
# Modifica estas variables con tus credenciales de base de datos.
# Para mayor seguridad, es recomendable usar variables de entorno.
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_HOST = os.getenv("DB_HOST", "127.0.0.1")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_NAME = os.getenv("DB_NAME", "juego_rapido_db")

# Cadena de conexión para MySQL con mysql-connector-python
DATABASE_URL = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

try:
    engine = create_engine(DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    print("Conexión a la base de datos establecida exitosamente.")
except Exception as e:
    print(f"Error al conectar a la base de datos: {e}")

def get_db():
    """
    Función para obtener una sesión de base de datos.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
