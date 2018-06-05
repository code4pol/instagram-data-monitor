FROM python:3.6.5

RUN apt update -y

RUN mkdir /usr/app

WORKDIR /usr/app

RUN curl -o /usr/local/bin/mantra -L https://github.com/pugnascotia/mantra/releases/download/0.0.1/mantra && \
    chmod +x /usr/local/bin/mantra

COPY $PWD/instagram-data-monitor/requirements.txt .

RUN pip install -r requirements.txt

# RUN curl -o /usr/local/bin/mantra -L https://github.com/pugnascotia/mantra/releases/download/0.0.1/mantra && \
#    chmod +x /usr/local/bin/mantra



# docker exec -it nome:tag bash # entra no bash da imagem
