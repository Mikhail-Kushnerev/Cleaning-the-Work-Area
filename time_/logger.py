import logging
import sys


logging.basicConfig(
    level=logging.INFO,
    encoding='utf-8',
    format="|\t%(asctime)s – [%(levelname)s]: %(message)s. Исполняемый файл – '%(name)s'",
    handlers=(logging.StreamHandler(sys.stdout), )
)
logger = logging.getLogger(__name__)
