# Generated by Django 2.1.1 on 2018-10-01 16:02

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Наименование категории')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Наименование заказчика')),
            ],
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Наименование этапа')),
            ],
        ),
        migrations.CreateModel(
            name='Tender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deadline_app', models.DateTimeField(verbose_name='Приём заявок закончится')),
                ('date_publication', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата публикации')),
                ('brief_description', models.CharField(max_length=256, verbose_name='Краткое описание')),
                ('initial_price', models.FloatField(verbose_name='Начальная цена')),
                ('contract_guarantee', models.FloatField(verbose_name='Обеспечение контракта')),
                ('place_performance', models.CharField(max_length=512, verbose_name='Место исполнения')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tenders_api.Category', verbose_name='Категория')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tenders_api.Customer', verbose_name='Заказчик')),
                ('procurement_stage', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tenders_api.Stage', verbose_name='Этап закупки')),
            ],
        ),
        migrations.CreateModel(
            name='TypePurchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Наименование вида')),
            ],
        ),
        migrations.AddField(
            model_name='tender',
            name='type_purchase',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tenders_api.TypePurchase', verbose_name='Вид закупки'),
        ),
    ]