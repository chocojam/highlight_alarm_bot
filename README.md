# highlight_alarm_bot

# 📢 어라운드어스 공지사항 텔레그램 알림 봇

어라운드어스 엔터테인먼트(Around US Ent)의 아티스트 공지사항을 주기적으로 감지하여 새로운 글이 등록되면 텔레그램으로 알림을 보내주는 자동화 파이프라인 프로젝트입니다.

---

## 📌 주요 특징

| 항목 | 내용 |
| :--- | :--- |
| **자동 감지** | GitHub Actions를 활용해 15분마다 웹사이트 크롤링 실행 |
| **무료 구동** | 서버 비용 없이 100% 무료(GitHub 무료 분량)로 24시간 작동 |
| **중복 방지** | `last_notice.txt` 상태 관리로 동일한 공지사항 중복 알림 방지 |
| **보안 유지** | Telegram API Token 및 Chat ID는 GitHub Repository Secrets로 보호 |

---

## 🛠️ 기술 스택

* **Language**: Python 3.10
* **Library**: `requests`, `beautifulsoup4`
* **Automation**: GitHub Actions
* **Notification**: Telegram Bot API

---

## 📁 프로젝트 구조

```text
.
├── .github/
│   └── workflows/
│       └── notice_check.yml    # GitHub Actions 자동화 워크플로우
├── bot.py                      # 공지사항 크롤링 및 텔레그램 전송 스크립트
├── last_notice.txt             # 마지막 감지 공지 제목 (자동 생성)
└── README.md                   # 프로젝트 설명 문서
