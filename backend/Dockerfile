# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container to /backend
WORKDIR /backend

# Copy the current directory contents into the container at /backend
COPY ./backend /backend/

# Install any needed packages specified in requirements.txt
# The `--no-binary` flag forces pip to use pre-built wheels instead of compiling from source.
RUN pip install --no-cache-dir --only-binary=:all: -r requirements.txt

# Make the 'build' directory if it doesn't exist and collect static files
RUN mkdir -p build/static \
    && python manage.py collectstatic --noinput

# Run makemigrations and migrate as separate steps to ensure the schema is up to date
RUN python manage.py makemigrations \
    && python manage.py migrate

# The command to run the app when the container starts
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
