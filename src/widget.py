from datetime import datetime
def mask_card_number(card_number: str) -> str:
    """Маскирует номер карты: первые 6 и последние 4 цифры видны."""
    digits = ''.join(card_number.split())
    return f"{digits[:4]} {digits[4:6]}** **** {digits[-4:]}"


def mask_account_number(account_number: str) -> str:
    """Маскирует номер счёта: видны только последние 4 цифры."""
    return f"**{account_number[-4:]}"

def mask_account_card(data: str) -> str:
    """
    Маскирует номер карты или счёта в строке, не разделяя её на имя и номер.
    """
    if data.lower().startswith("счет"):
        parts = data.split()
        account_number = parts[-1]
        masked_number = mask_account_number(account_number)
        return f"Счет {masked_number}"
    else:
        parts = data.split()
        card_number = parts[-1]
        card_name = " ".join(parts[:-1])
        masked_number = mask_card_number(card_number)
        return f"{card_name} {masked_number}"

def get_date(date_str: str) -> str:
    """
    Преобразует дату из формата ISO 8601 (например, "2024-03-11T02:26:18.671407")
    в формат "ДД.ММ.ГГГГ" (например, "11.03.2024").

    :param date_str: строка с датой в формате ISO 8601
    :return: строка в формате "ДД.ММ.ГГГГ"
    """
    try:
        date_obj = datetime.fromisoformat(date_str)
        return date_obj.strftime("%d.%m.%Y")
    except ValueError:
        return "Неверный формат даты"


if __name__ == "__main__":
    print(mask_account_card("Visa Platinum 7000792289606361"))
    print(mask_account_card("Maestro 1234567890123456"))
    print(mask_account_card("Счет 73654108430135874305"))
    print(get_date("2024-03-11T02:26:18.671407"))
    print(get_date("не-дата"))