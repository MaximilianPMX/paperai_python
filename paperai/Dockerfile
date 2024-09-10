FROM python:3.9-slim-buster

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN pip install poetry && poetry config virtualenvs.create false

RUN poetry install --no-interaction --no-ansi

COPY ./src ./src

CMD ["python", "./src/paperai/cli.py", "--help"]