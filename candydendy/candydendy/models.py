from django.db import models

class Candy(models.Model):
    name = models.CharField(max_length=256)
    company = models.CharField(max_length=256)
    company_country = models.CharField(max_length=64)
    company_address = models.CharField(max_length=256)
    company_site = models.URLField(max_length=64)
    company_email = models.EmailField(max_length=256)
    # company_phone_number = PhoneNumberField(null=False, blank=False)
    company_phone_number = models.CharField(max_length=64)
    company_director = models.CharField(max_length=256)
    pricetag = models.CharField(max_length=64)
    fats = models.IntegerField()
    carbohydrates = models.IntegerField()
    protein = models.IntegerField()
    calories = models.IntegerField()
    type = models.CharField(max_length=256)
    rating = models.BigIntegerField()

    def __str__(self):
        return self.name
