# Week 5 Submission - Reporting, Analysis & Automation Implementation


## Nội dung package

Package này bao gồm đầy đủ Week 5 từ đầu đến cuối:

1. Chuẩn bị dữ liệu ticket Week 4
2. Tạo báo cáo Odoo
3. Phân tích pattern và impact
4. Findings & recommendations
5. Phân tích Login Issue
6. Thiết kế + implement automation có Odoo API/Webhook
7. Test workflow automation
8. Documentation + KB + operation guide
9. Final presentation outline
10. Submission checklist

## Cấu trúc folder

```text
week-5-submission-pro/
├── overview/
├── ticket-data-summary/
├── odoo-reports/
├── pattern-analysis/
├── findings-recommendations/
├── login-issue-problem-analysis/
├── login-issue-automation/
│   ├── src/
│   ├── config/
│   ├── data/
│   ├── docs/
│   ├── tests/
│   └── logs/
├── presentation/
├── evidence/screenshots/
└── submission-checklist/
```

## Điểm nổi bật 

- Có **Odoo API client thật bằng XML-RPC**.
- Có **webhook server** để nhận event từ Odoo/external automation.
- Có **scheduled job runner** để chạy định kỳ.
- Có **mock mode** để chạy demo không cần Odoo thật.
- Có **unit test** và test result.
- Có **action plan giảm ticket volume**.
- Có **monitoring metrics sau automation**.
- Toàn bộ tài liệu viết bằng **tiếng Việt**.

## Cách chạy demo automation

```bash
cd 06-login-issue-automation
python src/automation_demo.py
```

## Cách chạy test

```bash
cd 06-login-issue-automation
python -m unittest discover -s tests
```

## Cách chạy scheduled job với Odoo API thật

1. Copy file config:

```bash
cp config/config.example.env config/.env
```

2. Điền thông tin Odoo:

```text
ODOO_URL=
ODOO_DB=
ODOO_USERNAME=
ODOO_API_KEY=
```

3. Chạy:

```bash
python src/run_scheduled_odoo.py
```

## Evidence cần bổ sung

Ảnh Odoo của bạn nên để vào:

```text
08-evidence/screenshots/
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
| Recurring ticket patterns are identified | `03-pattern-analysis/week-5-pattern-analysis.md` |
| Findings and recommendations documented | `04-findings-recommendations/week-5-findings-recommendations.md` |
| Automation workflow implemented | `06-login-issue-automation/src/automation_demo.py` |
| Auto-analyzes tickets, checks HR, processes accordingly | `06-login-issue-automation/src/login_automation_service.py` |
| Integrates with Odoo ticket system webhook/API | `06-login-issue-automation/src/odoo_api_client.py`, `06-login-issue-automation/src/webhook_server.py`, `06-login-issue-automation/docs/api-integration.md` |
| Action plan to reduce ticket volume | `04-findings-recommendations/week-5-findings-recommendations.md` |
