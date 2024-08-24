FROM python:3.9-slim-buster

WORKDIR /app

# Copy poetry.lock and pyproject.toml
COPY poetry.lock pyproject.toml ./

# Install poetry
RUN pip install poetry

# Install dependencies defined in poetry.lock
RUN poetry install --no-interaction --no-ansi

# Copy the application source code
COPY ./src ./src

# Set the entrypoint command to run the application
CMD ["python", "./src/paperai/cli.py"]