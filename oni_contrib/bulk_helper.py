from django.utils.html import format_html
from io import BytesIO as IO
import pandas


def get_blank_generic_file_from_fields(bulk_fields) -> bytes:
    """
    Cria e retorna um arquivo xlsx de acordo com uma lista de campos
    Args:
        bulk_fields: Lista de campos

    Returns: Arquivo xlsx
    """
    fields = {bulk_field[0]: [f"#{bulk_field[1]}"] for bulk_field in bulk_fields}
    df = pandas.DataFrame.from_dict(fields)
    # noinspection PyPep8Naming
    excel_file = IO()
    # noinspection PyTypeChecker
    excel_writer = pandas.ExcelWriter(excel_file, engine='xlsxwriter')
    df.to_excel(excel_writer, 'data', index=False)
    excel_writer.save()
    excel_writer.close()
    excel_file.seek(0)

    return excel_file.read()


def get_errors_messages_html(errors) -> str:
    """
    Retorna um código html com uma lista de erros ou n/a
    Args:
        errors: Lista de erros

    Returns: String html com os erros no formato de lista
    """
    if not errors:
        return "n/a"
    errors = str(errors).split("|")
    return format_html(f'<br><ol>{"".join([f"<li>{error}</li>" for error in errors])}</ol>')
