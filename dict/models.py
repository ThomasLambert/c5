from django.db import models

# Create your models here.

class Cycle(models.Model):
    def __unicode__(self):
        return self.cycle
    n1 = models.IntegerField()
    n2 = models.IntegerField()




class Reading(models.Model):
  #  def __unicode__(self):
   #     return self.reading
    rname = models.CharField(max_length=100)
    rtype = models.CharField(max_length=10)
    fondamental = models.IntegerField()
    cycle = models.ForeignKey(Cycle)
    created = models.DateTimeField('Date de creation')


class GtrVoicing(models.Model):
   # def __unicode__(self):
    #    return self.gtrvoicing
    cycle = models.ForeignKey(Cycle)
    s1 = models.IntegerField()
    s2 = models.IntegerField()
    s3 = models.IntegerField()
    s4 = models.IntegerField()
    s5 = models.IntegerField()
    s6 = models.IntegerField()

class Test(models.Model):
	rname = models.CharField(max_length=100)
