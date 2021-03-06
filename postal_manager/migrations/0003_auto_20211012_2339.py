# Generated by Django 3.2.8 on 2021-10-12 23:39

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('postal_manager', '0002_alter_objetos_db_data_inclusao'),
    ]

    operations = [
        migrations.AddField(
            model_name='objetos_db',
            name='vencimento',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='objetos_db',
            name='classe_obj',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='postal_manager.tipos_postais_base', verbose_name='Tipo'),
        ),
        migrations.AlterField(
            model_name='objetos_db',
            name='destinatario',
            field=models.CharField(max_length=70, verbose_name='Destinatário'),
        ),
    ]
