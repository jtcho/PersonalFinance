FROM python:3.6

RUN apt-get update

RUN mkdir /root/.ssh/

WORKDIR /opt/code
# Install all dependencies.
ADD ./requirements.txt /opt/code/requirements.txt
RUN pip install -r requirements.txt

# Add all other files.
ADD . /opt/code

# Install the local project.
RUN ["python", "setup.py", "sdist"]
RUN pip install .

# Sets entry point for executing docker container.
CMD ["/bin/bash", "init.sh"]

