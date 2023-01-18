from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
from time import sleep


driver = webdriver.Chrome()
trending_youtube_url = 'https://www.youtube.com/feed/trending?bp=4gIKGgh0cmFpbGVycw%3D%3D'
driver.get(trending_youtube_url)


def get_driver():
   chrome_options = Options()
   chrome_options.add_argument('--headless')
   chrome_options.add_argument('--no-sandbox')
   chrome_options.add_argument('--disable-dev-shm-usage')
   chrome_options.add_argument("--disable-setuid-sandbox")
   driver = webdriver.Chrome(options=chrome_options)

   return driver


def get_videos(driver):
    video_div_class = 'ytd-video-renderer'
    driver.get(trending_youtube_url)
    sleep(5)
    videos = driver.find_elements(By.TAG_NAME, video_div_class)
    return videos


videos_list = []


def parse_videos(video):
    #title, url, thumbnail, channel name, views, uploaded date and description
    title_tag = video.find_element(By.ID, 'video-title')
    title = title_tag.text
    url = title_tag.get_attribute('href')
    thumbnail_tag = video.find_element(By.TAG_NAME, 'img')
    thumbnail_url = thumbnail_tag.get_attribute('src')
    channel_div = video.find_element(By.CLASS_NAME, 'ytd-channel-name')
    channel = channel_div.text
    views = video.find_element(By.XPATH,
                               '//*[@id="metadata-line"]/span[1]').text
    uploaded = video.find_element(By.XPATH,
                                  '//*[@id="metadata-line"]/span[2]').text
    description_tag = video.find_element(By.ID, 'description-text')
    description = description_tag.text


    result = {
        'title ': title,
        'url ': url,
        'thumbnail_url ': thumbnail_url,
        'channel name ': channel,
        'views ': views,
        'uploaded ': uploaded,
        'description ': description
    }
    videos_list.append(result)
    return result

if __name__ == '__main__':
    driver = get_driver()
    get_videos(driver)
    videos = get_videos(driver)
    print(f'Found {len(videos)} videos.')
    for video in videos:
        parse_videos(video)
    videos_df = pd.DataFrame(videos_list)   
    videos_df.to_csv('YT_trending_movies.csv', index=None)
