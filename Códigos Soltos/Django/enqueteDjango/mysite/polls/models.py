import datetime

from django.db import models
from django.utils import timezone
# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200) #Charfield permite a entrada de String(textos) com no max. 200 carac.
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)#apaga as alternativas vinculadas a pergunta
    choice_text = models.CharField(max_length=100)
    votes = models.IntegerField(default=0) #campo de inteiros, um campo de num. inteiros iniciando em 0

    def __str__(self):
        return self.choice_text