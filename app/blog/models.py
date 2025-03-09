from django.db import models
from utils.rand_slug import slugify_new
from django.contrib.auth.models import User
# Create your models here.

class Tag(models.Model):
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    name = models.CharField(max_length=255)
    # um texto que representa a entidade, sendo uma forma de "id"
    slug = models.SlugField(
        unique=True, default=None,
        null=True, blank=True, 
        max_length=255
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_new(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=255)
    slug = models.SlugField(
        unique=True, default=None,
        null=True, blank=True,
        max_length=255
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_new(self.name)
        
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Page(models.Model):
    class Meta:
        verbose_name = 'Page'
        verbose_name_plural = 'Pages'
    
    title = models.CharField(max_length=65)
    slug = models.SlugField(
        unique=True, default='',
        null=False, blank=True,
        max_length=255
    )
    is_published = models.BooleanField(
        default=True,
        help_text=(
            'Este campo precisa estar marcado para '
            'publicação aparecer no blog.'
        )
    )
    content = models.TextField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_new(self.name)
        
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Post(models.Model):
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    title = models.CharField(max_length=65)
    slug = models.SlugField(
        unique=True, default='',
        blank=True, null=False,
        max_length=65
    )
    is_published = models.BooleanField(
        default=True,
        help_text=(
            'Este campo precisa estar marcado para '
            'publicação aparecer no blog.'
        )
    )
    content = models.TextField()
    cover = models.ImageField(upload_to='post/Y%/%m/', blank=True, default='')
    cover_in_posts_content = models.BooleanField(
        default=True,
        help_text=(
            'Exibir a imagem de capa também dentro do '
            'conteúdo do post?'
        )
    )
    # auto_now_add x auto_now
    # atualiza uma vez só x atualiza após cada save
    created_at = models.DateTimeField(auto_now_add=True)
    # o atributo related_name substitui o nome de query set 
    # para evitar conflitos. Por exemplo, para pegar um dado
    # relacionado ao usuário, deve-se usar user.post_set.all()
    # com related_name ficaria: user.post_created_by, pois user 
    # é uma ForeignKey.
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True, null=True,
        related_name='post_created_by'
    )
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True, null=True,
        related_name='post_updated_by'
    )
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True, default=None,
    )
    # Uma relação de muito pra muitos com Tags, pois um post 
    # pode ter muitas tags e uma Tag pode estar em muitos posts
    tags = models.ManyToManyField(Tag, blank=True, default='')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_new(self.title)
        
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    