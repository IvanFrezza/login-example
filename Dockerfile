#The Flask application container will use python:3.10-alpine as the base image
FROM python:3.10-alpine

# Installing client libraries and any other package you need
RUN apk update && apk add libpq

# Installing build dependencies
# For python3 you need to add python3-dev *please upvote the comment
# of @its30 below if you use this*
RUN apk add --virtual .build-deps gcc musl-dev postgresql-dev


#This command will create the working directory for our Python Flask application Docker image
WORKDIR /app

#This command will copy the dependencies and libraries in the requirements.txt to the working directory
COPY requirements.txt /app

#This command will install the dependencies in the requirements.txt to the Docker image
RUN pip install -r requirements.txt --no-cache-dir

#This command will copy the files and source code required to run the application
COPY . /app

#This command will start the Python Flask application Docker container
CMD python app.py