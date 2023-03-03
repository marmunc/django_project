from django.shortcuts import render

# import view sets from the REST framework
from rest_framework import viewsets

# import the TodoSerializer from the serializer file
from .serializers import TodoSerializer, ResearcherSerializer, UserSerializer, ResultSerializer

# import the Todo model from the models file
from .models import Todo, Researcher, User, Result

# create a class for the Todo model viewsets
class TodoView(viewsets.ModelViewSet):
	serializer_class = TodoSerializer
	queryset = Todo.objects.all()

class ResearcherView(viewsets.ModelViewSet):
	serializer_class = ResearcherSerializer
	queryset = Researcher.objects.all()

class UserView(viewsets.ModelViewSet):
	serializer_class = UserSerializer
	queryset = User.objects.all()

class ResultView(viewsets.ModelViewSet):
	serializer_class = ResultSerializer
	queryset = Result.objects.all()