#base image
FROM python:3.11

# working directory
WORKDIR /app

#copy files
COPY . /app

# install dependencies
RUN pip install -r requirements.txt

#Expose port
EXPOSE 8002

# execute the code
CMD ["python","./head.py"]
