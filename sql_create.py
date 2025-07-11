
import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship, sessionmaker




Base = declarative_base()

class Publisherr(Base):
    __tablename__ = "publisher"

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String, unique=True)

  

class Book(Base):
    __tablename__= "book"

    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String, unique=True)
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey("publisher.id"), nullable=False)

   
    course = relationship(Publisherr, backref="book")

class Shop(Base):
    __tablename__ = "shop"

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=30), unique=True)

class Stock(Base):
    __tablename__ = "stock"
    
    id = sq.Column(sq.Integer, primary_key=True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey("book.id"), nullable=False)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey("shop.id"), nullable=False)
    count = sq.Column(sq.Integer)
    
    # course = relationship(Course, back_populates="homeworks")
    book = relationship(Book, backref="stocks")
    shop = relationship(Shop, backref="stocks")

class Sale(Base):
    __tablename__ = "sale"

    id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.Float, nullable=False)
    data_sale = sq.Column(sq.Date, nullable=False)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey("stock.id"), nullable=False)
    count = sq.Column(sq.Integer)

    stock = relationship(Stock, backref="sales")


def create_tables(engine):
    # Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


sql_base = "postgresql://postgres:7777777@localhost:5432/sqlalchemy"
engine = sq.create_engine(sql_base)
create_tables(engine)

# сессия
Session = sessionmaker(bind=engine)
session = Session()

select = session.query(Publisherr).all()
print(select)
