# Generated by Django 2.2 on 2019-04-30 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cadastro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='tipo_de_usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Cadastro.Tipo_de_Usuario'),
            preserve_default=False,
        ),
    ]
