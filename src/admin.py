from django.contrib import admin
from .models import Question, Quiz, Choice, AnswerList, Answer


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['title']}),
        ('Quiz information', {'fields': ['quiz']})
    ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Quiz)
admin.site.register(AnswerList)
admin.site.register(Answer)