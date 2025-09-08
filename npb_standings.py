# npb_standing.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from datetime import datetime
from config import LEAGUE_MAP, NPB_LOGOS, LEAGUE_TITLES


def extract_standings(driver, url_c, url_p):
    results = {
        "central": [],
        "pacific": [],
        "interleague": []
    }

    # --- Central League ---
    driver.get(url_c)
    central_prefix = '//*[@id="stdivmaintbl"]/table/tbody/tr/td/div[1]/table/tbody/tr[2]/td[1]/table/tbody/tr/td'
    central_rows = driver.find_elements(By.XPATH, central_prefix + '/..')
    for i in range(1, len(central_rows)+1):
        try:
            team = driver.find_element(By.XPATH, f'{central_prefix}[{i}]/td[2]').text.strip()
            game = driver.find_element(By.XPATH, f'{central_prefix}[{i}]/td[3]').text.strip()
            win = driver.find_element(By.XPATH, f'{central_prefix}[{i}]/td[4]').text.strip()
            lose = driver.find_element(By.XPATH, f'{central_prefix}[{i}]/td[5]').text.strip()
            tie = driver.find_element(By.XPATH, f'{central_prefix}[{i}]/td[6]').text.strip()
            pct = driver.find_element(By.XPATH, f'{central_prefix}[{i}]/td[7]').text.strip()
            gb = driver.find_element(By.XPATH, f'{central_prefix}[{i}]/td[8]').text.strip()
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
    pacific_prefix = '//*[@id="stdivmaintbl"]/table/tbody/tr/td/div[1]/table/tbody/tr[2]/td[2]'
    pacific_rows = driver.find_elements(By.XPATH, pacific_prefix + '/table/tbody/tr/td')
    for i in range(1, len(pacific_rows)+1):
        try:
            team = driver.find_element(By.XPATH, f'{central_prefix}[{i}]/td[2]').text.strip()
            game = driver.find_element(By.XPATH, f'{central_prefix}[{i}]/td[3]').text.strip()
            win = driver.find_element(By.XPATH, f'{central_prefix}[{i}]/td[4]').text.strip()
            lose = driver.find_element(By.XPATH, f'{central_prefix}[{i}]/td[5]').text.strip()
            tie = driver.find_element(By.XPATH, f'{central_prefix}[{i}]/td[6]').text.strip()
            pct = driver.find_element(By.XPATH, f'{central_prefix}[{i}]/td[7]').text.strip()
            gb = driver.find_element(By.XPATH, f'{central_prefix}[{i}]/td[8]').text.strip()
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
        

def generate_md_table_standings(standings):
    a