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

    # Informando a MenuLink a chave estrangeira, ou seja,
    # informando a qual entidade ele pertence que seria
    # SiteSetup, que é chamado como String pois o Django,
    # consegue identificar ele na base de dados
    site_setup = models.ForeignKey('SiteSetup', 
                                   on_delete=models.CASCADE, 
                                   blank=True, null=True,
                                   default=None
                                   )
    def __str__(self):
        return self.text


class SiteSetup(models.Model):
    class Meta:
        verbose_name = 'Setup'
        verbose_name_plural = 'Setup'

    title = models.CharField(max_length=70)
    description = models.CharField(max_length=255)

    show_header = models.BooleanField(default=True)
    show_search = models.BooleanField(default=True)
    show_menu = models.BooleanField(default=True)
    show_description = models.BooleanField(default=True)
    show_pagination = models.BooleanField(default=True)
    show_footer = models.BooleanField(default=True)

    def __str__(self):
        return self.title
