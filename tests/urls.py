from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'levels', LevelViewSet)
router.register(r'tests', TestViewSet)
router.register(r'tests-results', TestResultViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'answers', AnswerOptionViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Prepify API",
        default_version='v1',
        description="API documentation for the Prepify application",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
