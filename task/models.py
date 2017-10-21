from django.db import models
from django.conf import settings

class Profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	date_of_birth = models.DateField(blank=True,null=True)
	photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)
	
	def __str__(self):
		return 'User profile {}.'.format(self.user.username)

class Material(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=250)
	description = models.CharField(max_length=250)
	notes = models.CharField(max_length=250)
	supplier = models.CharField(choices=(("Tire Systems", ("Tire Systems")),
                                        ("IT Enterprise", ("IT Enterprise")),
                                        ("Car Manufacture", ("Car Manufacture")),
                                        ("Electro Market", ("Electro Market")),
                                        ),
                                default="Tire Systems",max_length=250)
	price = models.DecimalField(max_digits=10, decimal_places=2,null=True)
	currency = models.CharField(choices=((" U.S. Dollar", (" U.S. Dollar")),
                                        ("EUR", ("EUR")),
                                        ("YEN", ("YEN")),
										 ("PLN", ("PLN")),
                                        ("GBP", ("GBP")),
                                        ),
                                default="Tire Systems",max_length=250)