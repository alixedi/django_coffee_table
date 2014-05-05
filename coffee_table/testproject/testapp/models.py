from django.db import models



class Medium(models.Model):
	name = models.CharField(max_length=32)

	def __unicode__(self):
		return self.name


class StarWar(models.Model):
	name = models.CharField(max_length=32)
	medium = models.ForeignKey(Medium)

	def __unicode__(self):
		return self.name