from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=100, default='')
    slug = models.CharField(max_length=100, default='')
    # mô tả
    description = models.TextField(default='')
    # trạng thái BooleanField(default=True) có nghĩa là được active
    active = models.BooleanField(default=True)


class Product(models.Model):
    title = models.CharField(max_length=255, default='')
    description = models.TextField(default='')
    # Vì liên kết vơi Category
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_img = models.CharField(max_length=255, default='')
    price = models.IntegerField(default=0)
    active = models.BooleanField(default=True)


class Variation(models.Model):
    # Vì liên kết với Product
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, default='')
    price = models.IntegerField(default=0)
    sale_price = models.IntegerField(default=0)
    # hàng tồn kho
    inventory = models.BooleanField(default=0)
    active = models.BooleanField(default=True)

