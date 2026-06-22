# Thiết kế Login Issue Automation Workflow

## 1. Mục tiêu

Tự động xử lý ticket Login Issue an toàn, có kiểm tra HR trước khi reactivate LMS account.

Trong bản demo này, dữ liệu HR được lưu tại `data/hr_demo.json`. Email test dùng domain `@mindx.com` để giống môi trường nội bộ hơn.

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
            Employee status?
              ├─ active → Reactivate LMS → Send response → Update Odoo Solved
              ├─ terminated → Manual review
              └─ other/unknown/error → Manual review
```

## 3. HR status policy

| HR status | Automation action | Lý do |
|---|---|---|
| `active` | Reactivate LMS account | Đủ điều kiện xử lý tự động |
| `terminated` | Manual review | Không được tự động khôi phục quyền truy cập |
| `unknown` | Manual review | Không xác minh được user |
| `inactive` | Manual review | Cần kiểm tra lại trạng thái thực tế |
| `locked` | Manual review | Có thể liên quan policy/security |
| `suspended` | Manual review | Không nên tự động mở lại account |
| `on_leave` | Manual review | Cần xác nhận quyền truy cập trong thời gian nghỉ |
| `contractor` | Manual review | Có thể có policy riêng |
| `probation` | Manual review | Demo chọn hướng an toàn, cần xác nhận policy |
| `resigned` | Manual review | Không được tự động khôi phục quyền truy cập |

## 4. Boundary

Automation chỉ reactivate nếu employee status là `active`. Mọi trạng thái khác đều đi về manual review để tránh rủi ro access control.
