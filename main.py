from peewee import *
from sys import argv
import datetime
import random
import os.path
import pytest

db_name = 'database.db'
db = SqliteDatabase(db_name)

class BaseModel(Model):
    class Meta:
        database = db

class Clients (BaseModel):
    name = CharField()
    city = CharField()
    address = CharField()

class Orders (BaseModel):
    clients = ForeignKeyField(Clients, backref='client')
    date = DateTimeField()
    amount = IntegerField()
    description = CharField()

# Функции
def init_db():
    if os.path.exists(db_name) == True:
        os.remove(db_name)
        print('The database has been deleted.')
    db.create_tables([Clients, Orders], safe=True)
    print('The database has been created.')


def fill_db():
    # ---Create table---
    people_number = 11
    print('Filling out database...')
    clients_list = []
    name_arr = ["Louise", "Gordon", "Casey", "Michael", "Marcus",
                "Henry", "Jordan", "Maria", "Joseph", "Smith",
                "Anthony", "Sam", "Florence", "Davis", "Theresa"]

    city_arr = ["Moscow", "Berlin", "Paris", "Washington", "Kyoto",
                "Lisbon", "Santiago", "Atlanta", "Prague", "Shanghai",
                "Denver", "Woburgh", "Efruburgh", "Troxlens", "Phelvine"]

    address_arr = ["5124 E Street Southeast", "1010 M Street Northwest", "1347 Blackwalnut Court", "906 West Berry Street", "3604 Ridgehaven Drive",
                   "10340 West 62nd Place", "78 Cliffside Drive", "275 Ridge Lane", "10700 South Pennsylvania Avenue", "165 New Hampshire Avenue",
                   "6100 Bullard Drive", "6206 Waters Avenue", "2349 East Tall Oaks Drive", "	2729 East 14th Street", "31 Ashworth Street"]

    for i in range(people_number):
        clients_list.append({'name': name_arr[random.randint(0, len(name_arr)-1)], 'city': city_arr[random.randint(
            0, len(city_arr)-1)], 'address': address_arr[random.randint(0, len(address_arr)-1)]})

    orders_list = []
    orders_list_dis = ['muffin', 'lollipop', 'cake',
                       'sorbet', 'pancake', 'donut']

    for i in range(len(clients_list)):
        orders_list.append({'clients': i+1, 'date': str(random.randint(2020, 2024))+'-'+str(random.randint(1, 12))+'-'+str(
            random.randint(1, 28)), 'amount': random.randint(1, 100), 'description': orders_list_dis[random.randint(0, len(orders_list_dis)-1)]})

    Clients.insert_many(clients_list).execute()
    Orders.insert_many(orders_list).execute()
    print('Database has been filled.')


def show_db(names):
    if names == 'Clients':
        print('\nNAME\tSITY\tADDRESS')
        query = Clients.select().order_by(Clients.id)
        for row in query:
            print(row.name, row.city, row.address, sep='\t', end='\n')
    elif names == 'Orders':
        print('\nID CLIENTS\t\tDATE\t\t\tAMOUNT\t\tDESCRIPTION')
        query = Orders.select().order_by(Orders.id)
        for row in query:
            print(row.clients.name, row.date, row.amount,
                  row.description, sep='\t\t', end='\n')
    elif names == 'all':
        print('\n-----------TABLE CLIENTS-----------\n')
        print('\nNAME\tSITY\tADDRESS')
        query = Clients.select().order_by(Clients.id)
        for row in query:
            print(row.name, row.city, row.address, sep='\t', end='\n')
        print('\n-----------TABLE ORDERS-----------\n')
        print('\nID CLIENTS\t\tDATE\t\t\tAMOUNT\t\tDESCRIPTION')
        query = Orders.select().order_by(Orders.id)
        for row in query:
            print(row.clients.name, row.date, row.amount,
                  row.description, sep='\t\t', end='\n')


if __name__ == "__main__":
    #param = ['init']
    param = ['fill']
    #param = ['show', 'all']

    if len(param) == 0:
        print("for create db:\tinit\nfor fill:\tfill\nfor show db:\tshow\n")
    else:
        if param[0] == 'init':
            init_db()
        if param[0] == 'fill':
            fill_db()
        if param[0] == 'show':
            show_db(param[1])
