# Use an official Python image with Debian (has apt)
FROM python:3.11-slim

# Install Chromium and dependencies
RUN apt-get update && apt-get install -y chromium chromium-driver

# Set environment variables for headless Chrome
ENV CHROME_BIN=/usr/bin/chromium
ENV PATH="/usr/lib/chromium/:${PATH}"

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Streamlit's default port
EXPOSE 8501

# Run Streamlit app
CMD ["streamlit", "run", "yt_meta_scrapper.py"]
