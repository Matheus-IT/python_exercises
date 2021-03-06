# Generated by Django 3.2.9 on 2021-12-14 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('summary', models.TextField(help_text='Breve descrição da obra', max_length=1000)),
                ('isbn', models.CharField(max_length=11, verbose_name='ISBN')),
                ('genre', models.ManyToManyField(help_text='Selecione um gênero literário', to='catalog.Genre')),
            ],
        ),
    ]
