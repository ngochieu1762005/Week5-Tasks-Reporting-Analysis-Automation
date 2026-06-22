# Thiết kế Login Issue Automation Workflow

## 1. Mục tiêu

Tự động xử lý ticket Login Issue an toàn, có kiểm tra HR trước khi reactivate LMS account.

## 2. Workflow

```text
Start
  ↓
Get ticket from Odoo API/Webhook
  ↓
Detect login issue by keyword
  ↓
Security risk?
  ├─ Yes → Manual review
  └─ No
      ↓
    Is login issue?
      ├─ No → automation-skipped
      └─ Yes
          ↓
        Requester email exists?
          ├─ No → Manual review
          └─ Yes
              ↓
            Check HR status
              ↓
            Active?
              ├─ Yes → Reactivate LMS → Send response → Update Odoo Solved
              ├─ Terminated → Manual review
              └─ Unknown/Error → Manual review
```

## 3. Boundary

Automation chỉ reactivate nếu employee status là `active`. Mọi trường hợp khác đều manual review.
