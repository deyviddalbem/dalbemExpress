# Generated by Django 3.2.3 on 2021-05-24 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_auto_20210522_1421'),
    ]

    operations = [
        migrations.CreateModel(
            name='FotoUsuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto_usuarios', models.FileField(upload_to='media/%Y/%m/%d/')),
            ],
        ),
        migrations.DeleteModel(
            name='Usuarios',
        ),
    ]
