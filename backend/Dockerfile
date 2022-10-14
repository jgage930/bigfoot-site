FROM python:3.8
WORKDIR /app

ENV POETRY_VERSION=0.1.0

RUN pip install 'poetry==${POETRY_VERSION}'

COPY poetry.lock poety.toml /app/

COPY ./main.py /app/

RUN poetry export --without-hashes --no-interaction --no-ansi -f requirements.txt -o requirements.txt

RUN pip install setuptools

RUN pip install --force-reinstall -r requirements.txt

CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8996"]