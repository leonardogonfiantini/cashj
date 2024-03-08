FROM python:3.11-buster

RUN pip install poetry

COPY ./api ./api
COPY pyproject.toml pyproject.toml

RUN poetry install

ENTRYPOINT ["poetry", "run", "python", "api"]