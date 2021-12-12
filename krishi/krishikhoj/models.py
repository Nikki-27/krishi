from django.db import models



# Create your models here.
class info(models.Model):
    name = models.CharField(max_length=1000000)
    phone = models.CharField(max_length=10)
    city = models.CharField(max_length=10000)
    state = models.CharField(max_length=100000)
    zip = models.CharField(max_length=10000)
    ntractor = models.IntegerField()
    implements = models.CharField(max_length=10000)

    def __str__(self) -> str:
        return self.name

