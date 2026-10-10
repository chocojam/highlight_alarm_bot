import os
import requests
from bs4 import BeautifulSoup

TOKEN = os.environ.get("TELEGRAM_TOKEN")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")
URL = "https://www.aroundusent.com/artistNotice/list?artist_idx=1"
STATE_FILE = "last_notice.txt"


def send_telegram(text):
  api_url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
  payload = {"chat_id": CHAT_ID, "text": text, "parse_mode": "HTML"}
  requests.post(api_url, data=payload)


def check_update():
  headers = {
      "User-Agent": (
          "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
      )
  }
  res = requests.get(URL, headers=headers)
  if res.status_code != 200:
    print("웹페이지 접속 실패")
    return

  soup = BeautifulSoup(res.text, "html.parser")
  target_elements = soup.select(".board_list a, .board-list a, table a")

  if not target_elements:
    print("공지사항 요소를 찾지 못함")
    return

  latest_title = target_elements[0].get_text().strip()
  latest_link = target_elements[0].get("href", "")

  if not latest_link.startswith("http"):
    latest_link = "https://www.aroundusent.com" + latest_link

  last_title = ""
  if os.path.exists(STATE_FILE):
    with open(STATE_FILE, "r", encoding="utf-8") as f:
      last_title = f.read().strip()

  if last_title != "" and latest_title != last_title:
    message = (
        f"🚨 <b>새로운 공지사항 등록</b>\n\n{latest_title}\n\n🔗 {latest_link}"
    )
    send_telegram(message)
    print(f"알림 발송 완료: {latest_title}")
  elif last_title == "":
    print(f"최초 실행: 기준 제목 설정 ({latest_title})")
  else:
    print("새로운 공지사항 없음")

  with open(STATE_FILE, "w", encoding="utf-8") as f:
    f.write(latest_title)


if __name__ == "__main__":
  check_update()
