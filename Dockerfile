# Use the official FastAPI image
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

# Set the working directory
WORKDIR /app

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 - && \
    /root/.local/bin/poetry --version  # Verify that Poetry was installed

# Ensure Poetry is in the PATH
ENV PATH="/root/.local/bin:$PATH"

# Copy pyproject.toml and poetry.lock
COPY ./pyproject.toml ./poetry.lock* /app/

# Install dependencies with Poetry
RUN poetry install --no-dev

# Copy the application code
COPY ./app /app

# Expose port 80 (since you are running on port 80)
EXPOSE 80

# Switch to a non-root user (optional but recommended for security)
RUN adduser --disabled-password fastapiuser
USER fastapiuser

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
