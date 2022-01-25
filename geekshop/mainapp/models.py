from django.db import models

class ProductCategory(models.Model):
    name = models.CharField(verbose_name='название категории', max_length=50, unique=True)
    description = models.TextField(verbose_name='описание категории', blank=True)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='название товара', max_length=128)
    price = models.DecimalField(verbose_name='цена товара', max_digits=8, decimal_places=2, default=0)
    colour = models.PositiveIntegerField(verbose_name='цвет товара', default=0x000000)
    image = models.ImageField(verbose_name='изображение товара', upload_to='products_images', blank=True)
    description = models.TextField(verbose_name='описание товара', blank=True)
    quantity = models.PositiveIntegerField(verbose_name='количество в наличии', default=0)

    def __str__(self):
        return self.name
