from django.db import models 

# Create your models here.



UNIT_CHOICES = [
        ('Harrow', 'Harrow'),
        ('Cultivator', 'Cultivator'),
        ( 'Rotavator' , 'Rotavator'),
        ('Plough' ,'Plough'),
        ('Paddy Thrasher' ,'Paddy Thrasher'),
        ('Dumping Trailer' ,'Dumping Trailer' ),
        ('4 wheel Trailer' ,'4 wheel Trailer')
    ]
        
class Farm(models.Model):
    name =models.CharField(max_length=70)
    email = models.EmailField(max_length=50)
    phone = models.IntegerField()
    tractor_brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    tractor_implements = models.CharField(choices=UNIT_CHOICES, max_length=50)