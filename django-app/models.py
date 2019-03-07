from django.db import models

# Create your models here.

class Category_1(models.Model):
	# 風雅頌之別
	name = models.CharField(max_length=5)
	def __str__(self):
		return self.name

class Category_2(models.Model):
	# 風則國別，雅頌則什，區以別之
	name = models.CharField(max_length=10)
	def __str__(self):
		return self.name

class Title(models.Model):
	# 詩題
	c1 = models.ForeignKey(Category_1, on_delete=models.CASCADE)
	c2 = models.ForeignKey(Category_2, on_delete=models.CASCADE)
	name = models.CharField(max_length=10)
	def __str__(self):
		return self.name

class Song(models.Model):
	# 詩，別之以章
	t = models.ForeignKey(Title, on_delete=models.CASCADE)
	name = models.CharField(max_length=200)
	def __str__(self):
		return self.name
