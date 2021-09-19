from django.db import models
from django.template.defaultfilters import slugify

class Category(models.Model):
    name = models.CharField(max_length = 255, verbose_name="Nom")
    thumbnail = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Image')

    class Meta:
        verbose_name = "Catégorie"

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Titre', help_text='Maximum: 255 caractères')
    author = models.CharField(max_length=255, verbose_name='Auteur', help_text='Maximum: 255 caractères')
    category = models.ForeignKey(Category, verbose_name='Catégorie', null=True, on_delete=models.SET_NULL)
    thumbnail = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Image')
    slug = models.SlugField()
    intro = models.TextField()
    keywords = models.TextField(verbose_name='Mots clés')
    content = models.TextField(verbose_name='Contenu')
    date_added = models.DateTimeField(auto_now_add=True, verbose_name='Date de création')

    class Meta:
        ordering = ['-date_added']
        verbose_name = "Article"
    
    def save(self, *args, **kwargs):
        original_slug = slugify(self.title)
        queryset = Post.objects.all().filter(slug__iexact=original_slug).count()

        count = 1
        slug = original_slug
        while(queryset):
            slug = original_slug + '-' + str(count)
            count += 1
            queryset = Post.objects.all().filter(slug__iexact=slug).count()

        self.slug = slug

        super(Post, self).save(*args, **kwargs)

    # def __str__(self):
    #     return self.title

class Pub(models.Model):
    title = models.CharField(max_length=255, verbose_name='Titre', help_text='Maximum: 255 caractères')
    link = models.CharField(max_length=500, verbose_name='Lien', help_text='Maximum: 500 caractères')
    thumbnail = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Image')