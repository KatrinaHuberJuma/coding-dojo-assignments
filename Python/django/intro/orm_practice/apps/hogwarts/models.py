from django.db import models

# Create your models here.
class Hogwarts(models.Model):
    name = models.CharField(max_length=45)
    house = models.CharField(max_length=45)
    pet = models.CharField(max_length=45)
    year = models.IntegerField()
    def __repr__(self):
        return f"<User object: {self.name} {self.house}, pet = {self.pet}, year {self.year}, id = {self.id}>"

# class Users(models.Model):
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     email_address = models.CharField(max_length=255)
#     age = models.IntegerField()
#     def __repr__(self):
#         return f"<User object: {self.first_name} {self.last_name}({self.email_address})>"
