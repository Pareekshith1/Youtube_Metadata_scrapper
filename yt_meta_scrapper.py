#import streamlit for the framework
import streamlit as st
#import the extractor package
import yt_dlp
#import pandas for data-analytics
import pandas as pd
#import selenium for synamic web scrapping
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
#import time to implement a sleep
import time
#import re for the hashtag extraction
import re
#import os for the path correction
import os

#=====CHROME DRIVER CONFIGURATION=======
CHROME_DRIVER_PATH = "./driver/chromedriver.exe"

#=======Scrapping Function=======
def short_link_fetcher(channel_link):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")  # VERY important for Streamlit Cloud
    options.add_argument("--disable-dev-shm-usage")  # Also helps in cloud environments

    service = Service(CHROME_DRIVER_PATH)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    driver.get(channel_link)
    time.sleep(5)

    for _ in range(3):
        driver.execute_script("window.scrollBy(0,1000);")
        time.sleep(2)

    link= set()
    elements = driver.find_elements(By.TAG_NAME,"a")
    for elm in elements:
        href = elm.get_attribute("href")
        if href and "/shorts/" in href:
            link.add(href.split("?")[0])

    driver.quit()
    return list(link)


#========Metadata Extractor========\
def meta_data_extractor(links):
    data =[]
    for link in links:
        yld_opt = {
            "quiet":True,
            "skip_download":True,
        }
        with yt_dlp.YoutubeDL(yld_opt) as yld:
            try:
                info = yld.extract_info(link, download=False)
                title = info.get("title","")
                description = info.get("description","")
                tags = info.get("tags",[])
                hashtags = re.findall(r"#\w+", description or "")
                views = info.get("view_count",0)
                likes = info.get("like_count",0)
                date = info.get("upload_date")

                data.append({
                    "Title":title,
                    "Description": description,
                    "Embedded_Tags": tags,
                    "Hashtags":hashtags,
                    "No_Of_Views":views,
                    "No_Of_Likes":likes,
                    "Upload_Date":date,
                    "Shorts_Link":link,
                })

            except Exception as e:
                st.warning(f"Failed to extractL {link} | Reason: {e}")
    return pd.DataFrame(data)


#====== Streamlit App Ui=========
st.set_page_config(page_title="Youtube Shorts Metadata Scrapper",layout="wide")
st.title("Shorts Metadata Scrapper")

channel_url = st.text_input("Enter the channel url (Ex : 'https://www.youtube.com/channel_name/shorts' )")

if st.button("Scrap contents"):
    if "shorts" not in channel_url:
        st.error("Make sure the link ends with `/shorts`.")
    else:
        with st.spinner(f"Fetching you the requested metadata from {channel_url}"):
            shorts_link = short_link_fetcher(channel_url)
            df = meta_data_extractor(shorts_link)
            if not df.empty:
                st.success(f"Found {len(df)} Shorts!")
                st.dataframe(df)
                csv = df.to_csv(index=False).encode("utf-8")
                st.download_button(
                    label="Download Meta-Data As CSV",
                    data=csv,
                    file_name="Metadata_yt_shorts.csv",
                    mime="text/csv",
                )
            else:
                st.warning("No Shorts Metadata Extracted.")



