from django.db import models

# starter test data: 
#  brook = Tv_show.objects.create(title="Brooklyn 99", description="funny police show", network="NBC", release_date=datetime.date(2013, 9, 17))
#  pr = Tv_show.objects.create(title="Parks and Recreation", description="funny civil servant show", network="NBC", release_date=datetime.date(2009, 4, 9))

class Tv_show(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateTimeField(auto_now_add=True)
    network = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    def __repr__(self):
        return f"<TV SHOW object: {self.title}, description: {self.description} {self.release_date}>"
