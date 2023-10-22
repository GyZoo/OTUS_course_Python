FROM python:3.11.4-bookworm

WORKDIR /fast_api_app

COPY fast_api_app/requirements.txt ./

RUN pip install -r requirements.txt

COPY fast_api_app .

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host=0.0.0.0" ,"--port=8000"]