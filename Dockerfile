FROM python:3.9

WORKDIR /app

COPY palindrome.py .

ENTRYPOINT ["python", "palindrome.py"]
