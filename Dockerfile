FROM python:3.4-alpine
ADD app /code
WORKDIR /code
ENV SLACK_TOKEN_BOT $SLACK_TOKEN_BOT
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
