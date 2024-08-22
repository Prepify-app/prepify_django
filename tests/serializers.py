from rest_framework import serializers
from .models import *


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'


class TestResultSerializer(serializers.ModelSerializer):
    test_id = serializers.IntegerField(source='test.id', read_only=True) 
    test_info = TestSerializer(source='test', read_only=True) 

    class Meta:
        model = TestResult
        fields = ['id', 'user_id', 'test_id', 'test_info', 'score', 'completed_at', 'created_at', 'updated_at'] 


class CategorySerializer(serializers.ModelSerializer):
    class Meta: 
        model = Category
        fields = '__all__'


class LevelSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Level
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    level = LevelSerializer(read_only=True)
    test = TestSerializer(read_only=True)
    class Meta: 
        model = Question
        fields = ['id', 'text', 'category', 'level', 'test', 'is_show', 'created_at', 'updated_at']


class AnswerOptionSerializer(serializers.ModelSerializer):
    question = QuestionSerializer(read_only=True)
    class Meta: 
        model = AnswerOption
        fields = ['id', 'question', 'text', 'is_correct', 'created_at', 'updated_at']
