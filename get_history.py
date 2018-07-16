# -*- coding: utf-8 -*-
import sqlite3
import sys
import os
import time
import datetime
reload(sys)
sys.setdefaultencoding( "utf-8" )

history_db = '/Users/truexinology/truexin/python/chrome-history-email/History'

# 1.连接history_db
c = sqlite3.connect(history_db)
cursor = c.cursor()

# 2.选取我们想要的网址和访问时间
try:
    select_statement = "SELECT url,title,datetime(last_visit_time/1000000-11644473600,'unixepoch','localtime') AS tm FROM urls WHERE julianday('now') - julianday(tm) < 1 ORDER BY tm DESC;"
    cursor.execute(select_statement)
except sqlite3.OperationalError:
    print("[!] The database is locked! Please exit Chrome and run the script again.")
    quit()

# 3.将网址和访问时间存入result.txt文件
results = cursor.fetchall()
# ticks = time.time()
timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

with open('/Users/truexinology/truexin/python/chrome-history-email/logs/result.txt','w') as f:
    for i in range(len(results)):
        f.write(results[i][2]+'\n')
        f.write(results[i][1]+'\n')
        f.write(results[i][0]+'\n')

with open('/Users/truexinology/truexin/python/chrome-history-email/result.txt','w') as f:
    for i in range(len(results)):
        f.write(results[i][2]+'\n')
        f.write(results[i][1]+'\n')
        f.write(results[i][0]+'\n')

# os.rename('/Users/truexinology/truexin/python/chrome-history-email/logs/result.txt','/Users/truexinology/truexin/python/chrome-history-email/logs/%s.txt' % ticks)
os.rename('/Users/truexinology/truexin/python/chrome-history-email/logs/result.txt','/Users/truexinology/truexin/python/chrome-history-email/logs/%s.txt' % timestamp)
