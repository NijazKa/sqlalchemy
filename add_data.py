import json
from sql_create import Publisherr, Book, Shop, Stock, Sale, create_tables, session

with open('bot_tg/sql/test_data.json', 'r') as fd:
    data = json.load(fd)

for record in data:
    if record['model'] == 'publisher':
        sql = Publisherr(id=record['pk'], name=record['fields']['name'])
        session.add(sql)
        session.commit()
        print(record['fields']['name'])

    if record['model'] == 'book':
        sql = Book(id=record['pk'], title = record['fields']['title'], id_publisher=record['fields']['id_publisher'])
        session.add(sql)
        session.commit()

    if record['model'] == 'shop':
        sql = Shop(id=record['pk'], name=record['fields']['name'])
        session.add(sql)
        session.commit()
    
    if record['model'] == 'stock':
        sql = Stock(id=record['pk'], id_book=record['fields']['id_book'], id_shop=record['fields']['id_shop'], count=record['fields']['count'])
        session.add(sql)
        session.commit()
    
    if record['model'] == 'sale':
        sql = Sale(id=record['pk'], price=record['fields']['price'], data_sale=record['fields']['date_sale'], count=record['fields']['count'], id_stock=record['fields']['id_stock'])
        session.add(sql)
        session.commit()
