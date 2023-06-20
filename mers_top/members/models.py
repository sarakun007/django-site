from django.db import models

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  content=models.TextField(blank=True)
  phone = models.IntegerField(null=True)
  joined_date = models.DateField(null=True)
  photo = models.ImageField(upload_to='images/', blank=True, null=True)


  def __str__(self):
    return f"{self.firstname} {self.lastname}"

class Pictures(models.Model):
  onlyphoto = models.ImageField(upload_to='images/', blank=True, null=True)

  def __str__(self):
    return self.onlyphoto.name