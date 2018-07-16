#!/usr/bin/env bash
cp /Users/truexinology/Library/Application\ Support/Google/Chrome/Default/History /Users/truexinology/truexin/python/chrome-history-email/
python /Users/truexinology/truexin/python/chrome-history-email/get_history.py
python /Users/truexinology/truexin/python/chrome-history-email/send_mail.py
