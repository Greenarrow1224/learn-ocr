FROM python:3.8
WORKDIR /app
COPY ./api ./api
COPY ./requirements.txt ./requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
EXPOSE 8000
CMD ["sanic", "api.get_data:app", "--host", "0.0.0.0","--fast","True","--workers","10"]