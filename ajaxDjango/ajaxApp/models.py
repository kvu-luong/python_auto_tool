from django.db import models

# Create your models here.
class Friend(models.Model):
	nick_name = models.CharField(max_length = 100, unique = True)
	first_name = models.CharField(max_length = 100)
	last_name = models.CharField(max_length = 100)
	likes = models.CharField(max_length = 250)
	dob = models.DateField(auto_now = False, auto_now_add = False)
	lives_in = models.CharField(max_length = 150, null = True, blank = True)

	def __str__(self):
		return self.nick_name

class Crawl(models.Model):
	web_site = models.CharField(max_length=500, unique = True)
	block = models.CharField(max_length = 250)

	def __str__(self):
		return self.web_site