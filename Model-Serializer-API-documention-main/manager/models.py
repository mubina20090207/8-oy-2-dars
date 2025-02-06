from django.db import models


class Klass(models.Model):
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Hotel(models.Model):
    name = models.CharField(max_length=150)
    star_count = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Travel(models.Model):
    name = models.CharField(max_length=150)
    comment = models.TextField(null=True, blank=True)
    deadline = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    klass = models.ForeignKey(Klass, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)

    def __str__(self):
        return self.name