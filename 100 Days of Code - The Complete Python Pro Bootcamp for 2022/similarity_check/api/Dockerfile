FROM python:3.10
WORKDIR /media/sagebeme/Kila kitu/Code/100-Days-of-Code-Bootcamp/100 Days of Code - The Complete Python Pro Bootcamp for 2022/similarity_check/api
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN pip install ./en_core_web_sm-3.7.0.tar.gz
CMD [ "python", "app.py" ]