FROM gcr.io/tensorflow/tensorflow:latest

RUN apt-get update
RUN apt-get install -qq build-essential libssl-dev libffi-dev python-dev curl
RUN pip install Flask azure-storage
RUN apt-get install -qq python-qt4
RUN pip uninstall -y numpy
RUN pip install --no-binary=:all: numpy
RUN pip install pandas

EXPOSE 80