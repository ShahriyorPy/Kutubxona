from django.db import models
from django.contrib.auth.models import User
# Create your models here.

T = (
    (1,1),
    (2,2),
    (3,3),
    (4,4)
)

class Talaba(models.Model):
    ism = models.CharField(max_length=50)
    kurs = models.PositiveSmallIntegerField(choices=T)
    yosh = models.PositiveSmallIntegerField(null=True,blank=True)
    kitob_soni = models.PositiveSmallIntegerField(default=0)
    universitet = models.CharField(max_length=50,null=True,blank=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.ism

class Kutubxonachi(models.Model):
    ism = models.CharField(max_length=50)
    ish_vaqti = models.CharField(max_length=20)

    def __str__(self):
        return self.ism

J = (
    ('erkak','erkak'),
    ('ayol','ayol')
)

class Muallif(models.Model):
    ism = models.CharField(max_length=30)
    tugilgan_yil = models.PositiveSmallIntegerField()
    tirik = models.BooleanField(default=False)
    kitoblari_soni = models.PositiveSmallIntegerField()
    jinsi = models.CharField(max_length=15,choices=J)

    def __str__(self):
        return self.ism

Janr = (
    ('badiiy','badiiy'),
    ('ilmiy','ilmiy')
)

class Kitob(models.Model):
    nom = models.CharField(max_length=30)
    muallif = models.ForeignKey(Muallif,on_delete=models.CASCADE)
    sahifa = models.PositiveSmallIntegerField()
    janr = models.CharField(max_length=30,choices=Janr)

    def __str__(self):
        return self.nom

class Record(models.Model):
    talaba = models.ForeignKey(Talaba,on_delete=models.CASCADE)
    kitob = models.ForeignKey(Kitob,on_delete=models.CASCADE)
    kutubxonachi = models.ForeignKey(Kutubxonachi,models.CASCADE)
    olingan_sana = models.DateField()
    qaytardi = models.BooleanField(default=False)
    qaytarish_sanasi = models.DateField(null=True,blank=True)

