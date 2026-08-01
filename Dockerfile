# hello-flask-sz · 生产镜像
FROM python:3.11-slim

ARG PIP_INDEX_URL=https://pypi.org/simple

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --timeout 120 -i "${PIP_INDEX_URL}" -r requirements.txt

COPY app.py .

EXPOSE 8003

CMD ["python", "app.py"]
