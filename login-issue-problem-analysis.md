# Week 5 - Phân tích Login Issue

## 1. Selected issue

| Field | Value |
|---|---|
| Scenario | Scenario 1 - Login Issue |
| Ticket | LMS Login Issue - Teacher cannot access account |
| Category | Login / Account Access |
| Class of Service | Standard |
| Priority | 1 sao |
| Users affected | 1 |
| Status | Solved |

## 2. Mô tả vấn đề

User không thể đăng nhập LMS. Các mô tả thường gặp:

- Cannot login to LMS
- Account disabled/locked/inactive
- Cannot access account
- Không đăng nhập được LMS
- Tài khoản bị khóa

Nếu user là teacher, issue này ảnh hưởng đến việc truy cập lớp học, tài liệu và quản lý học viên.

## 3. Manual process hiện tại

1. Support nhận ticket trong Odoo.
2. Đọc title/description để xác định login issue.
3. Lấy requester email.
4. Check employee status trong HR system.
5. Nếu employee active, reactivate LMS account.
6. Nếu employee terminated/unknown, chuyển manual review.
7. Gửi phản hồi user.
8. Ghi note vào Odoo.
9. Chuyển ticket sang Solved nếu xử lý xong.

## 4. Vấn đề của manual process

- Lặp lại nhiều bước giống nhau.
- Tốn 5-10 phút/ticket.
- Dễ thiếu note/log nếu xử lý nhanh.
- Response time phụ thuộc vào support availability.
- Nếu login ticket tăng, workload tăng.

## 5. Vì sao automation tốt hơn trong ngắn hạn

Root cause có thể liên quan đến rule deactivate account sau 30 ngày không hoạt động. Sửa code tận gốc cần dev team, testing và deployment.

Automation là giải pháp nhanh hơn vì:

- Không cần sửa code LMS ngay.
- Xử lý được 80%+ case rõ ràng.
- Có thể giữ boundary an toàn.
- Giúp support tập trung vào issue khó hơn.

## 6. Automation boundary

Automation chỉ reactivate khi:

- Ticket là Login Issue.
- Có requester email.
- HR status = active.
- LMS reactivation thành công.

Automation không reactivate khi:

- Employee terminated.
- Employee unknown.
- Thiếu email.
- HR/LMS/Odoo API lỗi.
- Có dấu hiệu security/access risk.

## 7. Kết luận

Login Issue phù hợp automation vì workflow rõ ràng, rủi ro có thể kiểm soát, và có thể tích hợp với Odoo API/Webhook để xử lý ticket tự động.
