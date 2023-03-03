from django.db import models

class Todo(models.Model):
	title=models.CharField(max_length=150)
	description=models.CharField(max_length=500)
	completed=models.BooleanField(default=False)

	# string representation of the class
	def __str__(self):

		#it will return the title
		return self.title



class Researcher(models.Model):
    fullname = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    phone = models.CharField(max_length=20)

class User(models.Model):
    ResearcherId = models.ForeignKey('Researcher', on_delete=models.PROTECT, null=True)
    fullname = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    education = models.CharField(max_length=50)
    sport = models.CharField(max_length=20)
    datebirth = models.DateField()
    datelasttest = models.DateField()

class Result(models.Model):
    UserId = models.ForeignKey('User', on_delete=models.PROTECT, null=True)
    date_start = models.DateField()
    date_end = models.DateField()
    time1 = models.IntegerField()
    time2 = models.IntegerField()
    time3 = models.IntegerField()
    time4 = models.IntegerField()