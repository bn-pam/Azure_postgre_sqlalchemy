from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base 
from orm import Base

Base = declarative_base()
DATABASE_URL = 'postgresql://pbosql:rgFa%$"j99"qHx"@pb-postgresql.postgres.database.azure.com:5432/db1books?client_encoding=en_US.utf8'

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
