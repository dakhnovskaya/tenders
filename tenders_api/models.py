from django.db import models


class Tender(models.Model):
    date_sum_up = models.DateField(verbose_name='Дата принятия решения по тендеру')
    cost_item = models.CharField(max_length=100,verbose_name='Статья расходов')
    item = models.CharField(max_length=200, verbose_name='Предмет тендера')
    customer = models.CharField(max_length=100, verbose_name='Заказчик')
    contractor = models.CharField(max_length=100, verbose_name='Исполнитель')
    period_validator = models.DurationField(verbose_name='Период, на который действуют итоги тендера')
    total_amount = models.FloatField(verbose_name='Итоговая сумма торгов')
    not_carried = models.BooleanField(null=True)
    level_of = models.CharField(max_length=100)
    order_selection_win = models.CharField(max_length=500)
