# KB: LMS Login Issue / Account Reactivation

## 1. Triệu chứng

- Không đăng nhập được LMS
- Cannot login to LMS
- Account disabled / locked / inactive
- Không truy cập được tài khoản
- Quên mật khẩu

## 2. Quy trình xử lý

1. Kiểm tra requester email.
2. Xác định ticket có phải Login Issue không.
3. Check employee status trong HR.
4. Nếu active: reactivate LMS account.
5. Nếu terminated/unknown: manual review.
6. Gửi response cho user.
7. Ghi note vào Odoo.

## 3. Template phản hồi khi xử lý xong

```text
Xin chào,

Tài khoản LMS của bạn đã được kiểm tra và kích hoạt lại. Vui lòng thử đăng nhập lại vào hệ thống.

Nếu bạn vẫn gặp lỗi, vui lòng phản hồi trực tiếp trong ticket này để support tiếp tục kiểm tra.

Trân trọng,
Support Team
```

## 4. Template manual review

```text
Xin chào,

Chúng tôi đã nhận được yêu cầu hỗ trợ đăng nhập LMS của bạn. Ticket đang được chuyển sang bước kiểm tra thủ công để xác minh thêm thông tin trước khi thực hiện thay đổi tài khoản.

Trân trọng,
Support Team
```
