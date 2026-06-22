# Week 5 - Tổng quan

## Mục tiêu

Week 5 thêm lớp phân tích dữ liệu lên trên hoạt động xử lý ticket của Week 4. Thay vì chỉ xử lý từng ticket riêng lẻ, mục tiêu là dùng dữ liệu ticket để tìm pattern, xác định vấn đề lặp lại, phân tích impact và đề xuất cải tiến.

## Quy trình tổng quát

```text
Ticket Data
    ↓
Odoo Reports
    ↓
Pattern Analysis
    ↓
Impact + Root Cause Analysis
    ↓
Recommendations
    ↓
Automation Implementation
    ↓
Monitoring
```

## Deliverables chính

| Phần | Deliverable |
|---|---|
| Data preparation | Week 4 ticket data summary |
| Reporting | Daily summary, team performance, category analysis, ticket trend |
| Analysis | Top recurring issues, impact, root cause |
| Findings | Recommendations + action plan |
| Automation | Login Issue automation workflow |
| Integration | Odoo API/Webhook documentation and code |
| Testing | Test results |
| Presentation | Final presentation outline |

## Ghi chú

Dữ liệu Week 4 là training/demo dataset gồm 6 ticket, vì vậy một số chỉ số như response time và resolution time có thể chưa được Odoo đo tự động. Trong trường hợp này, report ghi rõ limitation và dùng stage/status + impact data làm operational metrics chính.
