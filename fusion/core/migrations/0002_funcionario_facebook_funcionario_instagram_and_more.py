# Generated by Django 5.0.6 on 2024-05-17 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='facebook',
            field=models.CharField(default='#', max_length=100, verbose_name='Facebook'),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='instagram',
            field=models.CharField(default='#', max_length=100, verbose_name='Instagram'),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='twitter',
            field=models.CharField(default='#', max_length=100, verbose_name='Twitter'),
        ),
        migrations.AlterField(
            model_name='servico',
            name='icone',
            field=models.CharField(choices=[('lni-starts-up', 'Graficos'), ('lni-mobile', 'Mobile'), ('lni-users', 'Usuarios'), ('lni-cog', 'Engrenagem'), ('lni-rocket', 'Foguete'), ('lni-layers', 'Design')], max_length=50, verbose_name='Icone'),
        ),
    ]
