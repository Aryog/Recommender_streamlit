FROM python:3.10
COPY . /app
WORKDIR /app
RUN pip install --no-cache-dir -r requirement.txt
EXPOSE 8501
CMD ["streamlit","run","app.py"]

