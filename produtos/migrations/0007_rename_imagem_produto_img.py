# Generated by Django 4.1.2 on 2022-10-29 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0006_remove_produto_img_categoria_imagem_produto_imagem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produto',
            old_name='imagem',
            new_name='img',
        ),
    ]
