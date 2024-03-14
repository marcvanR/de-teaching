FROM python:3.12.2-slim

WORKDIR /work

COPY . .
RUN pip install --no-cache-dir .

EXPOSE 8080
USER 1001
CMD [ "uvicorn", "http-svc.backend:app", "--reload", "--port", "8080", "--host", "0.0.0.0"]
