FROM python:3.9

# Устанавливаем рабочую директорию
WORKDIR /code

# Копируем файл requirements.txt и устанавливаем зависимости
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# Копируем весь проект в контейнер
COPY . /code/

# Запускаем Gunicorn для сервера Django
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "prepify.wsgi:application"]
