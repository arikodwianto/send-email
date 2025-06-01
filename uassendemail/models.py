from django.db import models

class Guest(models.Model):
   nim = models.CharField(max_length=10)
   nama = models.CharField(max_length=100)
   email = models.EmailField(max_length=100, default='default@example.com')
   kegiatan = models.TextField()
   def __str__(self):
    return self.nim
