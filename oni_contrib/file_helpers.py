import os


def get_extension(filename) -> str:
    """
    Retorna a extensão de um arquivo
    Args:
        filename: Nome do arquivo

    Returns: extensão do arquivo
    """
    name, extension = os.path.splitext(filename)
    return extension
