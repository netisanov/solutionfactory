from django.urls import path, include
from .views import QuestionDetail, QuizList, ChoiceDetail, QuizDetail, AnswerListDetail, Authentication, ApiRoot


# urlpatterns = [
#     path('', ApiRoot.as_view()),
#     path('quizes/', QuizList.as_view(), name='quiz-list'),
#     path('quizes/<int:quiz_id>/', QuizDetail.as_view(), name='quiz-detail'),
#     path('questions/<int:question_id>/', QuestionDetail.as_view(), name='question-detail'),
#     path('choices/<int:choice_id>/', ChoiceDetail.as_view(), name='choice-detail'),
#     path('answers-lists/<int:answerlist_id>/', AnswerListDetail.as_view(), name='answer-list-detail'),
#     path('auth/', Authentication.as_view(), name='authentication')
# ]

urlpatterns = [
    path('', ApiRoot.as_view()),
    path('quizes/', QuizList.as_view(), name='quiz-list'),
    path('quizes/<int:quiz_id>/', QuizDetail.as_view(), name='quiz-detail'),
    path('quizes/<int:quiz_id>/questions/<int:question_id>/', QuestionDetail.as_view(), name='question-detail'),
    path('quizes/<int:quiz_id>/questions/<int:question_id>/choices/<int:choice_id>/', ChoiceDetail.as_view(), name='choice-detail'),
    path('quizes/<int:quiz_id>/answers-lists/<int:answerlist_id>/', AnswerListDetail.as_view(), name='answer-list-detail'),
    path('auth/', Authentication.as_view(), name='authentication')
]

