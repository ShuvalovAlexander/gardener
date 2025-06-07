from django.db import models

class Product(models.Model):
    title = models.CharField("Название", max_length=255)
    description = models.TextField("Описание")
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    old_price = models.DecimalField("Старая цена", max_digits=10, decimal_places=2, blank=True, null=True)
    image = models.ImageField("Основное изображение", upload_to="products/")
    additional_image = models.ImageField("Дополнительное изображение", upload_to="products/", blank=True, null=True)
    characteristics = models.TextField("Характеристики", blank=True)

    def __str__(self):
        return self.title


from django.db import models

class Feedback(models.Model):
    name = models.CharField("Имя", max_length=100)
    phone = models.CharField("Телефон", max_length=20)
    agree = models.BooleanField("Согласие", default=False)

    def __str__(self):
        return f"{self.name} - {self.phone}"


class Order(models.Model):
    product = models.CharField("Товар", max_length=255)
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    email = models.EmailField("Email")
    phone = models.CharField("Телефон", max_length=20)
    address = models.TextField("Адрес доставки")
    comment = models.TextField("Комментарий", blank=True)
    created_at = models.DateTimeField("Дата заказа", auto_now_add=True)

    def __str__(self):
        return f"Заказ: {self.product} — {self.email}"