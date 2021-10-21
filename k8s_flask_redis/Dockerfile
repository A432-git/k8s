From python:3.7
# Set the working directory to /app
WORKDIR /app
ADD ./app /app
#COPY requirements.txt /app/
# Install any needed packages specified in requirement.txt
RUN pip install requirements.txt
# Make port 6000 available to the world outside this container
EXPOSE 6000
# Define environment variable
ENV envname=k8s
# ADD application.py to /app
#ADD application.py /app/
CMD ["python", "app.py"]