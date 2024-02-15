import pandas as pd

match_title = [
    "第1週-女 2：臺北鯨華 vs 高雄台電 (10月14日)",
    "第2週-女 8：新北中纖 vs 臺北鯨華 (11月04日)",
    "第2週-女 12：臺北鯨華 vs 凱撒飯店連鎖 (11月05日)",
    "第3週-女 13：臺北鯨華 vs 極速超跑 (11月11日)",
    "第3週-女 16：高雄台電 vs 臺北鯨華 (11月12日)",
    "第5週-女 26：高雄台電 vs 臺北鯨華 (11月25日)",
    "第5週-女 28：極速超跑 vs 臺北鯨華 (11月26日)",
    "第8週-女 43：極速超跑 vs 臺北鯨華 (12月16日)",
    "第8週-女 46：臺北鯨華 vs 凱撒飯店連鎖 (12月17日)",
    "第9週-女 49：新北中纖 vs 臺北鯨華 (12月23日)",
    "第9週-女 52：臺北鯨華 vs 新北中纖 (12月24日)",
    "第10週-女 58：臺北鯨華 vs 凱撒飯店連鎖 (01月07日)"
]

for mach in match_title:
    table_csv = pd.read_csv('Matches/results/' + mach + '.csv')
    table_csv.to_html('Matches/results/html/' + mach + '.html')
