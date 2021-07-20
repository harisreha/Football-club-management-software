from django.db import models
from django.utils.timezone import now
from datetime import datetime

import datetime

# Create your models here.
class Prihod(models.Model):
    Naziv_lica = models.CharField(max_length=100)
    Tip_Uplate = models.CharField(max_length=200)
    Datum_uplate = models.DateField(default=now, editable=False)
    Cijena = models.IntegerField()

    def __str__(self):
        return self.Tip_Uplate
    
class Rashod(models.Model):
    Naziv_lica = models.CharField(max_length=100)
    Tip_Uplate = models.CharField(max_length=200)
    Datum_uplate = models.DateField(default=now, editable=False)
    Cijena = models.IntegerField()

    def __str__(self):
        return self.Tip_Uplate


class Sponzors(models.Model):
    name = models.CharField(max_length=200)
    Tip_Sponzorstva = models.CharField(max_length=200)
    Cijena_sponzorstva = models.IntegerField()

    def __str__(self):
        return self.name

class Players(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    datumRodj = models.DateField()
    email = models.CharField(max_length=200)
    ugovorVazi = models.DateField()
    pozicija = models.CharField(max_length=200, null=True ,blank=True)
    plata = models.IntegerField()

    def __str__(self):
        return self.name

class Members(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    godina = models.IntegerField()
    datumUclanjenja = models.DateField(default=now, editable=False)
    email = models.CharField(max_length=200)
    datumVazi = models.DateField()
    

    def __str__(self):
        return self.name
class Staff(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    datumUposlenja = models.DateField(default=now, editable=False)
    email = models.CharField(max_length=200)
    datumIstekaUgovora = models.DateField()
    pozicijaa = models.CharField(max_length=200, null=True,blank=True)
    plata = models.IntegerField()
    
    def __str__(self):
        return self.name

class Track(models.Model):
    user = models.CharField(max_length=200)
    modul = models.CharField(max_length=200)
    datumIzmjene = models.DateTimeField(default=now, editable=False)
    tipPromjene = models.CharField(max_length=200)
    

    def __str__(self):
        return self.name
        
    @property
    def delete_after(self):
        if self.datumIzmjene < datetime.datetime.now()-datetime.timedelta(days=7):
            e = Track.objects.get(pk=self.pk)
            e.delete()
            return True
        else:
            return False
