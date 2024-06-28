from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base 
from orm import Base
from dotenv import load_dotenv
import os

load_dotenv() # charge dotenv pour les références au fichier .ENV

Base = declarative_base()
# Définir la connexion à la base de données

# url de la BDD
DATABASE_URL = os.getenv("DATABASE_URL") 

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True, autoincrement=True)
    ISBN = Column(String, unique=True, nullable=False)
    Book_Title = Column(String, nullable=False)
    Book_Author = Column(String, nullable=False)
    Year_Of_Publication = Column(Integer, nullable=False)
    Publisher = Column(String, nullable=False)
    Image_URL_S = Column(String)
    Image_URL_M = Column(String)
    Image_URL_L = Column(String)

    def __repr__(self):
        return f"<Book(id='{self.id}', title='{self.Book_Title.encode('utf-8').decode('utf-8')}', author='{self.Book_Author.encode('utf-8').decode('utf-8')}', year='{self.Year_Of_Publication}')>"

    @classmethod
    def ajouter_livre(cls, session, ISBN, title, auteur, annee, editeur, img_url_s, img_url_m, img_url_l):
        nouveau_livre = cls(ISBN=ISBN, Book_Title=title, Book_Author=auteur, Year_Of_Publication=annee, Publisher=editeur, Image_URL_S= img_url_s, Image_URL_M= img_url_m, Image_URL_L= img_url_l)
        session.add(nouveau_livre)
        session.commit()
        print(f"Livre ajouté : {nouveau_livre}")
