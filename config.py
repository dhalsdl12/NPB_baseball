# config.py
from datetime import datetime, timedelta
from pytz import timezone


SEOUL_TZ = timezone('Asia/Seoul')
TODAY = datetime.now(SEOUL_TZ)
YESTERDAY = TODAY - timedelta(days=1)
TODAY_DATE_STR = TODAY.strftime('%Y%m%d')
YESTERDAY_DATE_STR = YESTERDAY.strftime('%Y%m%d')
YEAR = TODAY.year  # 연도 동적 처리

# --- 팀 이름 매핑 ---
TEAM_NAME_MAP = {
    "Hanshin Tigers": "Hanshin",
    "Yomiuri Giants": "Yomiuri",
    "Hiroshima Toyo Carp": "Hiroshima",
    "Chunichi Dragons": "Chunichi",
    "Tokyo Yakult Swallows": "Yakult",
    "YOKOHAMA DeNA BAYSTARS": "DeNA",

    "Saitama Seibu Lions": "Seibu",
    "Chiba Lotte Marines": "Lotte",
    "Orix Buffaloes": "ORIX",
    "Hokkaido Nippon-Ham Fighters	": "Nippon-Ham",
    "Fukuoka SoftBank Hawks": "SoftBank",
    "Tohoku Rakuten Golden Eagles": "Rakuten",
}

# --- 팀 로고 ---
NPB_LOGOS = {
    "central": {
        "DeNA": f"https://npb.jp/bis/images/pet{YEAR}_db_1.gif",
        "Yakult": f"https://npb.jp/bis/images/pet{YEAR}_s_1.gif",
        "Chunichi": f"https://npb.jp/bis/images/pet{YEAR}_d_1.gif",
        "Yomiuri": f"https://npb.jp/bis/images/pet{YEAR}_g_1.gif",
        "Hanshin": f"https://npb.jp/bis/images/pet{YEAR}_t_1.gif",
        "Hiroshima": f"https://npb.jp/bis/images/pet{YEAR}_c_1.gif"
    },
    "pacific": {
        "Seibu": f"https://npb.jp/bis/images/pet{YEAR}_l_1.gif",
        "Lotte": f"https://npb.jp/bis/images/pet{YEAR}_m_1.gif",
        "ORIX": f"https://npb.jp/bis/images/pet{YEAR}_b_1.gif",
        "Nippon-Ham": f"https://npb.jp/bis/images/pet{YEAR}_f_1.gif",
        "SoftBank": f"https://npb.jp/bis/images/pet{YEAR}_h_1.gif",
        "Rakuten": f"https://npb.jp/bis/images/pet{YEAR}_e_1.gif"
    }
}

# --- 리그 매핑 ---
LEAGUE_MAP = {
    "Central League": "central",
    "Pacific League": "pacific",
    "Interleague": "interleague",
    "C.L. Climax Series First Stage": "climax_central_first",
    "P.L. Climax Series First Stage": "climax_pacific_first",
    "C.L. Climax Series Final Stage": "climax_central_final",
    "P.L. Climax Series Final Stage": "climax_pacific_final",
    "Nippon Series": "nippon_series"
}

# --- 리그 제목 ---
LEAGUE_TITLES = {
    "central": "Central League",
    "pacific": "Pacific League",
    "interleague": "Interleague",
    "climax_central_first": "C.L. Climax Series First Stage",
    "climax_pacific_first": "P.L. Climax Series First Stage",
    "climax_central_final": "C.L. Climax Series Final Stage",
    "climax_pacific_final": "P.L. Climax Series Final Stage",
    "nippon_series": "Nippon Series",
}
