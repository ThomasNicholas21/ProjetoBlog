# será feito um utilitário para gerar slugs aleatórios
from random import SystemRandom
from django.utils.text import slugify
import string


def random_letters(size):
    return ''.join(
        SystemRandom().choices(
            string.ascii_lowercase + string.digits, size
            )
        )

def slugify_new(text, size=5):
    return slugify(text) + random_letters(size)
