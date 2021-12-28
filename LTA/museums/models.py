from django.db import models


class Museums(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    price = models.IntegerField()
    img_url = models.CharField(max_length=200)
    start_work_hour = models.CharField(max_length=10)
    end_work_hour = models.CharField(max_length=10)
    description = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    phone_number = models.CharField(max_length=80)
    category = models.IntegerField(null=True)

    def __str__(self):
        return self.name
