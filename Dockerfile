FROM python:3.10

COPY app/requirements.txt .

RUN pip install -r requirements.txt

COPY app .

ENTRYPOINT ["gunicorn", "main:app", "--workers", "10", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000", "--log-level", "info", "--timeout", "30"]
