from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class AirCategory(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    aircategory = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="aircategory")


    def __str__(self):
        return self.name


class Tour(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='product_images', null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    
    

    def __str__(self):
        return self.name



