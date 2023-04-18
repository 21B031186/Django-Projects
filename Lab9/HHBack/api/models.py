from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    city = models.CharField(max_length=50)
    address = models.TextField()
    test = models.TextField(null=True)


    def __str__(self) ->str:
        return f'{self.name}'

class Vacancy(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    salary = models.FloatField()
    company = models.ForeignKey(to=Company, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'