from rest_framework import serializers
from .models import Quiz


class ChoiceSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)


class QuestionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)
    choices = ChoiceSerializer(many=True)


class AnswerSerializer(serializers.Serializer):
    pass


class AnswerListSerializer(serializers.Serializer):
    answers = AnswerSerializer(many=True)

#####################
class QuizSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    start_date = serializers.DateField()
    end_date = serializers.DateField()
    title = serializers.CharField(max_length=100)
    questions = QuestionSerializer(many=True)
    answer_lists = AnswerListSerializer(many=True)


class QuizPostUpdateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    end_date = serializers.DateField()

    def create(self, validated_data):
        return Quiz.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.end_date = validated_data.get('end_date', instance.end_date)
        instance.clean()
        instance.save()
        return instance




