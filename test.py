import pytest
import os.path
import main


def test_create_database():  # Тест на создание БД
    main.init_db()
    assert os.path.exists(main.db_name) == True


def test_clients():  # Тест на наличие столбцов в Clients
    assert main.Clients.name == False
    assert main.Clients.city == False
    assert main.Clients.address == False


def test_orders():  # Тест на наличие столбцов в Orders
    assert main.Orders.clients == False
    assert main.Orders.amount == False
    assert main.Orders.date == False
    assert main.Orders.description == False


def test_sum_clients():  # Тест на наличие 10 строк в Clients
    main.fill_db()
    assert len(main.Clients.select()) > 10


def test_sum_orders():  # Тест на наличие 10 строк в Orders
    main.fill_db()
    assert len(main.Orders.select()) > 10