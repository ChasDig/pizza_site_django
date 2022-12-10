from django.db import models

from datetime import datetime


class Pizza(models.Model):
    """ Модель: Пицца """

    name = models.CharField(verbose_name='Название пиццы', max_length=50)
    weight = models.CharField(verbose_name='Вес пиццы',  max_length=30)
    descriptions = models.TextField(verbose_name='Описание пиццы', max_length=500)
    price = models.IntegerField(verbose_name='Цена пицыы', )
    image_url = models.URLField(verbose_name='Изображение пиццы', null=True)
    url = models.SlugField(verbose_name='Префикс', default='1')

    def __str__(self):
        return self.name

    class Meta:

        verbose_name = 'Пицца'
        verbose_name_plural = 'Пиццы'
        ordering = ['name']


class Order(models.Model):
    """ Модель: Заказ пиццы """

    order_stage_list = (('Accepted', 'Заказ принят'), ('Delivered', 'Заказ доставлен'))

    number_order = models.IntegerField(verbose_name='Индивидуальный номер заказа', unique=True,
                                       error_messages='Проблема при создании индивидуального номера заказа',
                                       default=f'{datetime.today().day}_{datetime.today().hour}_{datetime.today().minute}')
    pizza = models.ForeignKey(Pizza, verbose_name='Заказанная пицца', on_delete=models.SET('Такой пиццы больше нет'))
    content = models.TextField(verbose_name='Дополнительные пожелания к заказу',
                               default='У клиента нет дополнительных пожеданий к заказу')
    order_stage = models.CharField(verbose_name='Стадия заказа', choices=order_stage_list, max_length=9)
    time_accept = models.TimeField(verbose_name='Время принятия заказа', auto_now_add=True)
    time_delivery = models.TimeField(verbose_name='Время принятия заказа', )

    def __str__(self):
        return self.number_order

    class Meta:

        verbose_name = 'Работа с заказом'
        verbose_name_plural = 'Работа с заказами'
        ordering = ['number_order']


class Reviews(models.Model):
    """ Отзывы покупателей """

    username = models.CharField(verbose_name='Имя клиента:', max_length=50)
    email = models.EmailField()
    comment = models.TextField(verbose_name='Текст комментария', max_length=500)
    order = models.OneToOneField(Order, verbose_name='Комментарий к заказу', on_delete=models.CASCADE)
    parents = models.ForeignKey('self', verbose_name='Комментарий на комментарий', on_delete=models.CASCADE, blank=True,
                                null=True)

    def __str__(self):
        return self.username

    class Meta:

        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
