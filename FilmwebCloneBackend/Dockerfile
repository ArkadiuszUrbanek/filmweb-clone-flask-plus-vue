FROM python:3.12.2-bookworm

EXPOSE 5000

WORKDIR /filmweb-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "flask", "run", "--host=0.0.0.0", "--port=5000"]