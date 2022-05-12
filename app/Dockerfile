FROM python:latest


COPY . /app

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5487

CMD [ "python", "main.py"]