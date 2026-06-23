# Week 5 - Reporting, Analysis & Automation Implementation

## Tổng quan

Đây là bài nộp Week 5, tập trung vào hai phần chính:

1. **Reporting & Analysis**: sử dụng dữ liệu ticket được cung cấp trong `doc/plans/data/sample.xlsx` để phân tích stage, priority, tag/category, pattern và impact.
2. **Automation Implementation**: xây dựng workflow automation cho Scenario 1 - Login Issue theo hướng Operating Engineer.

Phần báo cáo và phân tích được thực hiện dựa trên file data mẫu:

```text
doc/plans/data/sample.xlsx
```

Riêng phần automation được thiết kế để chạy trên ticket Odoo của em thông qua API/webhook. Workflow đọc ticket Login Issue từ Odoo, phân tích nội dung ticket, kiểm tra HR demo data, sau đó cập nhật note/tag/stage lại vào ticket Odoo.

---

## Mục tiêu Week 5

* Phân tích ticket patterns từ file `doc/plans/data/sample.xlsx`.
* Xác định và ưu tiên các vấn đề có khả năng lặp lại.
* Đề xuất hướng cải thiện để giảm ticket volume.
* Implement automation cho Scenario 1 - Login Issue.
* Tích hợp automation với Odoo ticket system thông qua API/webhook.
* Viết test, log và documentation cho workflow automation.

---

## Nguồn dữ liệu

Phần reporting/analysis sử dụng file:

```text
doc/plans/data/sample.xlsx
```

Dữ liệu này được dùng để tạo các phần:

* Ticket data summary
* Odoo reports
* Pattern analysis
* Findings and recommendations
* Final presentation outline

Các số liệu trong bài như tổng số ticket, stage distribution, priority distribution và tag analysis đều được lấy từ file data này.

---

## Cấu trúc bài nộp

```text
.
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
│   │   ├── automation_demo.py
│   │   ├── detector.py
│   │   ├── hr_client.py
│   │   ├── lms_client.py
│   │   ├── login_automation_service.py
│   │   ├── models.py
│   │   ├── odoo_api_client.py
│   │   ├── run_scheduled_odoo.py
│   │   └── webhook_server.py
│   ├── config/
│   │   └── config.example.env
│   ├── data/
│   │   └── hr_demo.json
│   ├── docs/
│   │   ├── api-integration.md
│   │   ├── kb-login-issue.md
│   │   ├── operation-guide.md
│   │   ├── test-results.md
│   │   └── workflow-design.md
│   ├── logs/
│   │   └── automation.log
│   └── tests/
│       └── test_login_automation.py
└── evidence/
    └── screenshots/
```

---

## Phần 1: Reporting & Analysis

Phần này sử dụng dữ liệu từ:

```text
doc/plans/data/sample.xlsx
```

Các file liên quan:

| File                            | Nội dung                                        |
| ------------------------------- | ----------------------------------------------- |
| `ticket-data-summary.md`        | Tổng hợp dữ liệu ticket từ file sample          |
| `odoo-reports.md`               | Báo cáo theo stage, priority, tag/category      |
| `pattern-analysis.md`           | Phân tích pattern, impact và root cause ban đầu |
| `findings-recommendations.md`   | Findings, recommendations và action plan        |
| `final-presentation-outline.md` | Outline trình bày cuối tuần                     |

Các nội dung chính đã làm:

* Tổng hợp ticket data từ file sample.
* Phân tích số lượng ticket theo stage.
* Phân tích ticket theo priority.
* Phân tích tag/category để tìm nhóm vấn đề nổi bật.
* Xác định các nhóm issue thường gặp.
* Đề xuất action plan để giảm ticket volume.

---

## Phần 2: Login Issue Automation

Phần automation tập trung vào **Scenario 1 - Login Issue**.

Lý do chọn Login Issue:

* Đây là dạng issue có khả năng lặp lại.
* Quy trình xử lý tương đối rõ ràng.
* Có thể nhận diện bằng keyword trong title/description.
* Có thể kiểm tra employee status trước khi thực hiện action.
* Nếu employee active thì có thể reactivate LMS account.
* Nếu employee không active hoặc không xác minh được thì chuyển manual review.

---

## Automation workflow

Workflow tổng quát:

```text
Odoo Ticket
    ↓
Read title, description, requester email
    ↓
Detect Login Issue
    ↓
Check HR demo data
    ↓
If employee is active
    → Reactivate LMS account
    → Add Odoo note/tag
    → Update ticket stage
    ↓
If employee is not active or cannot be verified
    → Add manual review note/tag
    → Keep ticket for support review
```

---

## Odoo integration

Automation có hai cách tích hợp với Odoo:

### 1. Scheduled job

File liên quan:

```text
login-issue-automation/src/run_scheduled_odoo.py
```

Cách chạy này dùng để script định kỳ đọc ticket từ Odoo, lọc các ticket Login Issue chưa xử lý, sau đó chạy workflow automation.

### 2. Webhook

File liên quan:

```text
login-issue-automation/src/webhook_server.py
```

Cách này dùng để nhận event khi Odoo có ticket mới, sau đó chạy automation cho ticket đó.

Trong bản demo/training, phần HR và LMS được mô phỏng bằng demo data và service local. Tuy nhiên phần Odoo integration được tách riêng qua `odoo_api_client.py` để thể hiện cách đọc ticket, thêm note, thêm tag và update stage trên Odoo.

---

## Evidence cho automation trên Odoo

Phần reporting/analysis sử dụng file data mẫu là đủ.
Riêng phần automation nên có evidence chạy trên ticket Odoo thật.

Các screenshot nên bổ sung vào:

```text
evidence/screenshots/
```

Gợi ý evidence:

```text
before-automation-ticket.png
terminal-run-automation.png
after-automation-ticket.png
```

Trong đó:

* `before-automation-ticket.png`: ticket Login Issue trước khi chạy automation.
* `terminal-run-automation.png`: terminal khi chạy script automation.
* `after-automation-ticket.png`: ticket sau khi automation cập nhật note/tag/stage.

Điều này chứng minh automation không chỉ chạy mock local, mà được thiết kế để xử lý ticket Odoo của mình.

---

## HR demo data

File HR demo data:

```text
login-issue-automation/data/hr_demo.json
```

Email demo sử dụng domain:

```text
@mindx.com
```

Automation chỉ tự động xử lý khi employee status là:

```text
active
```

Các trạng thái khác như `terminated`, `inactive`, `locked`, `suspended`, `contractor`, `unknown` sẽ được chuyển sang manual review để tránh rủi ro về access control.

---

## Cách chạy demo local

Vào folder automation:

```bash
cd login-issue-automation
```

Chạy demo workflow local:

```bash
python src/automation_demo.py
```

Chạy test:

```bash
python -m pytest tests/
```

Kết quả demo và test được lưu tại:

```text
demo-output.txt
test-output.txt
logs/automation.log
```

---

## Cách chạy với Odoo API

Tạo file `.env` từ file mẫu:

```bash
cp config/config.example.env .env
```

Cập nhật các thông tin Odoo:

```env
ODOO_URL=
ODOO_DB=
ODOO_USERNAME=
ODOO_API_KEY=
ODOO_HELPDESK_MODEL=helpdesk.ticket
ODOO_SOLVED_STAGE_ID=
ODOO_MANUAL_REVIEW_STAGE_ID=
DRY_RUN=true
```

Chạy scheduled job:

```bash
python src/run_scheduled_odoo.py
```

Lưu ý: nên để `DRY_RUN=true` khi test lần đầu để tránh update nhầm ticket.

---

## Test coverage

Các test case chính:

| Case                                    | Expected result        |
| --------------------------------------- | ---------------------- |
| Login Issue + active employee           | Reactivate LMS account |
| Login Issue + terminated employee       | Manual review          |
| Login Issue + unknown employee          | Manual review          |
| Login Issue + locked/suspended employee | Manual review          |
| Non-login issue                         | Skip                   |
| Missing requester email                 | Manual review          |

---

## Kết quả chính

Bài nộp này đã hoàn thành các phần:

* Reporting từ file `doc/plans/data/sample.xlsx`.
* Pattern analysis và impact analysis.
* Findings, recommendations và action plan.
* Automation workflow cho Login Issue.
* Odoo API/webhook integration structure.
* HR demo data với nhiều employee status.
* Test cases, logs và documentation.
* Evidence folder để bổ sung screenshot chạy trên Odoo ticket thật.

