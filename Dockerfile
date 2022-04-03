FROM python:3.8.13

WORKDIR /mlservice/
COPY . .
RUN apt update && apt upgrade -y && apt install -y cmake libopencv-dev
RUN pip install -r requirements.txt
EXPOSE 5100
ENTRYPOINT [ "python" ]
CMD [ "api.py" ]