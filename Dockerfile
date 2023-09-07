FROM python:3.10-slim
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY django_graphql /usr/src/app/
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]