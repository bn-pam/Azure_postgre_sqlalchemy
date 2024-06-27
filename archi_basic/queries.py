from script_sqlalchemy import Book, create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'postgresql://pbosql:rgFa%$"j99"qHx"@pb-postgresql.postgres.database.azure.com:5432/db1books'

engine = create_engine(DATABASE_URL) 
Session = sessionmaker(bind=engine)
session = Session()

def filtre_par_titre(session, mot):
    x=0
    for book in session.query(Book).filter_by(Book_Title = mot).all(): # On interroge la table Book de la base de donnée en appliquant un filtre via la colonne titre. On resort tous les résultats sous forme de liste
        print(book)
    print(x)

def filtre_par_annee(session, annee):
    x=0
    for book in session.query(Book).filter_by(Year_Of_Publication = annee).all(): # On interroge la table Book de la base de donnée en appliquant un filtre via la colonne titre. On resort tous les résultats sous forme de liste
        x+=1
        #print(book)
    print(x)



#filtre_par_titre(session, 'The Hobbit')
filtre_par_annee(session, 2000)
Book.ajouter_livre(session, 123456789, 'test_titre', 'test_auteur', 2001, 'test_editeur', 'test_url_s', 'test_url_m', 'test_url_l')