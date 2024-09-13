# Use the official FastAPI image
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

# Set the working directory
WORKDIR /app

# Copy and install dependencies
COPY ./requirements.txt /app/requirements.txt
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r /app/requirements.txt

# Copy the application code
COPY ./app /app

# Expose port 80 (since you are running on port 80)
EXPOSE 80

# Switch to a non-root user (optional but recommended for security)
RUN adduser --disabled-password fastapiuser
USER fastapiuser

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
