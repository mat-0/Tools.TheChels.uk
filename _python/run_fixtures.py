import re
import requests
from datetime import datetime, timedelta
from bs4 import BeautifulSoup

link ="https://www.live-footballontv.com/live-english-football-on-tv.html"

def add_suffix(day):
    if 4 <= day <= 20 or 24 <= day <= 30:
        suffix = "th"
    else:
        suffix = ["st", "nd", "rd"][day % 10 - 1]
    return suffix

def format_date(date):
    suffix = add_suffix(date.day)
    formatted_date = date.strftime(f'%A {date.day}{suffix} %B %Y')
    return formatted_date


page = requests.get(link)
today = format_date(datetime.now())
tomorrow = format_date(datetime.now() + timedelta(days=1))
print(today, tomorrow)
match = re.search(f'{today}(.*?){tomorrow}', page.text, re.DOTALL)
print(match)
if match:
    content = match.group(1)
    soup = BeautifulSoup(content, 'html.parser')
    body_text = ' - '.join(soup.stripped_strings)
    matches = []
    for line in body_text.split(' - '):
        if ' v ' in line:
            matches.append(line)
    if not matches:
        print("- No fixtures found")
    print("\n".join([f"- {match}" for match in matches]))
else:
    print("- No Fixtures")
