class Urls:
    BASE_URL = 'https://qa-scooter.praktikum-services.ru'
    CREATE_ORDERS = f'{BASE_URL}/api/v1/orders'
    CREATE_COURIER = f'{BASE_URL}/api/v1/courier'
    RECEIVING_ORDERS = f'{BASE_URL}/api/v1/orders'
    LOGIN = f'{BASE_URL}/api/v1/courier/login'
    DELETE_COURIER = f'{BASE_URL}/api/v1/courier/login'


class Message:
    RESPONSE_SUCCESS = '{"ok":true}'
    CONFLICT_LOGIN = 'Этот логин уже используется. Попробуйте другой.'
    INSUFFICIENT_INFO = 'Недостаточно данных для создания учетной записи'
    INSUFFICIENT_LOGIN = 'Недостаточно данных для входа'
    INVALID_DATA = 'Учетная запись не найдена'


class PersonalDate:
    personal_date = [
        ['Иван', 'Рождественский', 'Большая 7', '1', '+79006663636', '1', '2024-04-01', 'Пасиба', 'BLACK'],
        ['Саламандр', 'Вилков', 'Старобольшая 74', '10', '+79621111111', '16', '2023-08-30', 'ой Ей', 'GREY'],
        ['Алекс', 'Карликов', 'Високосная улица, д5', '15', '+79151201200', '12', '2023-12-25', 'Два слова', 'BLACK, GREY'],
        ['Катя', 'Большевичка', 'Новолюблино 15', '36', '+79265443030', '5', '2021-06-06', 'Целых три слова', '']
    ]
