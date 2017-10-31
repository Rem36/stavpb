from django.db import models
from django.utils import timezone
from django.forms import ModelForm

PRODUCT_QUANTITY_CHOICES = (
		(1, "1 otd"),
		(2, "2 otd"),
	)

class Post(models.Model):
	title = models.CharField(max_length=200)
	otd = models.IntegerField(choices=PRODUCT_QUANTITY_CHOICES)
	fio = models.CharField(max_length=50)
	text = models.TextField(default="")
	status = models.CharField(max_length=20, default="В стадии выполнения")
	ispolnitel = models.CharField(max_length=30)
	date_pub = models.DateTimeField(blank=True, null=True)
	date_comp = models.DateTimeField(blank=True, null=True)

	def pub(self):
		self.date_pub = timezone.now()
		self.save()

	def __str__(self):
		return self.title