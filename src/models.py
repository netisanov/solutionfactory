from django.db import models
from django.urls import reverse
from datetime import datetime, timedelta, date


class BaseModel(models.Model):
    created_at = models.DateTimeField(db_index=True, auto_now_add=True)

    class Meta:
        abstract = True


class Quiz(BaseModel):
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(default=date.today() + timedelta(days=5))
    quiz_title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    question_title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    choice_title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class AnswerList(BaseModel):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='answer_lists')


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE, related_name='answers')
    answer_list = models.ForeignKey(AnswerList, on_delete=models.CASCADE, related_name='answers')

