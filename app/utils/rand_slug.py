# será feito um utilitário para gerar slugs aleatórios
from random import SystemRandom
from django.utils.text import slugify
import string


def random_letters(k=5):
    return ''.join(
        SystemRandom().choices(
            string.ascii_lowercase + string.digits, k
            )
        )

def slugify_new(text, k=5):
    return slugify(text) + random_letters(k)
