from django.db import models


class Item(models.Model):

	def __str__(self):
		return self.name

	name = models.CharField(max_length=200)
	description = models.CharField(max_length=200)
	price = models.IntegerField()

