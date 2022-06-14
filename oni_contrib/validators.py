from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from pathlib import Path

from typing import List


def _default_extension_validator(file, extensions: List[str]) -> None:
    """
    Validador padrão de extensões de arquivos
    Args:
        file: Arquivo alvo
        extensions: Lista de extensões permitidas

    Returns: None
    """
    extension = Path(file.file.name).suffix
    if extension not in extensions:
        raise ValidationError(
            _('Invalid file format. Valid formats are %s') % ', '.join(extensions)
        )


def validate_document_format(file) -> None:
    """
    Validador de extensão do tipo Documento
    Args:
        file: Arquivo alvo

    Returns: None
    """
    _default_extension_validator(file, ['.doc', '.pdf', '.zip'])


def validate_image_format(file) -> None:
    """
    Validador de extensão do tipo Imagem
    Args:
        file: Arquivo alvo

    Returns: None
    """
    _default_extension_validator(file, ['.png', '.jpg', '.jpeg', '.JPG', '.JPEG', '.PNG'])


def validate_audio_format(file) -> None:
    """
    Validador de extensão do tipo Áudio
    Args:
        file: Arquivo alvo

    Returns: None
    """
    _default_extension_validator(file, ['.wav'])


def validate_file_max_size(file, max_size_kb: int) -> None:
    """
    Validador de extensão do tipo Documento
    Args:
        file: Arquivo alvo
        max_size_kb: Tamanho máximo do arquivo em KB

    Returns: None
    """
    file_size = file.file.size
    limit_kb = max_size_kb
    if file_size > limit_kb * 1024:
        raise ValidationError(_("Max size of file is %s KB") % limit_kb)


def validate_image_max_300(image):
    """ Valida o tamanho do arquivo em 300kb
    """
    return validate_file_max_size(image, 300)


def validate_image_max_500(image):
    """ Valida o tamanho do arquivo em 500kb
    """
    return validate_file_max_size(image, 500)


def validate_file_max_1000(file):
    """ Valida o tamanho do arquivo em 1mb
    """
    return validate_file_max_size(file, 1000)


def validate_file_max_2000(file):
    """ Valida o tamanho do arquivo em 2mb
    """
    return validate_file_max_size(file, 2000)


def validate_file_max_5000(file):
    """ Valida o tamanho do arquivo em 5mb
    """
    return validate_file_max_size(file, 5000)


def validate_file_max_10000(file):
    """ Valida o tamanho do arquivo em  10mb
    """
    return validate_file_max_size(file, 10000)


def validate_file_max_15000(file):
    """ Valida o tamanho do arquivo em 15mb
    """
    return validate_file_max_size(file, 15000)


def validate_file_max_20000(file):
    """ Valida o tamanho do arquivo em 20mb
    """
    return validate_file_max_size(file, 20000)


def validate_file_max_50000(file):
    """ Valida o tamanho do arquivo em 50mb
    """
    return validate_file_max_size(file, 50000)


def validate_file_max_200000(file):
    """ Valida o tamanho do arquivo em 200mb
    """
    return validate_file_max_size(file, 200000)


def validate_file_max_300000(file):
    """ Valida o tamanho do arquivo em 300mb
    """
    return validate_file_max_size(file, 300000)


def validate_only_positive_values(value):
    """ Valida se o valor é positivo
    """
    if value is None or value <= 0:
        raise ValidationError(_('The value must be greater than zero!'))
