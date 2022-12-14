# Generated by Django 4.1.2 on 2022-10-29 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0005_alter_produto_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='img',
        ),
        migrations.AddField(
            model_name='categoria',
            name='imagem',
            field=models.FileField(blank=True, default='', upload_to='img_category/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='produto',
            name='imagem',
            field=models.FileField(blank=True, default='', upload_to='img_prod/%Y/%m/%d/'),
        ),
    ]
