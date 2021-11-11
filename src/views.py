import datetime

from dateutil import parser

from django.shortcuts import get_object_or_404
from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login
from django.http import Http404

from .models import (
    Question,
    Quiz,
    Choice,
    AnswerList,
    Answer
)
from .serializers import (
    QuestionSerializer,
    QuizSerializer,
    ChoiceSerializer,
    AnswerSerializer,
    AnswerListSerializer,
    QuizPostUpdateSerializer,
    QuestionPostUpdateSerializer,
    ChoicePostUpdateSerializer,
)


class ApiRoot(APIView):
    def get(self, request, format=None):
        return Response({
            'quizes': reverse('quiz-list', request=request, format=format),
            'authentication': reverse('authentication', request=request, format=format)
        })


##############


class QuestionList(APIView):
    def get(self, request, quiz_id, format=None):
        queryset = Question.objects.filter(quiz=quiz_id)
        serializer_context = {'request': request}
        response = QuestionSerializer(queryset, context=serializer_context, many=True)
        return Response(response.data)

    def post(self, request, quiz_id, format=None):
        request.data['quiz_id'] = quiz_id
        serializer = QuestionPostUpdateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        pass


class QuestionDetail(APIView):
    def get_object(self, question_id, quiz_id):
        return get_object_or_404(Question, pk=question_id, quiz__pk=quiz_id)

    def get(self, request, question_id, quiz_id, format=None):
        question = self.get_object(question_id, quiz_id)
        serializer_context = {
            "request": request
        }
        response = QuestionSerializer(question, context=serializer_context)
        return Response(response.data)

    def put(self, request, question_id, quiz_id, format=None):
        question = self.get_object(question_id, quiz_id)
        serializer = QuestionPostUpdateSerializer(question, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, question_id, quiz_id, format=None):
        question = self.get_object(question_id, quiz_id)
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ChoiceDetail(APIView):
    def get_object(self, choice_id, question_id, quiz_id):
        question = get_object_or_404(Question, pk=question_id, quiz__pk=quiz_id)
        return get_object_or_404(Choice, pk=choice_id, question__pk=question.id)

    def get(self, request, choice_id, question_id, quiz_id, format=None):
        choice = self.get_object(choice_id, question_id, quiz_id)
        serializer_context = {
            "request": request
        }
        response = ChoiceSerializer(choice, context=serializer_context)
        return Response(response.data)

    def put(self, request, choice_id, question_id, quiz_id):
        choice = self.get_object(choice_id, question_id, quiz_id)
        serializer = ChoicePostUpdateSerializer(choice, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, choice_id, question_id, quiz_id, format=None):
        choice = self.get_object(choice_id, question_id, quiz_id,)
        choice.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class QuizList(APIView):
    def get(self, request, format=None):
        queryset = Quiz.objects.filter(start_date__lte=datetime.datetime.now(),
                                       end_date__gte=datetime.datetime.now())
        serializer_context = {"request": request}
        response = QuizSerializer(queryset, context=serializer_context, many=True)
        return Response(response.data)

    def post(self, request, format=None):
        request.data['end_date'] = (parser.parse(request.data['end_date'])).date()
        serializer = QuizPostUpdateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuizDetail(APIView):
    def get_object(self, quiz_id):
        return get_object_or_404(Quiz, pk=quiz_id)

    def get(self, request, quiz_id, format=None):
        quiz = self.get_object(quiz_id)
        serializer_context = {"request": request}
        response = QuizSerializer(quiz, context=serializer_context)
        return Response(response.data)

    def delete(self, request, quiz_id, format=None):
        quiz = self.get_object(quiz_id)
        quiz.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, quiz_id, format=None):
        quiz = self.get_object(quiz_id)
        request.data['end_date'] = (parser.parse(request.data['end_date'])).date()
        serializer = QuizPostUpdateSerializer(quiz, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


###########


class AnswerDetail(APIView):
    def get_object(self, pk):
        try:
            return Answer.objects.get(pk=pk)
        except Answer.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        answer = self.get_object(pk=pk)
        serializer_context = {"request": request}
        response = AnswerSerializer(answer, context=serializer_context)
        return Response(response.data)


class AnswerListDetail(APIView):
    def get_object(self, answerlist_pk):
        try:
            return AnswerList.objects.get(pk=answerlist_pk)
        except AnswerList.DoesNotExist:
            raise Http404

    def get(self, request, answerlist_pk, format=None):
        answer_list = self.get_object(answerlist_pk)
        serializer_context = {
            "request": request
        }
        response = AnswerListSerializer(answer_list, context=serializer_context)
        return Response(response.data)


class Authentication(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return Response('Success')
            else:
                return Response('Fuck')
        else:
            return Response('Oops')



