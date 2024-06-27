from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base 
import csv
from dotenv import load_dotenv
import os

load_dotenv()

# D�finir la connexion � la base de donn�es

# url de la BDD
DATABASE_URL = os.getenv("DATABASE_URL") 

Base = declarative_base()

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
        return f"<Book(id={self.id}, title='{self.Book_Title}', author='{self.Book_Author}, year='{self.Year_Of_Publication}')>"

    @classmethod
    def ajouter_livre(cls, session, ISBN, title, auteur, annee, editeur, img_url_s, img_url_m, img_url_l):
        nouveau_livre = cls(ISBN=ISBN, Book_Title=title, Book_Author=auteur, Year_Of_Publication=annee, Publisher=editeur, Image_URL_S= img_url_s, Image_URL_M= img_url_m, Image_URL_L= img_url_l)
        session.add(nouveau_livre)
        session.commit()
        print(f"Livre ajouté : {nouveau_livre}")


def import_books_from_csv(session, csv_file_path):
    with open(csv_file_path, newline='', encoding='ISO-8859-1') as csvfile:
        csvreader =  csv.DictReader(csvfile, delimiter=';', quotechar='"', escapechar='\\')
        for row in csvreader:
            book = Book(
                ISBN=row['ISBN'],
                Book_Title=row['Book-Title'],
                Book_Author=row['Book-Author'],
                Year_Of_Publication=int(row['Year-Of-Publication']),
                Publisher=row['Publisher'],
                Image_URL_S=row['Image-URL-S'],
                Image_URL_M=row['Image-URL-M'],
                Image_URL_L=row['Image-URL-L']
            )
            session.add(book)
        session.commit()



if __name__ == '__main__':
    # Configuration de la base de données
    #remplacer par le lien de la base potgrésql
    engine = create_engine(DATABASE_URL) 
    Base.metadata.create_all(engine)
    csv_file_path = './books.csv'
    import_books_from_csv(csv_file_path)
    

# Chemin vers le fichier CSV



