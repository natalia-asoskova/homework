def get_mask_card_number(card_number: str) -> str | None:
    """функция маскирующая номер карты"""
    if card_number.isdigit() and len(card_number) == 16:
        return f"{card_number[:4]} {card_number[4:6]}{'*' * 2} {'*' * 4} {card_number[12:]}"
    else:
        return None


def get_mask_account(bank_account: str) -> str | None:
    """функция маскирующая номер счета"""
    if bank_account.isdigit() and len(bank_account) == 20:
        return f"{'*' * 2}{bank_account[-4::]}"
    else:
        return None
