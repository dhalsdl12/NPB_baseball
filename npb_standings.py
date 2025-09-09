# npb_standing.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from datetime import datetime
from config import LEAGUE_MAP, NPB_LOGOS, LEAGUE_TITLES, TEAM_NAME_MAP


def extract_standings(driver, url_c, url_p):
    results = {
        "central": [],
        "pacific": [],
        "interleague": []
    }

    # --- Central League ---
    driver.get(url_c)
    central_prefix = '//*[@id="stdivmaintbl"]/table/tbody/tr/td/div[1]/table/tbody/tr'
    for i in range(2, 8):
        try:
            team = driver.find_element(By.XPATH, f'{central_prefix}[{i}]/td[1]/table/tbody/tr/td[2]').text.strip()
            game = driver.find_element(By.XPATH, f'{central_prefix}[{i}]/td[2]').text.strip()
            win = driver.find_element(By.XPATH, f'{central_prefix}[{i}]/td[3]').text.strip()
            lose = driver.find_element(By.XPATH, f'{central_prefix}[{i}]/td[4]').text.strip()
            tie = driver.find_element(By.XPATH, f'{central_prefix}[{i}]/td[5]').text.strip()
            pct = driver.find_element(By.XPATH, f'{central_prefix}[{i}]/td[6]').text.strip()
            gb = driver.find_element(By.XPATH, f'{central_prefix}[{i}]/td[7]').text.strip()
            results["central"].append({
                "team": team,
                "G": game,
                "W": win,
                "L": lose,
                "T": tie,
                "PCT": pct,
                "GB": gb
            })
        except Exception as e:
            print(f"Central row {i} error: {e}")
    
    
    # --- Pacific League ---
    driver.get(url_p)
    pacific_prefix = '//*[@id="stdivmaintbl"]/table/tbody/tr/td/div[1]/table/tbody/tr'
    for i in range(2, 8):
        try:
            team = driver.find_element(By.XPATH, f'{pacific_prefix}[{i}]/td[1]/table/tbody/tr/td[2]').text.strip()
            game = driver.find_element(By.XPATH, f'{pacific_prefix}[{i}]/td[2]').text.strip()
            win = driver.find_element(By.XPATH, f'{pacific_prefix}[{i}]/td[3]').text.strip()
            lose = driver.find_element(By.XPATH, f'{pacific_prefix}[{i}]/td[4]').text.strip()
            tie = driver.find_element(By.XPATH, f'{pacific_prefix}[{i}]/td[5]').text.strip()
            pct = driver.find_element(By.XPATH, f'{pacific_prefix}[{i}]/td[6]').text.strip()
            gb = driver.find_element(By.XPATH, f'{pacific_prefix}[{i}]/td[7]').text.strip()
            results["pacific"].append({
                "team": team,
                "G": game,
                "W": win,
                "L": lose,
                "T": tie,
                "PCT": pct,
                "GB": gb
            })
        except Exception as e:
            print(f"Pacific row {i} error: {e}")
    
    return results


def generate_md_table_standings(standings):
    """
    standings 리스트를 HTML 테이블(Markdown에 포함 가능)로 변환
    """
    md = "## NPB Standings\n\n"
    for league, rows in standings.items():
        title = LEAGUE_TITLES.get(league, league)
        md += f"#### {title}\n\n"
        if not rows:
            md += "데이터 없음!\n\n"
            continue

        # 테이블 헤더
        md += (
            "<table>\n"
            "<tr>"
            "<th></th><th>Team</th><th>G</th><th>W</th><th>L</th><th>T</th><th>PCT</th><th>GB</th>"
            "</tr>\n"
        )

        # 각 팀 데이터
        for r in rows:
            team_name = r['team'].replace("\n", " ")
            team_key = TEAM_NAME_MAP.get(team_name, team_name)
            logo = NPB_LOGOS.get(league, {}).get(team_key, "")
            print(team_name, team_key, logo)
            
            md += (
                f"<tr>"
                f"    <td><img src='{logo}' width='30'></td>\n"
                f"<td>{r['team']}</td>"
                f"<td>{r['G']}</td>"
                f"<td>{r['W']}</td>"
                f"<td>{r['L']}</td>"
                f"<td>{r['T']}</td>"
                f"<td>{r['PCT']}</td>"
                f"<td>{r['GB']}</td>"
                f"</tr>\n"
            )

        md += "</table>\n\n"
    return md
