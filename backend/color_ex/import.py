import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'color_ex.settings')


import django
django.setup()

from colors import models
from constants import questions


def main():
    experiment, _ = models.Experiment.objects.get_or_create(name='colors')
    for question, answers in questions.items():
        correct_answer, _ = models.Answer.objects.get_or_create(text=answers['correct'])
        incorrect_answer, _ = models.Answer.objects.get_or_create(text=answers['incorrect'])
        models.Question.objects.update_or_create(
            text=question,
            defaults={
                'experiment': experiment,
                'correct_answer': correct_answer,
                'incorrect_answer': incorrect_answer,
            }
        )



if __name__ == "__main__":
    main()