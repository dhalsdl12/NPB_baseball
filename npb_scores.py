# npb_scores.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from datetime import datetime


def extract_scores(driver):
    central_games = []
    pacific_games = []

    c_home = driver.find_element(By.XPATH, '//*[@id="gmdivlist"]/div/table/tbody/tr[2]/td[1]/div/table/tbody/tr[1]/td[2]').text
    c_away = driver.find_element(By.XPATH, '//*[@id="gmdivlist"]/div/table/tbody/tr[2]/td[1]/div/table/tbody/tr[1]/td[6]').text
    c_home_score = driver.find_element(By.XPATH, '//*[@id="gmdivlist"]/div/table/tbody/tr[2]/td[1]/div/table/tbody/tr[1]/td[3]').text
    c_away_score = driver.find_element(By.XPATH, '//*[@id="gmdivlist"]/div/table/tbody/tr[2]/td[1]/div/table/tbody/tr[1]/td[5]').text
    c_score = c_home_score + ' - ' + c_away_score
    central_games.append({"home": c_home, "score": c_score, "away": c_away})

    return {"central": central_games, "pacific": pacific_games}


def generate_md_table(scores):
    """
    여러 경기 리스트를 받아서 HTML 테이블 포함 Markdown 생성
    """
    md_contents = "# 오늘의 경기 결과\n\n<table>\n"
    md_contents += "  <tr>\n    <th></th>\n    <th colspan='3'>센트럴리그</th>\n    <th colspan='3'>퍼시픽리그</th>\n    <th></th>\n  </tr>\n"

    # 가장 많은 경기 수 기준으로 반복
    max_games = max(len(scores['central']), len(scores['pacific']))
    for i in range(max_games):
        central = scores['central'][i] if i < len(scores['central']) else {"home": "", "score": "", "away": ""}
        pacific = scores['pacific'][i] if i < len(scores['pacific']) else {"home": "", "score": "", "away": ""}
        md_contents += f"  <tr>\n    <td></td>\n"
        md_contents += f"    <td>{central['home']}</td><td>{central['score']}</td><td>{central['away']}</td>\n"
        md_contents += f"    <td>{pacific['home']}</td><td>{pacific['score']}</td><td>{pacific['away']}</td>\n"
        md_contents += f"    <td></td>\n  </tr>\n"

    md_contents += "</table>\n"
    return md_contents