# 📽️ YouTube Shorts Metadata Scraper

A powerful web application built with Streamlit that extracts comprehensive metadata from YouTube Shorts videos. This tool helps content creators, marketers, and researchers analyze YouTube Shorts content at scale.

## 🚀 Features

- 🔍 **Automatic Shorts Discovery**: Scrapes all Shorts from a YouTube channel
- 📊 **Comprehensive Metadata Extraction**: Extracts titles, descriptions, tags, hashtags, views, likes, and upload dates
- 💾 **CSV Export**: Download extracted data in CSV format for further analysis
- 🎨 **User-Friendly Interface**: Clean and intuitive Streamlit web interface
- 🐳 **Docker Support**: Containerized deployment for easy setup

## 🛠️ Tech Stack

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)

</div>

### Core Technologies

- **Python 3.11**: Primary programming language
- **Streamlit**: Web application framework for the user interface
- **yt-dlp**: YouTube data extraction library
- **Selenium**: Web automation for dynamic content scraping
- **Pandas**: Data manipulation and CSV export
- **Chromium/ChromeDriver**: Headless browser for web scraping

## 📋 Prerequisites

### For Local Development
- Python 3.11 or higher
- Chromium/Chrome browser
- ChromeDriver (matching your Chrome version)

### For Docker Deployment
- Docker installed on your system

## 🔧 Installation

### Method 1: Local Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/Youtube_Metadata_scrapper.git
   cd Youtube_Metadata_scrapper
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv ytvenv
   ```

3. **Activate the virtual environment**
   - Windows:
     ```bash
     ytvenv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source ytvenv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Install ChromeDriver**
   - Download ChromeDriver matching your Chrome version from [ChromeDriver Downloads](https://chromedriver.chromium.org/downloads)
   - Add it to your system PATH or place it in the project directory
   - For Linux (Docker): ChromeDriver is automatically installed

### Method 2: Docker Setup

1. **Build the Docker image**
   ```bash
   docker build -t youtube-shorts-scraper .
   ```

2. **Run the container**
   ```bash
   docker run -p 8501:8501 youtube-shorts-scraper
   ```

## 🎯 Usage

### Running Locally

1. **Start the application**
   ```bash
   streamlit run yt_meta_scrapper.py
   ```

2. **Access the web interface**
   - Open your browser and navigate to `http://localhost:8501`

3. **Scrape YouTube Shorts**
   - Enter a YouTube channel's Shorts URL (e.g., `https://www.youtube.com/@channelname/shorts`)
   - Click "Scrape Contents" button
   - Wait for the scraping process to complete
   - View the extracted metadata in a table
   - Download the data as CSV

### Running with Docker

1. **Start the container** (if not already running)
   ```bash
   docker run -p 8501:8501 youtube-shorts-scraper
   ```

2. **Access the application at** `http://localhost:8501`

## 📊 Extracted Metadata Fields

The scraper extracts the following information for each Short:

| Field | Description |
|-------|-------------|
| **Title** | Video title |
| **Description** | Full video description |
| **Embedded_Tags** | Tags added by the creator |
| **Hashtags** | Hashtags extracted from description |
| **No_Of_Views** | Total view count |
| **No_Of_Likes** | Total like count |
| **Upload_Date** | Date when the video was uploaded |
| **Shorts_Link** | Direct URL to the Short |

## 🏗️ Project Structure

```
Youtube_Metadata_scrapper/
│
├── yt_meta_scrapper.py      # Main application file
├── requirements.txt          # Python dependencies
├── Dockerfile               # Docker configuration
├── .gitignore              # Git ignore rules
├── README.md               # Project documentation
│
├── ytvenv/                 # Virtual environment (git-ignored)
└── driver/                 # ChromeDriver location (git-ignored)
```

## ⚙️ Configuration

### Selenium Settings (in `yt_meta_scrapper.py`)

The scraper uses headless Chrome with the following options:
- `--headless`: Runs browser in background
- `--no-sandbox`: Required for Docker environments
- `--disable-dev-shm-usage`: Prevents memory issues in containers

### Chromium Paths (Docker)
- Binary: `/usr/bin/chromium`
- ChromeDriver: `/usr/bin/chromedriver`

> **Note**: For local development on Windows/macOS, you'll need to update these paths in the code to match your system's ChromeDriver location.

## 🐛 Troubleshooting

### Common Issues

1. **ChromeDriver version mismatch**
   - Ensure ChromeDriver version matches your installed Chrome version
   - Download the correct version from [ChromeDriver Downloads](https://chromedriver.chromium.org/downloads)

2. **Module not found errors**
   - Ensure virtual environment is activated
   - Reinstall dependencies: `pip install -r requirements.txt`

3. **No Shorts found**
   - Verify the URL ends with `/shorts`
   - Some channels may have Shorts disabled or use different URLs
   - Try scrolling behavior adjustment in the code (increase sleep time)

4. **Docker container issues**
   - Ensure port 8501 is not already in use
   - Check Docker logs: `docker logs <container_id>`

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This tool is for educational and research purposes only. Please respect YouTube's Terms of Service and rate limits when using this scraper. The developers are not responsible for any misuse of this tool.

## 🔮 Future Enhancements

- [ ] Add support for regular YouTube videos
- [ ] Implement rate limiting and retry logic
- [ ] Add authentication for private/restricted content
- [ ] Support for multiple channels in batch
- [ ] Advanced filtering and sorting options
- [ ] Data visualization dashboard
- [ ] Export to multiple formats (JSON, Excel)

## 📧 Contact

For questions, suggestions, or issues, please open an issue on GitHub or contact the maintainer.

---

<div align="center">

**Made with ❤️ using Python and Streamlit**

⭐ Star this repo if you find it useful!

</div>
