from datetime import datetime

class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

    @property
    def name_items(self):
        return self.__name_items

    @property
    def number_items(self):
        return self.__number_items

    def add_item_to_cheque(self, name:str):
        # не была уверена, как именно по заданию ожидается прокинуть экзепшн,
        # так что сделала без try, except
        if len(name) == 0 or len(name) > 40:
            raise ValueError('Нельзя добавить товар, если в его названии нет символов или их больше 40')
        if name not in list(self.__item_price.keys()):
            raise NameError('Позиция отсутствует в товарном справочнике')
        self.__name_items.append(name)
        self.__number_items += 1


    def delete_item_from_check(self, name:str):
        if name not in list(self.__name_items):
            raise NameError('Позиция отсутствует в чеке')
        self.__name_items.remove(name)
        self.__number_items -= 1

    def get_check_amount(self):
        total = []
        for item in self.__name_items:
            total.append(self.__item_price[item])
        product_cost = sum(total)
        if self.__number_items > 10:
            product_cost *= 0.9
        return product_cost

    def _calculate_twenty_percent_tax(self):
        twenty_percent_tax = []
        total = []
        for item in self.__name_items:
            if self.__tax_rate[item] == 20:
                # тут получилось, что twenty_percent_tax список довольно излишен,
                # но лишние строчки кода не хотелось добавлять и при этом выполнить условия задания
                twenty_percent_tax.append(item)
                total.append(self.__item_price[item])
        total_twenty_per_tax = sum(total) * 0.2
        if self.__number_items > 10:
            total_twenty_per_tax *= 0.9
        return total_twenty_per_tax

    def _calculate_ten_percent_tax(self):
        ten_percent_tax = []
        total = []
        for item in self.__name_items:
            if self.__tax_rate[item] == 10:
                # тут аналогично
                ten_percent_tax.append(item)
                total.append(self.__item_price[item])
        total_ten_per_tax = sum(total) * 0.1
        if self.__number_items > 10:
            total_ten_per_tax *= 0.9
        return total_ten_per_tax

    def get_total_tax(self):
        total_tax = self._calculate_twenty_percent_tax() + self._calculate_ten_percent_tax()
        return total_tax

    @staticmethod
    def get_telephone_number(telephone_number:int):
        if type(telephone_number) != int:
            raise ValueError('Необходимо ввести цифры')
        if len(str(telephone_number)) > 10:
            raise ValueError('Необходимо ввести 10 цифр после "+7"')
        return f'+7{telephone_number}'

    @staticmethod
    def get_date_and_time():
        date_and_time = []
        now = datetime.now()
        dates = [
            ['часы', lambda x:x.hour],
            ['минуты', lambda x: x.minute],
            ['день', lambda x: x.day],
            ['месяц', lambda x: x.month],
            ['год', lambda x: x.year]
        ]
        for date in dates:
            date_and_time.append(f'{date[0]}: {date[1](now)}')
        return date_and_time

