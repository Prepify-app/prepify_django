FROM python:3.10-alpine

WORKDIR /app
COPY . /app

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

EXPOSE 8000


# Определите команду для запуска приложения
ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
