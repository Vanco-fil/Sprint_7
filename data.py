class Urls:
    CREATE_ORDERS = 'https://qa-scooter.praktikum-services.ru/api/v1/orders'
    CREATE_COURIER = 'https://qa-scooter.praktikum-services.ru/api/v1/courier'
    RECEIVING_ORDERS = 'https://qa-scooter.praktikum-services.ru/api/v1/orders'
    LOGIN = 'https://qa-scooter.praktikum-services.ru/api/v1/courier/login'
    DELETE_COURIER = 'https://qa-scooter.praktikum-services.ru/api/v1/courier/login'


class Message:
    RESPONSE_SUCCESS = '{"ok":true}'
    CONFLICT_LOGIN = 'Этот логин уже используется. Попробуйте другой.'
    INSUFFICIENT_INFO = 'Недостаточно данных для создания учетной записи'
    INSUFFICIENT_LOGIN = 'Недостаточно данных для входа'
    INVALID_DATA = 'Учетная запись не найдена'


class PersonalDate:
    personal_date = [
        ['Иван', 'Рождественский', 'Большая 7', '1', '+7 900 666 36 36', '1', '2024-04-01', 'Пасиба', 'BLACK'],
        ['Алекс', 'Карликов', 'Високосная улица, д5', '15', '+79151201200', '12', '2023-12-25', 'Два слова', 'BLACK, GREY'],
        ['Катя', 'Большевичка', 'Новолюблино 15', '36', '+79265443030', '5', '2021-06-06', 'Целых три слова', '']
    ]
