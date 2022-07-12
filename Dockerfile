#FROM python:3.9.4-alpine
FROM python:3.9
MAINTAINER PCTeam pcteam@bahag.com

# set work directory
WORKDIR /usr/

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV  PYTHONPATH "${PYTHONPATH}:/usr/src/app/:/usr/src/"

# copy requirements file
COPY ./requirements.txt ./requirements.txt

#setting up the virtualenv
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN python -m pip install pip

# needed to prevent from breaking on rfc6266 install
RUN pip install setuptools==57.5.0
RUN pip install wheel==0.37.1
# requirements
RUN pip install -r requirements.txt

RUN rm -rf /root/.cache/pip

# copy project
COPY . /usr/
