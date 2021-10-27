# Assignment

Mess around with Docker and explore their documentation to learn the power and functionality
of Docker containers.

I encourage you to reference the Module 1 assignment and create more helper functions *within* a Docker container. Create an image from a
Dockerfile that will download the necessary dependencies for your helper functions and be sure to use a different Operating System than the one you are currently using. (Try a linux-based one like Ubuntu!)

You should follow this work flow in terms of creation: Dockerfile -> Image -> Container -> helper_functions.py

Here are some test Dockerfiles that you can play around with or modify as your run some of your own experiments.

Here's a dockerfile that runs the debian operating system instead of ubuntu.

```
# Dockerfile

FROM debian

### So logging/io works reliably w/Docker
ENV PYTHONUNBUFFERED=1
### UTF Python issue for Click package (pipenv dependency)
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
### Need to explicitly set this so `pipenv shell` works
ENV SHELL=/bin/bash

### Basic Python dev dependencies
RUN apt-get update && \
  apt-get upgrade -y && \
  apt-get install python3-pip curl -y && \
  pip3 install pipenv

### Install via pip or pipenv:
RUN pip3 install pandas
#RUN pipenv install pandas
```
Here's a dockerfile with a "python" image.

```
 Dockerfile

FROM python:3

ENV PYTHONUNBUFFERED=1

RUN apt-get update && \
    apt-get upgrade -y && \
    pip install --upgrade pip

RUN pip install pandas 
    
#  or install packages from the requirements.txt file (must be in same dir as Dockerfile)
# COPY requirements.txt /tmp/requirements.txt
# RUN pip install -r /tmp/requirements.txt
```

**Submit your Dockerfile on Canvas as evidence of your work this afternoon.**

If you finish the exercise early go back and review your module 1 and 2 assignments.