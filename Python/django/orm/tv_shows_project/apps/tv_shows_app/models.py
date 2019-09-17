from django.db import models

# starter test data: 
#  brook = Tv_show.objects.create(title="Brooklyn 99", description="funny police show", network="NBC", release_date=datetime.date(2013, 9, 17))
#  pr = Tv_show.objects.create(title="Parks and Recreation", description="funny civil servant show", network="NBC", release_date=datetime.date(2009, 4, 9))

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['tv_show_title']) < 2:
            errors["title"] = "TV Show title should be at least 2 characters"
        if len(postData['tv_show_network']) < 3:
            errors["network"] = "TV Show network should be at least 3 characters"
        if postData['description'] and len(postData['description']) < 10:
            errors["description"] = "TV Show descriptions should be longer than 10 characters, if it exists at all"
        if not postData['tv_show_relase_date']:
            errors["tv_show_release_date"] = "TV Show release date should exist"
        return errors



class Tv_show(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateTimeField(auto_now_add=True)
    network = models.CharField(max_length=255)
    description = models.TextField()
    objects = ShowManager()
    def __repr__(self):
        return f"<TV SHOW object: {self.title}, description: {self.description} {self.release_date}>"

