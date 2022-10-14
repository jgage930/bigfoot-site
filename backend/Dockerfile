FROM python:3.8
WORKDIR /app


RUN pip install poetry

COPY poetry.lock poety.toml /app/

COPY ./main.py /app/

RUN poetry export --without-hashes --no-interaction --no-ansi -f requirements.txt -o requirements.txt

RUN pip install setuptools

RUN pip install --force-reinstall -r requirements.txt

CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8996"]