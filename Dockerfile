FROM python:3.10

#RUN mkdir /crm

#WORKDIR /crm

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

#RUN chmod a+x /docker/*.sh

CMD ["gunicorn", "main:app", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind=0.0.0.0:8000"]