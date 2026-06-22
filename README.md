# Week 5 Submission - Reporting, Analysis & Automation Implementation

## Tổng quan

Package này là phần nộp Week 5, gồm hai phần chính:

1. **Reporting & Analysis:** dùng dữ liệu ticket từ Week 4 để tạo báo cáo, phân tích pattern, đánh giá impact và đưa ra recommendation.
2. **Automation Implementation:** thiết kế và implement workflow automation cho Scenario 1 - Login Issue theo hướng Operating Engineer.

Mình giữ tên file, folder và code bằng tiếng Anh để dễ đọc trên GitHub. Nội dung các file `.md` được viết bằng tiếng Việt để dễ review và trình bày.

## Cấu trúc package

Các file tài liệu chính được đặt ngay ở root để dễ mở và review. Những phần có nhiều file như automation source code, docs, tests, logs và evidence vẫn được giữ trong folder riêng.

```text
week-5-submission-pro/
├── README.md
├── overview.md
├── ticket-data-summary.md
├── odoo-reports.md
├── pattern-analysis.md
├── findings-recommendations.md
├── login-issue-problem-analysis.md
├── final-presentation-outline.md
├── submission-checklist.md
├── login-issue-automation/
│   ├── README.md
│   ├── requirements.txt
│   ├── demo-output.txt
│   ├── test-output.txt
│   ├── src/
│   ├── config/
│   ├── data/
│   ├── docs/
│   ├── tests/
│   └── logs/
└── evidence/
    └── screenshots/
```

## Nội dung chính

| Phần | File / Folder | Mục đích |
|---|---|---|
| Overview | `overview.md` | Tóm tắt mục tiêu và cách tiếp cận Week 5 |
| Ticket data | `ticket-data-summary.md` | Tổng hợp 6 ticket Week 4 dùng làm dữ liệu phân tích |
| Odoo reports | `odoo-reports.md` | Báo cáo ticket summary, team performance, category và trend |
| Pattern analysis | `pattern-analysis.md` | Phân tích issue lặp lại, impact và root cause ban đầu |
| Findings | `findings-recommendations.md` | Findings, recommendations và action plan giảm ticket volume |
| Problem analysis | `login-issue-problem-analysis.md` | Giải thích vì sao chọn Login Issue để automation |
| Automation | `login-issue-automation/` | Code, API/Webhook, tests, docs và log cho automation |
| Presentation | `final-presentation-outline.md` | Outline trình bày cuối Week 5 |
| Checklist | `submission-checklist.md` | Checklist tự kiểm tra trước khi nộp |
| Evidence | `evidence/screenshots/` | Ảnh Odoo ticket list và ticket details |

## Điểm nổi bật

- Có phân tích dữ liệu ticket từ Week 4 thay vì chỉ làm automation.
- Có Odoo reports, pattern analysis, impact analysis và action plan.
- Có automation workflow cho Scenario 1 - Login Issue.
- Có Odoo API client bằng XML-RPC.
- Có webhook server để mô phỏng hướng tích hợp event-based.
- Có scheduled runner để mô phỏng hướng chạy định kỳ.
- Có mock mode để chạy demo không cần Odoo thật.
- Có unit test, demo output, test output và operation guide.
- Có KB article cho Login Issue để support có thể xử lý thủ công khi cần.

## Cách chạy demo automation

```bash
cd login-issue-automation
python src/automation_demo.py
```

## Cách chạy test

```bash
cd login-issue-automation
python -m unittest discover -s tests
```

## Cách chạy với Odoo API thật

1. Copy file config mẫu:

```bash
cp config/config.example.env config/.env
```

2. Điền thông tin Odoo:

```text
ODOO_URL=https://your-odoo-domain.com
ODOO_DB=your_database
ODOO_USERNAME=your_email@example.com
ODOO_API_KEY=your_api_key
```

3. Chạy scheduled job:

```bash
python src/run_scheduled_odoo.py
```

## Evidence

Ảnh Odoo để trong:

```text
evidence/screenshots/
```

Các ảnh nên có:

- Ticket list view 6 ticket
- Ticket detail 00001 Login Issue
- Ticket detail 00002 Performance Issue
- Ticket detail 00003 Critical Bug
- Ticket detail 00004 Feature Request
- Ticket detail 00005 Video Playback
- Ticket detail 00006 Fixed Deadline Request

## Acceptance Criteria Coverage

| Acceptance Criteria | File chứng minh |
|---|---|
| Recurring ticket patterns are identified | `pattern-analysis.md` |
| Findings and recommendations with evidence are documented | `findings-recommendations.md` |
| Automation workflow implemented for Scenario 1 | `login-issue-automation/src/login_automation_service.py` |
| Workflow auto-analyzes tickets, checks HR system, and processes accordingly | `login-issue-automation/src/detector.py`, `login-issue-automation/src/hr_client.py`, `login-issue-automation/src/login_automation_service.py` |
| Workflow integrates with Odoo ticket system webhook/API | `login-issue-automation/src/odoo_api_client.py`, `login-issue-automation/src/webhook_server.py`, `login-issue-automation/docs/api-integration.md` |
| Action plan to reduce ticket volume is developed | `findings-recommendations.md` |

