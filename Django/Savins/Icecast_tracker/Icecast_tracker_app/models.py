from django.db import models

class Channel(models.Model):
	name = models.CharField(max_length=200)
	def __str__(self):
		return self.name

class Server(models.Model):
	name = models.CharField(max_length=200)
	ip = models.CharField(max_length=50)
	port = models.IntegerField()
	def __str__(self):
		return self.name + " (" + self.ip + ":" + str(self.port) + ")"

class Route(models.Model):
	channel = models.ForeignKey(Channel)
	server = models.ForeignKey(Server)
	path = models.CharField(max_length=200)
	def __str__(self):
		return str(self.server) +", " + str(self.channel) + " /" + self.path
