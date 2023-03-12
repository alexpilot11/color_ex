from rest_framework import serializers

from colors import models


class ExperimentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Experiment
        fields = [
            'name',
        ]


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Answer
        fields = [
            'text',
        ]


class QuestionSerializer(serializers.ModelSerializer):
    experiment = ExperimentSerializer()
    correct_answer = AnswerSerializer()
    incorrect_answer = AnswerSerializer()
    class Meta:
        model = models.Question
        fields = [
            'text',
            'experiment',
            'correct_answer',
            'incorrect_answer',
        ]