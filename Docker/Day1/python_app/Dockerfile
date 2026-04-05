FROM python:3.9-slim AS builder
WORKDIR /app
COPY app.py .

FROM python:3.9-alpine
WORKDIR /app
COPY --from=builder /app /app
CMD ["python", "app.py"]