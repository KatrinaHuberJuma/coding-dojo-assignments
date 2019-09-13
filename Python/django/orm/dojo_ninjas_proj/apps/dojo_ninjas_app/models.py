from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    desc = models.CharField(max_length=255)
    def __repr__(self):
        return f"<Dojo object: {self.name}, city: {self.city}, state = {self.state}, id = {self.id}>"

class Ninja(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dojo = models.ForeignKey(Dojo, related_name="ninjas")
    def __repr__(self):
        return f"<Ninja object: {self.first_name} {self.last_name}(from the {self.dojo.name} dojo)>"

