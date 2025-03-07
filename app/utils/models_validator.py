# aqui são criados utilitários para models
from django.core.exceptions import ValidationError


def validate_png(image):
    if not image.name.lower().endswith('.png'):
        raise ValidationError('Somente arquivos PNG')
