from django.db import models

# Create your models here.
class bookshop(models.Model):
    name = models.CharField(max_length=30)
    author = models.CharField(max_length=40)
    # def __str__(self):  
    #     return self.name, self.author

class Item_list(models.Model):
    book_list = ["Not Even Wrong","Classical Physics","Indian Economics",]
    student_list = ["Harish", "Suresh", "Ganesh", "Gukesh",]
    fruit_list = ["Mango","Guavaa","JackFruit","Orange","Banana",]