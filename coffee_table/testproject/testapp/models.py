from django.db import models



class Medium(models.Model):
	"""
	Medium includes TV, Movie, Comic Book etc.
	"""
	name = models.CharField(max_length=32, help_text='Name of Medium')

	def __unicode__(self):
		return self.name


class StarWar(models.Model):
	"""
	StarWar merchandise - anything and everything from TV series to movies
	to comic books.
	"""
	name = models.CharField(max_length=32, help_text='Name of Release')
	medium = models.ForeignKey(Medium, help_text='Medium of Release')

	def __unicode__(self):
		return self.name
