# npb_standing.py
from config import LEAGUE_MAP, NPB_LOGOS, LEAGUE_TITLES


def extract_standings(driver, url_c, url_p):
  driver.get(url_c)

  driver.get(url_p)
