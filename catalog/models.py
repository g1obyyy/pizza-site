from django.db import models
from PIL import Image

class Client(models.Model):
    id = models.AutoField('ID', primary_key=True)
    firstName = models.CharField('Имя', max_length=20)
    phone = models.CharField('Телефон', max_length=10)
    email = models.EmailField('Email', default=None)
    birthday = models.DateField('Дата рождения')
    city = models.CharField('Город', max_length=20)

    def __str__(self):
        return f"{self.phone} - {self.firstName} - {self.city}"

    class Meta:
        verbose_name = "Клиента"
        verbose_name_plural = "Клиенты"


class Order(models.Model):
    id = models.AutoField('ID', primary_key=True)
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
    orderComposition = models.TextField('Состав заказа')
    time = models.DateTimeField('Время заказа')
    status = models.CharField('Статус заказа', max_length=10, default=None)
    amount = models.IntegerField('Сумма', default=None)

    def __str__(self):
        return f"Заказ #{self.id}  Клиент: {self.client.phone}  Статус: {self.status}"

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"


class Category(models.Model):
    id = models.AutoField('ID',primary_key=True)
    category = models.CharField('Категория', max_length=30)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = "Категорию"
        verbose_name_plural = "Категории"


class Pizza(models.Model):
    id = models.AutoField('ID', primary_key=True)
    category = models.ManyToManyField(Category)
    city = models.CharField("Город", max_length=20, default=None)
    tittle = models.CharField('Название', max_length=20, default=None)
    description = models.TextField('Описание', default=None)
    cost = models.IntegerField("Стоимость", default=None)
    sale = models.BooleanField("По скидке?",default=False)
    img = models.ImageField("Картинка", upload_to="pizzas", blank=True, null=True)
    weight = models.FloatField("Вес", null=True, blank=True)
    protein = models.FloatField('Белки', null=True, blank=True)
    fats = models.FloatField("Жиры", null=True, blank=True)
    carbon = models.FloatField("Углеводы", null=True, blank=True)
    calories = models.FloatField("Ккал", null=True, blank=True)

    def __str__(self):
        return self.tittle

    class Meta:
        verbose_name = "Пиццу"
        verbose_name_plural = "Пиццы"

