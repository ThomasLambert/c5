# -*- coding: utf-8 -*- 
from django.db import models
from c5.dict.base12 import *
from pcsets import pcset
import string

#§%

class Shape(models.Model):
	rname = models.CharField(max_length=100)

def c5_form(pcset):
    """ Function that finds the prime c5 form of a shape
    A prime c5 form is more compact way of expressing the chord in the circle : the interval of fifth is favored """
    [doz(i) % 5 for i in list(pcset)]


class Reading(models.Model):
    """ Reading est une interpretation d'une shape. Ex : "Accord mineur" """
    def __unicode__(self):
        return self.rname
#    rname = models.CharField(max_length=100)
#    rtype = models.CharField(max_length=10)
#    fondamental = models.IntegerField()
    pcset = models.CharField(max_length=12)
#    shape = models.ForeignKey(Shape)
#    created = models.DateTimeField('Date de creation')


class Voicing(models.Model):
    pcset = models.CharField(max_length=12)
# Il faudrait declarer les fonctions relatives au voicings ici, de facon à se préparer a eventuellement avoir un autre instrument (ex : guitare accordée en open)


class GtrVoicing(Voicing):
    def __unicode__(self):
        return str(s1)+str(s2)+str(s3)+str(s4)+str(s5)+str(s6)
    def instrument(self):
	return "gtr"
# Je suis pas sur si on stock chaque corde separement, ou plutot un champ "string"
    s1 = models.IntegerField()
    s2 = models.IntegerField()
    s3 = models.IntegerField()
    s4 = models.IntegerField()
    s5 = models.IntegerField()
    s6 = models.IntegerField()

