from django.contrib import admin

from . import models

# Register your models here.

@admin.register(models.Experiment)
class ExperimentAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Answer)
class AnswerAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Test)
class TestAdmin(admin.ModelAdmin):
    pass

@admin.register(models.TestAnswer)
class TestAnswerAdmin(admin.ModelAdmin):
    pass