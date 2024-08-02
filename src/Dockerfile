FROM python:3.11.9-slim

WORKDIR /code

COPY --from=for_requirements requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

CMD ["fastapi", "run", "main.py", "--port", "80"]
