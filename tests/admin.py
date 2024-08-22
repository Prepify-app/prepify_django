from django.contrib import admin
from .models import Test, TestResult, Category, Level, Question, AnswerOption

# Регистрация модели Test
@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'updated_at')  # Какие поля отображать
    search_fields = ('name', 'description')  # По каким полям можно искать
    list_filter = ('created_at', 'updated_at')  # Фильтры по дате создания и обновления

# Регистрация модели TestResult
@admin.register(TestResult)
class TestResultAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'test', 'score', 'completed_at', 'created_at', 'updated_at')
    search_fields = ('user_id', 'test__name')  # Возможность поиска по user_id и названию теста
    list_filter = ('completed_at', 'created_at')

# Регистрация модели Category
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('created_at', 'updated_at')

# Регистрация модели Level
@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('created_at', 'updated_at')

# Регистрация модели Question
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'category', 'level', 'test', 'is_show', 'created_at', 'updated_at')
    search_fields = ('text', 'category__name', 'level__name', 'test__name')  # Поиск по вопросу и связанным полям
    list_filter = ('is_show', 'created_at', 'updated_at')

# Регистрация модели AnswerOption
@admin.register(AnswerOption)
class AnswerOptionAdmin(admin.ModelAdmin):
    list_display = ('question', 'text', 'is_correct', 'created_at', 'updated_at')
    search_fields = ('text', 'question__text')  # Поиск по тексту ответа и вопроса
    list_filter = ('is_correct', 'created_at', 'updated_at')

