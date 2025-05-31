# Use official python slim base image
FROM python:3.11-slim

# Install Chromium and dependencies
RUN apt-get update && apt-get install -y \
    chromium \
    chromium-driver \
    fonts-liberation \
    libx11-xcb1 \
    libxcomposite1 \
    libxcursor1 \
    libxdamage1 \
    libxi6 \
    libxtst6 \
    libnss3 \
    libxrandr2 \
    libasound2 \
    libatk1.0-0 \
    libcups2 \
    libdbus-1-3 \
    libpangocairo-1.0-0 \
    libgtk-3-0 \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

# Set Chromium path environment variable for Selenium
ENV CHROME_BIN=/usr/bin/chromium

# Set working directory
WORKDIR /app

# Copy requirements & install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your app code
COPY . .

# Expose port if needed (Streamlit default 8501)
EXPOSE 8501

# Command to run your app
CMD ["streamlit", "run", "yt_meta_scrapper.py", "--server.port=8501", "--server.address=0.0.0.0"]
