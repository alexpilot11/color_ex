from django.db import models
from django.utils.translation import gettext_lazy as _


class Color(models.TextChoices):
    RED = 'r', _('Red')
    BLUE = 'b', _('Blue')
    WHITE = 'w', _('White')


class Experiment(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Answer(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text


class Question(models.Model):
    text = models.TextField()
    experiment = models.ForeignKey(Experiment, on_delete=models.PROTECT)
    correct_answer = models.OneToOneField(Answer, on_delete=models.PROTECT, related_name='correct_questions')
    incorrect_answer = models.OneToOneField(Answer, on_delete=models.PROTECT, related_name='incorrect_questions')

    def __str__(self):
        return self.text


class Test(models.Model):
    experiment = models.ForeignKey(Experiment, on_delete=models.PROTECT)

    def __str__(self):
        return f'Test {self.pk} for {self.experiment.name}'


class TestAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.PROTECT)
    color = models.CharField(max_length=1, choices=Color.choices)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
