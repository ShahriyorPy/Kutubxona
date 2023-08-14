# Generated by Django 4.2.2 on 2023-06-18 03:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kitob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('sahifa', models.PositiveSmallIntegerField()),
                ('janr', models.CharField(choices=[('badiiy', 'badiiy'), ('ilmiy', 'ilmiy')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Kutubxonachi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=50)),
                ('ish_vaqti', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Muallif',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=30)),
                ('tugilgan_yil', models.PositiveSmallIntegerField()),
                ('tirik', models.BooleanField(default=False)),
                ('kitoblari_soni', models.PositiveSmallIntegerField()),
                ('jinsi', models.CharField(choices=[('erkak', 'erkak'), ('ayol', 'ayol')], max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Talaba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=50)),
                ('kurs', models.PositiveSmallIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)])),
                ('yosh', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('kitob_soni', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('olingan_sana', models.DateField()),
                ('qaytardi', models.BooleanField(default=False)),
                ('qaytarish_sanasi', models.DateField(blank=True, null=True)),
                ('kitob', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.kitob')),
                ('kutubxonachi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.kutubxonachi')),
                ('talaba', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.talaba')),
            ],
        ),
        migrations.AddField(
            model_name='kitob',
            name='muallif',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.muallif'),
        ),
    ]
