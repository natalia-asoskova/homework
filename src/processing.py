from datetime import datetime


def filter_by_state(data, state='EXECUTED'):
    """
    Фильтрует список словарей по значению ключа 'state'.
    :param data: Список словарей для фильтрации.
    :param state: Значение ключа 'state' для фильтрации (по умолчанию 'EXECUTED').
    :return: Новый список словарей, соответствующих указанному значению 'state'.
    """
    return [item for item in data if item.get('state') == state]

def sort_by_date(data, descending=True):
    """
      Сортирует список словарей по ключу 'date'.
      :param data: Список словарей для сортировки.
      :param descending: Порядок сортировки. True для убывающего порядка (по умолчанию), False для возрастающего.
      :return: Новый список словарей, отсортированный по дате.
      """

    def parse_date(item):
        date_str = item.get('date')
        if not date_str:
            return datetime.min
        try:
            return datetime.fromisoformat(date_str)
        except ValueError:
            return datetime.min

    return sorted(data, key=parse_date, reverse=descending)


# проверка
data = [
    {'id': 1, 'state': 'EXECUTED'},
    {'id': 2, 'state': 'PENDING'},
    {'id': 3, 'state': 'EXECUTED'},
]
filtered_data = filter_by_state(data)
print(filtered_data)

