from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, blank=False, null=False)
    tags = models.ManyToManyField('Tag', blank=True)
    
    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=500)
	
    def __str__(self):
        return self.name

class Tag(models.Model):
	name = models.CharField(max_length=100)
	
	def __str__(self):
		return self.name