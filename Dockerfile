FROM python:3.10-slim

COPY . /autograder

WORKDIR /autograder

CMD ["python3", "autograder.py"]