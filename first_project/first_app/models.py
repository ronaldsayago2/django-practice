from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
	topic_name = models.CharField(max_length=264, unique=True)
	
	def __str__(self):
		return self.topic_name 
	
	
class Webpage(models.Model):
	topic = models.ForeignKey(
		Topic, 
		on_delete=models.DO_NOTHING,
		related_name='webpages'
	)
	name = models.CharField(max_length=264, unique=True)
	url = models.URLField(unique=True)
	
	def __str__(self):
		return self.name 

	
class AccessRecord(models.Model):
	name = models.ForeignKey(
		Webpage, 
		on_delete=models.DO_NOTHING,
		related_name='access_records'
	)
	date = models.DateField()
	
	def __str__(self):
		return str(self.date)


class Users(models.Model):
    firstname = models.CharField(max_length = 250)
    lastname = models.CharField(max_length = 250)
    email = models.EmailField(max_length = 260)
    
    def __str__(self):
        return str(self.firstname) + ' ' + str(self.lastname)
    
    

class WebUsers(models.Model):
    user = models.OneToOneField(User, on_delete = models.DO_NOTHING)
    portfolio = models.URLField(blank = True)
    picture = models.ImageField(upload_to = 'profile', blank = True)
    
    
    
    def __str__(self):
        return self.user.username
    
    