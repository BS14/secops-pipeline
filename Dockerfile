# --- Stage 1: Build Stage ---
FROM python:3.14-slim-trixie AS builder

WORKDIR /app

# Create and switch to a new non-root user
RUN groupadd -r appuser && useradd -r -g appuser appuser

COPY requirements.txt .

RUN pip install \
  --no-cache-dir \
  --default-timeout=100 \
  -r requirements.txt

# --- Stage 2: Final Stage ---
FROM python:3.14-slim-trixie AS final

# Set the working directory
WORKDIR /app

# Create the same non-root user as in the builder stage
RUN groupadd -r appuser && useradd -r -g appuser appuser

# Copy the installed packages from the builder stage
COPY --from=builder /usr/local/lib/python3.14/site-packages /usr/local/lib/python3.14/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy the application code into an 'apps' directory
COPY apps/ apps/

# Change ownership of the app directory to the non-root user
RUN chown -R appuser:appuser /app

# Switch to the non-root user
USER appuser

# Expose the port the app will run on
EXPOSE 8000

# Define the command to run the application
# We update the module path from 'main:app' to 'apps.main:app'
CMD ["uvicorn", "apps.main:app", "--host", "0.0.0.0", "--port", "8000"]
