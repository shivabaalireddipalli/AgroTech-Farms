# Generated by Django 2.2.5 on 2019-11-23 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AgroTech', '0029_seconddata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seconddata',
            name='Head',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='seconddata',
            name='img',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='seconddata',
            name='quote',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='seconddata',
            name='subquote',
            field=models.CharField(max_length=250),
        ),
    ]
