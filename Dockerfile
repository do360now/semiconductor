# Use the official FastAPI image
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

# Install dependencies
RUN pip install --upgrade pip
RUN pip install fastapi uvicorn jinja2 motor pyOpenSSL cryptography

# Copy the application code
COPY ./app/ /app

# Set the working directory
WORKDIR /app

# Expose the port
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
