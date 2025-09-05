import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from datetime import datetime
from pytz import timezone
from github_setting import get_github_repo, upload_github_issue

  
def pageCrawl():
    xpath = '//*[@id="gmdivlist"]/div/table/tbody/tr[2]/td[1]/div/table/tbody/tr[1]/td[2]'
    element = driver.find_elements(By.XPATH, xpath)
    try:
        test.append(element.text)
    except:
        print("error")


def extract_article_data():
    upload_contents = ''

    for i in range(len(test)):
        url = '\"' + test[i] + '\"'
        upload_contents += content

    return upload_contents

# 크롬 드라이버 자동 설치 및 실행
def execute_driver():
    url = 'https://npb.jp/bis/eng/2025/games/gm20250904.html'
    '''
    chrome_driver = os.path.join('chromedriver')
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')
    service = ChromeService(executable_path=chrome_driver)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(url)
    '''
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    return driver


if __name__ == "__main__":
    access_token = os.environ['MY_GITHUB_TOKEN']
    repository_name = "NPB_baseball"
    seoul_timezone = timezone('Asia/Seoul')
    today = datetime.now(seoul_timezone)
    today_date = today.strftime("%Y년 %m월 %d일")
    
    test = []

    driver = execute_driver()
    pageCrawl()

    for i in range(len(test)):
        print(test[i])

    issue_title = f"NPB_baseball ({today_date})"
    upload_contents = extract_article_data()
    repo = get_github_repo(access_token, repository_name)
    upload_github_issue(repo, issue_title, upload_contents)
    print("Upload Github Issue Success!")
