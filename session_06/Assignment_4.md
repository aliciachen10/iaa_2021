# [Institute for Advanced Analytics](https://analytics.ncsu.edu/)
Distruted Analytics & Machine Learning - Dan Zaratsian, March 2021

-----------------
## Assignment #4 - Docker Containers or SparkML

Due on **Wednesday, April 14, 2021**.

This is a choose your own adventure assignment. You can choose one of the following:

1) Select a [Kaggle dataset](https://www.kaggle.com/datasets) and write SparkML code to train an ML model. YOu can choose any dataset that you want. This will also be very similar to what you did in assignment #3, with the goal of repetition and potentially forcing you to use new spark functions to process the new dataset.

2) **(Preferred Option)** Build a Docker container to run this [python script](https://github.com/zaratsian/iaa_2021/blob/main/session_06/python_joke.py). The goal of this assignment is to have you create your own docker container. Your Docker container will need to run this [python script](https://github.com/zaratsian/iaa_2021/blob/main/session_06/python_joke.py). If you're able to run this python file within your container, then you've successfully completed the assignment.

If you choose the Docker homework (option #2), then here are suggested steps that I'd take:

1) Install Docker
    - Install [Docker for Windows](https://docs.docker.com/docker-for-windows/install/)
    - Install [Docker for Mac](https://docs.docker.com/docker-for-mac/install/)
    - Install [Docker for Ubuntu](https://docs.docker.com/engine/install/ubuntu/)

2) Create a [Dockerfile](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)
    
    a) Install python as part of the Dockerfile
    
    b) pip install any required python packages (hint: pyjokes)
    
    c) Add a way to call the [python script](https://github.com/zaratsian/iaa_2021/blob/main/session_06/python_joke.py) from within the Docker container

3) [Build the Docker container](https://docs.docker.com/language/python/build-images/#build-an-image)

4) [Run the Docker Container](https://docs.docker.com/language/python/run-containers/)

**References:**
  - [Building a Python Docker Container](https://docs.docker.com/language/python/build-images/)
  - [Dan's Docker Containers](https://github.com/zaratsian/docker_containers/tree/master/containers)
  - [Docker Tutorial for Beginners](https://docker-curriculum.com/)
  - [Creating a Simple Python Dockerfile](https://docker-curriculum.com/#dockerfile)
  
