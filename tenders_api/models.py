from django.db import models
from django.utils import timezone


class Customer(models.Model):
    name = models.CharField(max_length=256, verbose_name='Наименование заказчика')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=256, verbose_name='Наименование категории')

    def __str__(self):
        return self.name


class Stage(models.Model):
    name = models.CharField(max_length=256, verbose_name='Наименование этапа')

    def __str__(self):
        return self.name


class TypePurchase(models.Model):
    name = models.CharField(max_length=256, verbose_name='Наименование вида')

    def __str__(self):
        return self.name


class Tender(models.Model):
    deadline_app = models.DateTimeField(verbose_name='Приём заявок закончится')
    date_publication = models.DateTimeField(default=timezone.now, verbose_name='Дата публикации')
    customer = models.ForeignKey(Customer, verbose_name='Заказчик', on_delete=models.PROTECT)
    brief_description = models.CharField(max_length=256, verbose_name='Краткое описание')
    initial_price = models.FloatField(verbose_name='Начальная цена')
    contract_guarantee = models.FloatField(verbose_name='Обеспечение контракта')
    place_performance = models.CharField(max_length=512, verbose_name='Место исполнения')
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.PROTECT)
    procurement_stage = models.ForeignKey(Stage, verbose_name='Этап закупки', on_delete=models.PROTECT)
    type_purchase = models.ForeignKey(TypePurchase, verbose_name='Вид закупки', on_delete=models.PROTECT)


