import decimal
from typing import Union


def round_or_0(value: Union[decimal.Decimal, float], digits: int =2) -> int:
    """
    Retorna o arredondamento do valor, ou 0.
    Args:
        value: Valor a ser arredondado
        digits: Qtd de casas decimais para o arredondamento

    Returns: Valor arredondado ou 0
    """
    try:
        return round(decimal.Decimal(value), digits)
    except Exception:
        return 0


def round_or_1(value: Union[decimal.Decimal, float], digits: int =2) -> int:
    """
    Retorna o arredondamento do valor, ou 1.
    Args:
        value: Valor a ser arredondado
        digits: Qtd de casas decimais para o arredondamento

    Returns: Valor arredondado ou 1
    """
    try:
        qtd = round(decimal.Decimal(value), digits)
        return max(qtd, 1)
    except Exception:
        return 1
