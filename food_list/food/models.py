from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Item(models.Model):

	def __str__(self):
		return self.name

	name = models.CharField(max_length=200)
	description = models.CharField(max_length=200)
	price = models.IntegerField()
	# will use charfield to store the image so I don't have to save the actual image on my server
	# I'm aware that on real life projects this is not I'll be doing
	image = models.CharField(
		max_length=500,
		default="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQipEtiHLzPkCFMzLEqzlkXcAb-R3Y92AE_cXZAO1VBiP4NhJrldG718z8k1MSoe6xU7zo&usqp=CAU"
	)
	user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

	def get_absolute_url(self):
		return reverse("food:detail", kwargs={"pk": self.pk})
