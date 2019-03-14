from django.db import models
from django.utils import timezone

# Create your models here.
class Moderator(models.Model):
  mod_id = models.AutoField(primary_key=True)
  email = models.CharField(max_length=50)
  username = models.CharField(max_length=50)
  password = models.CharField(max_length=50)
  age = models.IntegerField()
  university = models.CharField(max_length=100)
  department = models.CharField(max_length=50)
  created = models.DateTimeField("Created on", default=timezone.now())
  subforum_id = models.IntegerField()

  def __str__(self):
    return self.username

class Subforum(models.Model):
  subforum_id = models.AutoField(primary_key=True)
  subforum_name = models.CharField(max_length=50)
  subforum_description = models.TextField(blank=True, null=True)
  ques_count = models.IntegerField(default=0)
  mod_id = models.ManyToManyField(Moderator, blank=True, related_name='moderator')

  def __str__(self):
    return f"{self.subforum_id} {self.subforum_name}"

class User(models.Model):
  user_id = models.AutoField(primary_key=True)
  email = models.CharField(max_length=50)
  username = models.CharField(max_length=50)
  password = models.CharField(max_length=50)
  age = models.IntegerField()
  university = models.CharField(max_length=100)
  department = models.CharField(max_length=50)
  created = models.DateTimeField("Created on", default=timezone.now())
  
  def __str__(self):
    return self.username
 
 
class Question(models.Model):
  ques_id = models.AutoField(primary_key=True)
  user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_question')
  subforum_id = models.ForeignKey(Subforum, on_delete=models.CASCADE, related_name='subforum_question')
  ques_text = models.TextField()

class Answer(models.Model):
  ans_id = models.AutoField(primary_key=True)
  user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_answer')
  subforum_id = models.ForeignKey(Subforum, on_delete=models.CASCADE, related_name='subforum_answer')
  ans_text = models.TextField()

class Comment(models.Model):
  comment_id = models.AutoField(primary_key=True)
  user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comment')
  subforum_id = models.ForeignKey(Subforum, on_delete=models.CASCADE, related_name='subforum_comment')
  comment_text = models.TextField()    