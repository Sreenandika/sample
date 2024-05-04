from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name



class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=100)
   

    def __str__(self):
        return self.name
    
class ProductVarient(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True,blank=True)
    size = models.CharField(max_length=100)
    actualprice=models.CharField(max_length=20)
    discountprice=models.CharField(max_length=30)
    
