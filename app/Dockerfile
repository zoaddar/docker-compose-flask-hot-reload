FROM python:alpine

EXPOSE 5000

WORKDIR /app
COPY * /app/

COPY requirements.txt ./
RUN python -m pip install --upgrade pip && \
    pip install -r requirements.txt

CMD python route.py
