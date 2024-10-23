from django.db import models


class Produs(models.Model):
    objects = None
    denumire = models.CharField(max_length=100)
    cantitate = models.CharField(max_length=50)
    pret_studenti = models.DecimalField(max_digits=5, decimal_places=2)
    imagine = models.ImageField(upload_to='produse/', null=True, blank=True)

    def __str__(self):
        return self.denumire
