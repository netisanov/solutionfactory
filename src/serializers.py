from rest_framework import serializers


class ChoiceSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)


class QuestionSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    choices = ChoiceSerializer(many=True)


class AnswerSerializer(serializers.Serializer):
    pass


class AnswerListSerializer(serializers.Serializer):
    answers = AnswerSerializer(many=True)


class QuizSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    questions = QuestionSerializer(many=True)
    answer_lists = AnswerListSerializer(many=True)

