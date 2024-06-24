# Use an official Python runtime as a parent image
FROM python:3

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /plusonecontainer

# Install dependencies
COPY requirements.txt /plusonecontainer/
RUN pip install --no-cache-dir -r requirements.txt
# Copy the rest of the application code
COPY . /plusonecontainer/

# Expose the port that Django runs on
EXPOSE 8000

# Run the Django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
