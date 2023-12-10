
from django.db import models
from django.contrib.auth.models import User
class Post(models.Model):
    title = models.CharField(max_length=255)
    mota = models.TextField(blank=True)
    text_url = models.TextField(blank = True)
    def __str__(self):
        return f"{self.title} - {self.mota} - {self.text_url}"


class Food(models.Model):
    title = models.CharField(max_length=255)
    mota = models.TextField(blank=True)
    text_url = models.TextField(blank = True)
    def __str__(self):
        return f"{self.title} - {self.mota} - {self.text_url}"
class Product(models.Model):
    title = models.CharField(max_length=255)
    khoihanh = models.CharField(max_length=50)
    isHot = models.BooleanField(default=False)
    thoigian = models.IntegerField()
    diadiem = models.CharField(max_length=100)
    lichtrinh = models.TextField(blank=True)
    gia = models.IntegerField()
    giachuasale = models.IntegerField()
    text_url = models.TextField(blank=True)
    soluoc = models.TextField(blank=True)
    trainghiem = models.TextField(blank=True)
    chuongtrinhtour = models.TextField(blank=True)
class Blog(models.Model):
    title = models.CharField(max_length=255)
    text_url = models.TextField(blank=True)

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    sdt = models.CharField(max_length=20, blank=True, null=True)
    
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    complete = models.BooleanField(default=False, null=True, blank=False)

    def tinh_tong_don_hang(self):
        total = 0
        order_items = self.orderitem_set.all()

        for item in order_items:
            total += item.tinh_tong()

        return total

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    
    def tinhTong(self):
        return self.product.gia * self.quantity
    def tinh_tong(self):
        if self.product is not None and self.quantity is not None:
            return self.product.gia * self.quantity
        return 0
    
class Accommodation(models.Model):
    name = models.CharField(max_length=255)
    gia = models.IntegerField(default=0, null=True, blank=True)
    vitri = models.CharField(max_length=255)
    text_url = models.TextField(blank=True)



