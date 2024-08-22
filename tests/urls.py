from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'levels', LevelViewSet)
router.register(r'tests', TestViewSet)
router.register(r'tests-results', TestResultViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'answers', AnswerOptionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
