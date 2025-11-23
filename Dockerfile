# Simple Python runtime for Apify actor
FROM python:3.11-slim

# Install git (for potential git-based dependencies)
RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements and install Python dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy actor code
COPY . ./

# Run actor via proper entry point
CMD ["python", "__main__.py"]
