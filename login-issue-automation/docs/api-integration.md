# API / Webhook Integration Documentation

## 1. Mục tiêu

Tài liệu này giải thích rõ phần tích hợp Odoo API/Webhook để đáp ứng acceptance criteria:

> Workflow integrates with Odoo ticket system (webhook/API)

Package này có cả 2 phương án:

1. **Odoo XML-RPC API** cho scheduled job
2. **Webhook server** cho event-based integration

---

## 2. Odoo API Integration

File chính:

```text
src/odoo_api_client.py
```

Client này hỗ trợ:

| Function | Mục đích |
|---|---|
| `authenticate()` | Đăng nhập Odoo bằng database, username, API key |
| `search_new_tickets()` | Tìm ticket chưa xử lý |
| `read_ticket()` | Đọc title, description, requester email, priority, stage, tags |
| `add_internal_note()` | Ghi note vào ticket |
| `send_message_to_requester()` | Gửi message cho requester qua Odoo chatter |
| `update_stage()` | Chuyển ticket sang Solved / Manual Review |
| `add_tag_by_name()` | Gắn tag automation-processed/manual-review |

---

## 3. Scheduled Job Flow

File chính:

```text
src/run_scheduled_odoo.py
```

Flow:

```text
Run scheduled job
    ↓
Connect Odoo API
    ↓
Search unprocessed tickets
    ↓
Read each ticket
    ↓
Normalize Odoo data
    ↓
Run LoginAutomationService
    ↓
Update Odoo via API
```

Dùng khi muốn chạy định kỳ, ví dụ mỗi 5-10 phút.

---

## 4. Webhook Integration

File chính:

```text
src/webhook_server.py
```

Endpoint:

```text
POST /webhook/odoo-ticket
```

Header bảo mật:

```text
X-Webhook-Secret: <secret>
```

Payload mẫu:

```json
{
  "ticket_id": "00001",
  "title": "LMS Login Issue - Teacher cannot access account",
  "description": "Teacher cannot login to LMS. Account seems disabled.",
  "requester_email": "teacher01@mindx.com",
  "priority": "1 star",
  "stage": "New",
  "tags": ["lms", "login"]
}
```

Response mẫu:

```json
{
  "ticket_id": "00001",
  "result": "resolved_by_automation",
  "employee_status": "active",
  "action": "lms_account_reactivated",
  "message_sent": true,
  "odoo_updated": true
}
```

---

## 5. Config

File mẫu:

```text
config/config.example.env
```

Các biến quan trọng:

```text
ODOO_URL=
ODOO_DB=
ODOO_USERNAME=
ODOO_API_KEY=
ODOO_HELPDESK_MODEL=helpdesk.ticket
ODOO_SOLVED_STAGE_ID=
ODOO_MANUAL_REVIEW_STAGE_ID=
DRY_RUN=true
WEBHOOK_SECRET=
```

Trong training nên để `DRY_RUN=true`. Khi production mới đổi `DRY_RUN=false`.

---

## 6. Safety

Automation có các rule an toàn:

- Không reactivate nếu không phải Login Issue.
- Không reactivate nếu thiếu email.
- Không reactivate nếu employee terminated/unknown.
- Không reactivate nếu có security keyword.
- Không reactivate nếu LMS API fail.
- Các case rủi ro đều gắn tag `manual-review`.

---

## 7. Kết luận

Package này không chỉ mô phỏng bằng function mà có sẵn cấu trúc API/Webhook rõ ràng. Khi có Odoo thật, chỉ cần điền `.env`, map đúng stage ID/tag model, và chạy scheduled job hoặc webhook server.
