from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import config


engine = create_engine(f'mysql+mysqlconnector://{config.USER}:{config.PASSWORD}@{config.SERVER}:3306/{config.DB}')
Session = sessionmaker(bind=engine)

def get_session():
    session = Session()
    return session

def close_session():
    session = Session()
    session.close()
# def dbConnection():
#     try:
#         mongo_db = PyMongo(app)
#         client = mongo_db.cx
#         db = client["dbb_products_app"]
#     except ConnectionError:
#         print("Error de conexão com o banco de dados")
#     return db
#
# def connectDB():
#     db = dbConnection()
#     products = db['products']
#     return products
