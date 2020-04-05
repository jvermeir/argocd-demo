FROM python:3

ADD my_service.py my_service.py
EXPOSE 8000
ENTRYPOINT ["python", "my_service.py"]