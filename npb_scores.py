# npb_scores.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from datetime import datetime
from config import LEAGUE_MAP, NPB_LOGOS, LEAGUE_TITLES


def parse_games(driver, rows, base_prefix):
    """개별 리그의 경기 정보 파싱"""
    games = []
    for i in range(1, len(rows) + 1):
        base_xpath = f"{base_prefix}[{i}]"
        try:
            home = driver.find_element(By.XPATH, base_xpath + '/td[2]').text
            home_score = driver.find_element(By.XPATH, base_xpath + '/td[3]').text
            away_score = driver.find_element(By.XPATH, base_xpath + '/td[5]').text
            away = driver.find_element(By.XPATH, base_xpath + '/td[6]').text
            score = home_score + " - " + away_score

            games.append({"home": home, "score": score, "away": away})
        except Exception as e:
            print(f"데이터 없음 (row {i}): {e}")
    return games
    
def extract_scores(driver):
    results = {key: [] for key in LEAGUE_TITLES.keys()}
    
    # --- 리그 개수 확인 ---
    leagues = driver.find_elements(By.XPATH, '//*[@id="gmdivlist"]/div/table/tbody/tr[1]/td')

    if len(leagues) == 1:
        # 리그 1개일 때
        league_name = driver.find_element(
            By.XPATH, '//*[@id="gmdivlist"]/div/table/tbody/tr[1]/td/div/table/tbody/tr/td[2]/div'
        ).text.strip()
        league_key = LEAGUE_MAP.get(league_name, "unknown")
        game_rows = driver.find_elements(
            By.XPATH, '//*[@id="gmdivlist"]/div/table/tbody/tr[2]/td/div/table/tbody/tr'
        )
        results[league_key] = parse_games(driver, game_rows, base_prefix='//*[@id="gmdivlist"]/div/table/tbody/tr[2]/td/div/table/tbody/tr')
    elif len(leagues) == 2:
        # 리그 2개일 때
        for idx in range(1, 3):
            league_name = driver.find_element(
                By.XPATH, f'//*[@id="gmdivlist"]/div/table/tbody/tr[1]/td[{idx}]/div/table/tbody/tr/td[2]/div'
            ).text.strip()
            league_key = LEAGUE_MAP.get(league_name, "unknown")
            game_rows = driver.find_elements(
                By.XPATH, f'//*[@id="gmdivlist"]/div/table/tbody/tr[2]/td[{idx}]/div/table/tbody/tr'
            )
            results[league_key] = parse_games(driver, game_rows, base_prefix=f'//*[@id="gmdivlist"]/div/table/tbody/tr[2]/td[{idx}]/div/table/tbody/tr')

    return results
    
def generate_md_table(scores):
    """
    여러 경기 리스트를 받아서 HTML 테이블 포함 Markdown 생성
    """
    md_contents = "## 오늘의 경기 결과\n\n\n"

    for league, games in scores.items():
        title = LEAGUE_TITLES.get(league, league)
        md_contents += f"### ⚾ {title}\n\n"

        if len(games) == 0:
            md_contents += "<br></br>\n"
        else:
            md_contents += "<table>\n"
            md_contents += f"  <tr>\n    <th></th>\n    <th colspan='3'>{title}</th>\n    <th></th>\n  </tr>\n"
            for game in games:
                home_logo = NPB_LOGOS.get(league, {}).get(game['home'], "")
                away_logo = NPB_LOGOS.get(league, {}).get(game['away'], "")

                md_contents += (
                    f"  <tr>\n"
                    f"    <td><img src='{home_logo}' width='30'></td>\n"
                    f"    <td>{game['home']}</td><td>{game['score']}</td><td>{game['away']}</td>\n"
                    f"    <td><img src='{away_logo}' width='30'></td>\n"
                    f"  </tr>\n"
                )
            md_contents += "</table>\n\n"

    return md_contents
