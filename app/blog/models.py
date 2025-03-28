from django.db import models
from utils.rand_slug import slugify_new
from django.contrib.auth.models import User
from utils.image import resize_image
from django_summernote.models import AbstractAttachment
from django.urls import reverse
# Create your models here.


class PostAttachment(AbstractAttachment):
    def save(self, *args, **kwargs):
        if not self.name :
            self.name = self.file.name

        current_file_name = str(self.file.name)
        super_save = super().save(*args, **kwargs)
        file_changed = False

        if self.file:
            file_changed = current_file_name != self.file.name

        if file_changed:
            resize_image(self.file, new_width=900, optimize=True, quality=70)

        return super_save


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

    def get_absolute_url(self):
        if not self.is_published:
            return reverse('blog:index')
        return reverse("blog:page", args=(self.slug, ))

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_new(self.title)
        
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class PostManager(models.Manager):
    # self representa objects dos models
    def get_published(self):
        return self.filter(is_published=True).order_by('-pk')
    
    def get_post(self, slug):
        return self.filter(slug=slug).first()


class Post(models.Model):
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
    
    # Como o objects é representado
    # objects = models.Manager()
    objects = PostManager()

    title = models.CharField(max_length=65)
    slug = models.SlugField(
        unique=True, default='',
        blank=True, null=False,
        max_length=65
    )
    excerpt = models.CharField(max_length=150, default='')
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

    def get_absolute_url(self):
        if not self.is_published:
            return reverse('blog:index')
        return reverse("blog:post", args=(self.slug, ))
    

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_new(self.title)
        
        current_cover_name = str(self.cover.name)
        super_save = super().save(*args, **kwargs)
        cover_changed = False

        if self.cover:
            cover_changed = current_cover_name != self.cover.name

        if cover_changed:
            resize_image(self.cover, new_width=900, optimize=True, quality=70)

        return super_save

    def __str__(self):
        return self.title
    