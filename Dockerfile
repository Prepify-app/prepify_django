# Используйте официальный образ Python
FROM python:3.10-alpine

# Установите рабочую директорию в контейнере
WORKDIR /app

# Установите виртуальное окружение
RUN python -m venv /venv

# Активируйте виртуальное окружение
ENV PATH="/venv/bin:$PATH"

# Скопируйте файлы проекта
COPY . /app

# Установите зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Определите команду для запуска приложения
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
