# mlservice-for-gender-age
Simple API created for getting gender and age detection through json api. This API is directly using deepface for extracting features out of faces.

## Installation

Clone this repository 
```shell
git clone https://github.com/Pritish053/mlservice-for-gender-age.git
cd mlservice-for-gender-age/
```

Create a new pip environment
```shell
python3.8 -m venv env_flask

#just to make sure you have updated version of pip
pip install -U pip

pip install -r requirements.txt
```
Run with flask.
```shell
python api.py
```

## Run with Docker

You can build a docker for this and run inside a docker container.
```shell
docker build -t mlservice_api .
```

Run the docker container with the required ports exposed
```shell
docker run -d -p 5100:5100 --name mlservice_docker mlservice_api
```

for logs you can always go to
```shell 
docker logs mlservice_docker
```
## Test the API

We have test_api.py for the testing purpose of the API.
```shell
#Please change the path of the image in test_api.py before running the file.
python test_api.py
```

