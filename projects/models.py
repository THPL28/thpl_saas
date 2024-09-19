from django.db import models

if False:
    class Project(models.Model):

        name = models.CharField(max_length=100)

        description = models.TextField()

        def __str__(self):

            return self.name
        

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
