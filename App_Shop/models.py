from django.db import models
#from App_Login.models import Profile
# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Categories"

class Product(models.Model):
    mainimage = models.ImageField(upload_to='Products')
    name = models.CharField(max_length=264)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    preview_text = models.TextField(max_length=200, verbose_name='Preview Text')
    detail_text = models.TextField(max_length=1000, verbose_name='Description')
    price = models.FloatField()
    old_price = models.FloatField(default=0.00)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created',]

'''
class ReviewRating(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(Profile,on_delete=models.CASCADE)
    subject = models.CharField(max_length=100,blank=True)
    review = models.TextField(max_length=500,blank=True)
    rating = models.FloatField()
    ip = models.CharField(max_length=20,blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.subject
'''
