from django.db import models

# Create your models here.
class place(models.Model):
    img = models.ImageField(upload_to='inmakesproject')
    name=models.CharField(max_length=250)

    desc=models.TextField()

    def __str__(self):
        return self.name

# class person(models.Model):
#     name1=models.CharField(max_length=250)
#     img1=models.ImageField(upload_to='inmakesproject')
#     desc1=models.TextField()
#
#     def __str__(self):
#         return self.name1