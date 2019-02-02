from django.db import models

# Create your models here.
# model is a class inside of the models module ????
# creating a table name item where the objects will have to values name and done
# all objets created in Item table will have this structure
#the boolean will help us interact whit the item later on 
class Item(models.Model):
    name = models.CharField(max_length=30, blank=False)
    done = models.BooleanField(blank=False, default=False)
    def __str__(self):
        return self.name