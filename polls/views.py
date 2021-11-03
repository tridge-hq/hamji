import requests
from django.http import HttpResponse
from rest_framework import viewsets

from .models import Question
from .serializers import QuestionSerializer


def index(request):
    response = requests.get("http://127.0.0.1:8000/_api/questions/")
    questions = response.json()
    output = ", ".join([q['question_text'] for q in questions])
    return HttpResponse(output)


# API
# ===


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
