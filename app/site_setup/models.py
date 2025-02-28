from django.db import models

# Create your models here.

# Configuração de menu para o aplicativo blog
class MenuLink(models.Model):
    class Meta:
        verbose_name = 'Menu Link'
        verbose_name_plural = 'Menu Links'

    text = models.CharField(max_length=50)

    # permite que o usuário coloque urls ou caminhos
    # e new_tap define se vai aparecer ou não.
    url_or_path = models.CharField(max_length=2048)
    new_tab = models.BooleanField(default=False)

    def __str__(self):
        return self.text
