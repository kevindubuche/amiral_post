# Generated by Django 3.2.7 on 2021-09-14 20:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nom')),
                ('thumbnail', models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Catégorie',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Maximum: 255 caractères', max_length=255, verbose_name='Titre')),
                ('author', models.CharField(help_text='Maximum: 255 caractères', max_length=255, verbose_name='Auteur')),
                ('thumbnail', models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Image')),
                ('slug', models.SlugField()),
                ('intro', models.TextField()),
                ('keywords', models.TextField(verbose_name='Mots clés')),
                ('content', models.TextField(verbose_name='Contenu')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='Date de création')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.category', verbose_name='Catégorie')),
            ],
            options={
                'verbose_name': 'Article',
                'ordering': ['-date_added'],
            },
        ),
    ]
