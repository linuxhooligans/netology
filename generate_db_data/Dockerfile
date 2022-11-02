FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
COPY adjectives.txt /code/
COPY type.txt /code/
COPY generate_db_data.py /code/
COPY entrypoint.sh /
RUN pip install -r requirements.txt
RUN chmod +x /entrypoint.sh
