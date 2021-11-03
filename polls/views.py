import requests
from django.http import HttpResponse
from rest_framework import viewsets

from utils.url import restify

from .models import Question
from .serializers import QuestionSerializer


def index(request):
    response = requests.get(restify("/questions/"))
    questions = response.json()
    output = ", ".join([q['question_text'] for q in questions])
    return HttpResponse(output)


# API
# ===


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
