import logging


def log_message(message: str, logger: str = 'django') -> None:
    """
    Envia uma mensagem qualquer para um logger do Django, que deve estar configurado no settings.py
    Args:
        message: Mensagem que será enviada para o log
        logger: String que identifica o logger do Django desejado
    Returns: None
    """
    logger = logging.getLogger('django')
    logger.exception(message)
