# Generated by Django 2.2.1 on 2019-05-12 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publish', models.CharField(choices=[('home_first', 'HOME_FIRST'), ('how', 'HOW'), ('home_second', 'HOME_SECOND'), ('why', 'WHY'), ('howmuch', 'HOWMUCH')], default='home_first', max_length=120)),
                ('title', models.CharField(max_length=150, unique=True, verbose_name='Title')),
                ('text', models.TextField(verbose_name='body')),
                ('articlecover', models.ImageField(blank=True, null=True, upload_to='static/images')),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
            },
        ),
    ]
