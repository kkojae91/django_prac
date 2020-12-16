from django.db import models

# Create your models here.

class AiClass(models.Model):
  class_num = models.IntegerField()
  lecturer = models.CharField(max_length=30)
  class_room = models.CharField(max_length=30)
  students_num = models.IntegerField()
  class Meta:
    verbose_name_plural = 'AiClass'

class AiStudents(models.Model):
  name = models.CharField(max_length=30)
  class_num = models.IntegerField()
  phone_num = models.CharField(max_length=30)
  intro_text = models.TextField()
  class Meta:
    verbose_name_plural = "AiStudents"