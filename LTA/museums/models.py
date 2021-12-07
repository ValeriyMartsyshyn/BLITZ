from django.db import models


class Museums(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    price = models.IntegerField()
    img_url = models.CharField(max_length=200)
    start_work_hour = models.IntegerField()
    end_work_hour = models.IntegerField()
    description = models.TextField()
    rating = models.IntegerField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name




