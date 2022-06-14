from django.utils.html import format_html


def return_mark_safe(string: str) -> str:
    """
    Retorna uma string como mark_safe
    Args:
        string: Autoexplicativo.

    Returns: string com mark_safe
    """
    return format_html(string.replace("{", "{{").replace("}", "}}"))


def remove_parameters_and_dash(url: str) -> str:
    """
    Remove os parâmetros e a barra da url
    Args:
        url: Autoexplicativo

    Returns: url sem parâmetros nem barra
    """
    dash_location = url.find('/')
    if dash_location >= 0:
        url = url[:dash_location]
    params_locations = url.find('?')
    if params_locations >= 0:
        url = url[:params_locations]
    return url
