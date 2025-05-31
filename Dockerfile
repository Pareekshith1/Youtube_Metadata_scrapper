FROM python:3.10-alpine

ENV PYTHONUNBUFFERED=1
ENV CHROME_BIN=/usr/bin/chromium-browser

# Install Chromium and dependencies
RUN apk update && apk add --no-cache \
    chromium \
    chromium-chromedriver \
    bash \
    curl \
    git \
    libc6-compat \
    libstdc++ \
    libffi \
    jpeg-dev \
    zlib-dev \
    libjpeg \
    gcc \
    g++ \
    python3-dev \
    musl-dev \
    make

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose port (Streamlit default)
EXPOSE 8501

# Run your app
CMD ["streamlit", "run", "yt_meta_scrapper.py", "--server.port=8501", "--server.enableCORS=false"]
