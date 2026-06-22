# Operation Guide

## 1. Chạy demo

```bash
python src/automation_demo.py
```

## 2. Chạy test

```bash
python -m unittest discover -s tests
```

## 3. Chạy với Odoo API thật

```bash
cp config/config.example.env config/.env
# sửa config/.env
python src/run_scheduled_odoo.py
```

## 4. Chạy webhook

```bash
python src/webhook_server.py
```

Test webhook:

```bash
curl -X POST http://localhost:8080/webhook/odoo-ticket \
  -H "Content-Type: application/json" \
  -H "X-Webhook-Secret: change-this-secret" \
  -d '{"ticket_id":"00001","title":"Cannot login to LMS","description":"Account disabled","requester_email":"teacher01@mindx.com"}'
```

## 5. Troubleshooting

| Lỗi | Cách xử lý |
|---|---|
| Không có logs | Tạo folder `logs` |
| Odoo auth failed | Kiểm tra URL/DB/username/API key |
| Ticket không update | Kiểm tra stage ID và quyền Odoo |
| Không detect login | Bổ sung keyword trong `detector.py` |
| Tất cả manual review | Kiểm tra HR data / HR API |
