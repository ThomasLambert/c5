from django.db import models

class Shape(models.Model):
# Une shape est un dessin sur le cercle, soit groupe de notes
    def __unicode__(self):
        return self.shape_id
    shape_id = models.TextField(primary_key=True)
# shape_id représente les intervals : il sera en base-12, un chiffre par note.
# Pour s'assurer qu'il n'y ai pas de doublons, on devra probablement toujours le transformer en sa "prime form"



class Reading(models.Model):
# Reading est une interprétation d'une shape. Ex : "Accord mineur"
    def __unicode__(self):
        return self.rname
    rname = models.CharField(max_length=100)
    rtype = models.CharField(max_length=10)
    fondamental = models.IntegerField()
    shape = models.ForeignKey(Shape)
    created = models.DateTimeField('Date de creation')


class Voicing(models.Model):
    shape = models.ForeignKey(Shape)
# Il faudrait déclarer les fonctions relatives au voicings ici, de facon à se préparer à éventuellement avoir un autre instrument (ex : guitare accordé en open)


class GtrVoicing(Voicing):
# Je suis pas sur si on stock chaque corde séparément, ou plutot un champ "string"
    s1 = models.IntegerField()
    s2 = models.IntegerField()
    s3 = models.IntegerField()
    s4 = models.IntegerField()
    s5 = models.IntegerField()
    s6 = models.IntegerField()

