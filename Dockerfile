# Use the official FastAPI image
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9


# Install dependencies
COPY ./requirements.txt /app/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the application code
COPY ./app/ /app

# Set the working directory
WORKDIR /app

# Expose the port
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
