from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = models.TextField(blank=True, verbose_name="Описание")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
    available = models.BooleanField(default=True, verbose_name="Наличие")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Категории")
    on_stock = models.CharField(max_length=255, verbose_name="Доступное количество")
    price = models.CharField(max_length=10, verbose_name="Цена")
    transaction = models.ForeignKey('Transaction', on_delete=models.PROTECT, verbose_name='транзакция')

    def __str__(self):
        return self.title


class Transaction(models.Model):
    from_where = models.CharField(max_length=50, verbose_name="от куда")
    to_where = models.CharField(max_length=50, verbose_name="куда")
    status = models.BooleanField(default=True, verbose_name="Статус отправки")
    how_many = models.CharField(max_length=50, verbose_name="Колличество")
    buyer = models.CharField(max_length=255, verbose_name="Покупатель")
    is_paid = models.BooleanField(default=False, verbose_name="Статус оплаты")


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категория")

    def __str__(self):
        return self.name