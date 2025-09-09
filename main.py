import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from datetime import datetime, timedelta
from pytz import timezone
from github_setting import get_github_repo, upload_github_issue
from config import TODAY_DATE_STR, YESTERDAY_DATE_STR, YEAR, MONTH
from npb_scores import extract_scores, generate_md_table
from npb_standings import extract_standings, generate_md_table_standings


# 크롬 드라이버 자동 설치 및 실행
def execute_driver():
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
    
    return driver


if __name__ == "__main__":
    # URL 설정 (연도와 날짜 자동 반영)
    url_scores = f'https://npb.jp/bis/eng/{YEAR}/games/gm{YESTERDAY_DATE_STR}.html'
    url_standing_c = f'https://npb.jp/bis/eng/{YEAR}/stats/std_c.html'
    url_standing_p = f'https://npb.jp/bis/eng/{YEAR}/stats/std_p.html'

    driver = execute_driver()
    driver.get(url_scores)

    # 경기 정보 파싱
    scores = extract_scores(driver)

    # Markdown 생성
    md_contents = generate_md_table(scores)

    # 저장
    folder = os.path.join("NPB_scores", str(YEAR), f"{MONTH:02d})
    os.makedirs(folder, exist_ok=True)
    filename = os.path.join(folder, f"NPB_baseball_{YESTERDAY_DATE_STR}.md")

    with open(filename, "w", encoding="utf-8") as f:
        f.write(md_contents)

    print(f"Markdown file created: {filename}")

    # 순위 정보 파싱
    standings = extract_standings(driver, url_standing_c, url_standing_p)
    
    # Markdown 생성
    md_contents = generate_md_table_standings(standings)
    
    # 저장
    folder = "NPB_standings"
    os.makedirs(folder, exist_ok=True)
    filename = os.path.join(folder, f"NPB_baseball_{YEAR}.md")

    with open(filename, "w", encoding="utf-8") as f:
        f.write(md_contents)

    print(f"Markdown file created: {filename}")

    driver.quit()
