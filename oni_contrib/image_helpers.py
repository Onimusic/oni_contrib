import os

from io import BytesIO
from typing import Union

from django.core.files import File
from PIL import Image


def make_thumbnail(image, size=(100, 100), filename='') -> Union[File, None]:
    """
    Gera thumbnail de uma imagem
    Args:
        image: Arquivo de imagem
        size: Tamanho desejado para a thumb
        filename: Nome do arquivo desejado

    Returns: Objeto django.core.files.File com a thumb
    """
    if not image:
        return None
    pil_image = Image.open(image).convert('RGB')
    pil_image.thumbnail(size)  # resize image
    thumb_io = BytesIO()
    pil_image.save(thumb_io, 'JPEG', quality=85)
    return File(thumb_io, name=filename)  # create a django friendly File object


def make_thumbnail_and_set_for_model(obj, image_fied, thumb_field, size=(150, 150)) -> None:
    """
    Cria uma thumbnail e seta no objeto
    Args:
        obj: Objeto que vai receber a thumbnail
        image_fied: Nome do atributo da imagem do modelo
        thumb_field: Nome do atributo da thumbnail do modelo
        size: Tamanho desejado para a thumb

    Returns: None
    """
    if image := getattr(obj, image_fied, None):
        cover_filename = os.path.basename(getattr(image, 'name', ''))
        image_thumbnail = getattr(obj, thumb_field, None)
        try:
            if not image_thumbnail or cover_filename != os.path.basename(getattr(image_thumbnail, 'name', '')):
                setattr(obj, thumb_field, make_thumbnail(image, size=size, filename=cover_filename))
        except IOError:
            # aqui a imagem nao existe.
            pass
    return None
