# Generated by Django 4.1.2 on 2022-10-28 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0004_alter_produto_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='img',
            field=models.FileField(blank=True, default='', upload_to='media/img/%Y/%m/%d/'),
        ),
    ]
