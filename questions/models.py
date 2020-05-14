from django.db import models
from users.models import User
from datetime import datetime


class Question(models.Model):
    title = models.CharField(max_length=1000)
    title_image = models.ImageField(default=None, upload_to='question_pics')
    topics = models.CharField()  # TODO: This should be choices or list field
    subject = models.CharField()  # TODO: This should be choices too or list field
    difficulty_level = models.IntegerField()
    subm_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(default=datetime.utcnow())
    updt_ts = models.DateTimeField(default=datetime.utcnow())

# Create your models here.
class SingleChoiceQuestion(Question):
    option_1 = models.CharField(max_length=1000)
    option_1_image = models.ImageField(default=None, upload_to='question_pics')
    option_2 = models.CharField(max_length=1000)
    option_2_image = models.ImageField(default=None, upload_to='question_pics')
    option_3 = models.CharField(max_length=1000)
    option_3_image = models.ImageField(default=None, upload_to='question_pics')
    option_4 = models.CharField(max_length=1000)
    option_4_image = models.ImageField(default=None, upload_to='question_pics')
    answer = models.IntegerField()
    category = models.CharField(default='single_choice')

class MultipleChoiceQuestion(Question):
    pass


class SubjectiveQuestion(Question):
    pass

