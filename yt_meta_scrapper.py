import streamlit as st
import yt_dlp
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import re

#======= Selenium Scraper Function =======
def short_link_fetcher(channel_link):
    options = Options()
    options.binary_location = "/usr/bin/chromium"
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # ✅ Use system-installed ChromeDriver (matches Chromium)
    service = Service("/usr/bin/chromedriver")
    driver = webdriver.Chrome(service=service, options=options)

    driver.get(channel_link)
    time.sleep(5)

    # Scroll down to load more Shorts
    for _ in range(3):
        driver.execute_script("window.scrollBy(0, 1000);")
        time.sleep(2)

    links = set()
    elements = driver.find_elements(By.TAG_NAME, "a")
    for elm in elements:
        href = elm.get_attribute("href")
        if href and "/shorts/" in href:
            links.add(href.split("?")[0])

    driver.quit()
    return list(links)

#======= Metadata Extractor =======
def meta_data_extractor(links):
    data = []
    for link in links:
        ydl_opts = {
            "quiet": True,
            "skip_download": True,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            try:
                info = ydl.extract_info(link, download=False)
                title = info.get("title", "")
                description = info.get("description", "")
                tags = info.get("tags", [])
                hashtags = re.findall(r"#\w+", description or "")
                views = info.get("view_count", 0)
                likes = info.get("like_count", 0)
                date = info.get("upload_date", "")

                data.append({
                    "Title": title,
                    "Description": description,
                    "Embedded_Tags": tags,
                    "Hashtags": hashtags,
                    "No_Of_Views": views,
                    "No_Of_Likes": likes,
                    "Upload_Date": date,
                    "Shorts_Link": link,
                })
            except Exception as e:
                st.warning(f"Failed to extract: {link} | Reason: {e}")
    return pd.DataFrame(data)

#======= Streamlit App UI =======
st.set_page_config(page_title="YouTube Shorts Metadata Scraper", layout="wide")
st.title("📽️ YouTube Shorts Metadata Scraper")

channel_url = st.text_input("Enter the channel Shorts URL (e.g. https://www.youtube.com/@channel_name/shorts)")

if st.button("Scrape Contents"):
    if "shorts" not in channel_url:
        st.error("⚠️ Make sure the link ends with `/shorts`.")
    else:
        with st.spinner(f"Fetching metadata from {channel_url}..."):
            shorts_links = short_link_fetcher(channel_url)
            df = meta_data_extractor(shorts_links)

            if not df.empty:
                st.success(f"✅ Found {len(df)} Shorts!")
                st.dataframe(df)
                csv = df.to_csv(index=False).encode("utf-8")
                st.download_button(
                    label="⬇️ Download Metadata as CSV",
                    data=csv,
                    file_name="Metadata_YT_Shorts.csv",
                    mime="text/csv",
                )
            else:
                st.warning("⚠️ No Shorts metadata extracted.")
