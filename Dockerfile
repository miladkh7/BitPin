# pull base image
FROM python:3.11

# Set env variabels
ENV PYTHONUNBUFFERED 1

# SET WORKING DIRECTORY
RUN mkdir /code
WORKDIR /code

# install depencencityes
## old version 
ADD requirements.txt /code/
RUN --mount=type=cache,target=/root/.cache/pip pip install -r requirements.txt

# install depencdencity pipenv
# RUN pip install pipenv
# COPY Pipfile Pipfile.lock /code/
# RUN pipenv install --skip-lock  --system
# RUN pipenv sync

# Copy project
COPY . /code/
# EXPOSE 8000

ENTRYPOINT ["sh","/code/run_blog.sh"]