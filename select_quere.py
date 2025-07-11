from sql_create import Publisherr, Book, Shop, Stock, Sale, session
#import sql_create

def select_id(id):

    results = session.query(Book, Shop, Sale).\
        select_from(Stock).\
        join(Book, Stock.id_book == Book.id).\
        join(Shop, Stock.id_shop == Shop.id).\
        join(Sale, Stock.id == Sale.id_stock).\
        filter(Book.id == id).\
        all()

    
    for book, shop, sale in results:
        print(f"{book.title} | {shop.name} |  {sale.price} | {sale.data_sale}")

def select_name(title):

    results = session.query(Book, Shop, Sale, Publisherr).\
            select_from(Stock).\
            join(Book, Stock.id_book == Book.id).\
            join(Shop, Stock.id_shop == Shop.id).\
            join(Sale, Stock.id == Sale.id_stock).\
            join(Publisherr, Publisherr.id == Book.id_publisher).\
            filter(Publisherr.name == 'Pearson').\
            all()

    # Обработка результатов
    for book, shop, sale, publisher in results:
        print(f"{book.title} | {shop.name} |  {sale.price} | {sale.data_sale}")


print("""
    Выеберите вариант запроса:
    1: ID
    2: Имя  
""")
id = input("Номер: 1")

if id == 1:
    pass
elif id == 2:
    pass
else:
    print('Неверный запрос')
