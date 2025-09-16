FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    curl \
    git \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Download NLTK data and models (if needed)
RUN python -c "import nltk; nltk.download('punkt', download_dir='/usr/local/share/nltk_data')"
RUN python -c "import nltk; nltk.download('stopwords', download_dir='/usr/local/share/nltk_data')"

# Copy application code
COPY . .

# Create directories for logs and static files
RUN mkdir -p logs static templates

# Create non-root user for security
RUN useradd --create-home --shell /bin/bash chatbot
RUN chown -R chatbot:chatbot /app
USER chatbot

# Health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8000/health || exit 1

# Expose port
EXPOSE 8000

# Command to run the application
CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]