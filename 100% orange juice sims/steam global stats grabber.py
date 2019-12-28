from steam import *
import datetime
chars = ["DLC21", "DLC20B", "DLC20A", "DLC19B", "DLC19A",
         "DLC17B", "DLC17A", "DLC16B", "DLC16A", "DLC15B",
         "SUGV2", "DLC15B", "DLC15A", "DLC13B", "DLC13A",
         "DLC11B", "DLC11A", "ARUS", "SWEETBREAKER",
         "STARBREAKER", "SORAMILITARY", "SHERRY", "SHAM",
         "MIXEDPOPPO", "KYOKO", "ALTE", "KAE", "KRILA",
         "KYOUSUKE", "SAKI", "QPD", "SYURA", "NANAKO",
         "SEAGULL", "ROBOT", "CHICKEN", "CASTLE",
         "BOSSROBOT", "MANAGER", "TOMOMO", "POPPO", "KAI",
         "PEAT", "FERNET", "MARC", "SUGURI", "ARU", "YUKI", "QP"]
steam_stats = {}

# Controls the time period we collect stats from in days
collection_period = 30

startdate =  str((datetime.date.today() - datetime.timedelta(collection_period)).strftime("%s"))
enddate = str(datetime.date.today().strftime("%s") )

# create keys for steam api query
for char in chars:
    request_string_wins = "STAT_" + char + "_ONLINE_GAMES"
    request_string_games = "STAT_" + char + "_ONLINE_WINS"
    steam_stats[char] = {}
    steam_stats[char][request_string_wins] = 0
    steam_stats[char][request_string_games] = 0

# build urls
for char in steam_stats:
    for stat in steam_stats[char]:
        url ="https://api.steampowered.com/ISteamUserStats/GetGlobalStatsForGame/v1/?appid=282800&count=1&name[0]=" + stat + "&startdate="+ startdate + "&enddate=" + enddate
        response=webapi.webapi_request(url)
        total = 0
        for data in response["response"]["globalstats"][stat]["history"]:
          total += int(data["total"])

        steam_stats[char][stat] = total

# calculate winrates        
for char in steam_stats:
    wins = steam_stats[char]["STAT_" + char + "_ONLINE_WINS"]
    games = steam_stats[char]["STAT_" + char + "_ONLINE_GAMES"]
    steam_stats[char][char+"_WINRATE"] = wins / games * 100

for char in steam_stats:
    print(steam_stats[char])
    print("\n")
