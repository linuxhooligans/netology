FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY entrypoint.sh /
COPY requirements.txt /code/
COPY manage.py /code/
RUN pip install -r requirements.txt
RUN chmod +x /entrypoint.sh
COPY ./candydendy/ /code/candydendy
