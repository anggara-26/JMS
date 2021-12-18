# Generated by Django 4.0 on 2021-12-13 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=255, verbose_name='Nama Perusahaan Client')),
                ('logo', models.ImageField(upload_to='static/assets/images/clients/%Y/%m/%d', verbose_name='Logo Client')),
                ('web', models.URLField(blank=True, default='#', help_text='masukkan url website client, beri # jika tidak ada)', max_length=500, verbose_name='Website Client')),
            ],
        ),
    ]
