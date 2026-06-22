# Login Issue Automation - Week 5

## Mục tiêu

Automation này xử lý Scenario 1 - Login Issue theo Operating Engineer approach.

Workflow:

```text
Odoo Ticket → Analyze ticket content → Check HR → Reactivate LMS / Manual Review → Update Odoo → Send response
```

## Cách chạy demo không cần Odoo thật

```bash
python src/automation_demo.py
```

## Cách chạy test

```bash
python -m unittest discover -s tests
```

## Cách chạy với Odoo API thật

1. Copy config:

```bash
cp config/config.example.env config/.env
```

2. Điền thông tin Odoo.

3. Chạy scheduled job:

```bash
python src/run_scheduled_odoo.py
```

## Cách chạy webhook server

```bash
python src/webhook_server.py
```

Endpoint:

```text
POST http://localhost:8080/webhook/odoo-ticket
```

## File quan trọng

| File | Mục đích |
|---|---|
| `src/login_automation_service.py` | Core workflow logic |
| `src/odoo_api_client.py` | Odoo XML-RPC API client |
| `src/run_scheduled_odoo.py` | Scheduled job runner |
| `src/webhook_server.py` | Webhook endpoint |
| `src/hr_client.py` | HR check demo/API abstraction |
| `src/lms_client.py` | LMS reactivation demo/API abstraction |
| `docs/api-integration.md` | Giải thích API/Webhook integration |
