from rest_framework import serializers

from .models import Todo, User, Researcher, Result

class TodoSerializer(serializers.ModelSerializer):

	class Meta:
		model = Todo
		fields = ('id', 'title', 'description', 'completed')

class ResearcherSerializer(serializers.ModelSerializer):

	class Meta:
		model = Researcher
		fields = ('id', 'fullname', 'email', 'phone')

class UserSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = ('id', 'ResearcherId', 'fullname', 'email', 'phone', 'city', 'education', 'sport', 'datebirth', 'datelasttest')

class ResultSerializer(serializers.ModelSerializer):

	class Meta:
		model = Result
		fields = ('id', 'UserId', 'date_start', 'date_end', 'time1', 'time2', 'time3', 'time4')
